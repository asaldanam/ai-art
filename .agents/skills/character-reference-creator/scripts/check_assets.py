"""Read-only checks for a character style manifest and its saved PNG assets."""

import argparse
import hashlib
import json
from pathlib import Path


REQUIRED_VIEWS = {
    "midshot", "fullbody_front", "fullbody_profile", "fullbody_back",
    "fullbody_three_quarter", "head_front", "head_profile",
    "head_three_quarter", "head_back",
}
ACTIVE = {"pending_review", "approved"}
KINDS = {"candidate", "reference", "detail"}
STATUSES = ACTIVE | {"selected", "not_selected", "rejected", "superseded"}


def check_manifest(manifest_path, outfit_id=None, complete=False):
    """Return diagnostics; never write files or infer user approvals."""
    errors = []
    manifest_path = Path(manifest_path).resolve()
    try:
        data = json.loads(manifest_path.read_text(encoding="utf-8-sig"))
    except (OSError, ValueError) as exc:
        return [f"Cannot read manifest: {exc}"]
    if not isinstance(data, dict) or data.get("schema_version") != 1:
        return ["Expected a manifest object with schema_version 1."]
    images, outfits = data.get("images"), data.get("outfits")
    if not isinstance(images, list) or not isinstance(outfits, list):
        return ["images and outfits must be lists."]

    jobs = {}
    for job in outfits:
        if not isinstance(job, dict) or not isinstance(job.get("id"), str):
            errors.append("Each outfit must be an object with a string id.")
            continue
        if job["id"] in jobs:
            errors.append(f"Duplicate outfit id: {job['id']}")
        jobs[job["id"]] = job
    if outfit_id is not None and outfit_id not in jobs:
        errors.append(f"Unknown outfit: {outfit_id}")

    try:
        from PIL import Image
    except ImportError:
        return errors + ["Pillow is required: use a Python environment with Pillow installed."]

    def asset_path(value, label):
        if not isinstance(value, str) or not value:
            errors.append(f"{label}: expected a relative file path.")
            return None
        relative = Path(value)
        path = (manifest_path.parent / relative).resolve()
        if relative.is_absolute() or not path.is_relative_to(manifest_path.parent):
            errors.append(f"{label}: path must stay inside the style directory.")
            return None
        if not path.is_file():
            errors.append(f"{label}: missing file {value}")
            return None
        return path

    by_id, image_paths, used_paths, active_views = {}, {}, set(), set()
    for index, entry in enumerate(images):
        if not isinstance(entry, dict):
            errors.append(f"images[{index}] must be an object.")
            continue
        image_id = entry.get("id")
        if not isinstance(image_id, str) or not image_id or image_id in by_id:
            errors.append(f"images[{index}]: missing or duplicate string id.")
            continue
        by_id[image_id] = entry
        job = jobs.get(entry.get("outfit_id"))
        if job is None:
            errors.append(f"{image_id}: unknown outfit_id.")
        if entry.get("kind") not in KINDS or entry.get("status") not in STATUSES:
            errors.append(f"{image_id}: invalid kind or status.")
        revision = entry.get("identity_revision")
        if type(revision) is not int or revision < 1:
            errors.append(f"{image_id}: identity_revision must be a positive integer.")
        asset_path(entry.get("prompt_file"), f"{image_id} prompt")
        path = asset_path(entry.get("file"), image_id)
        if path is None:
            continue
        if path in used_paths:
            errors.append(f"{image_id}: PNG file already registered by another image.")
        used_paths.add(path)
        image_paths[image_id] = path
        active = entry.get("kind") in {"reference", "detail"} and entry.get("status") in ACTIVE
        current = job is not None and revision == job.get("identity_revision")
        if active and current and entry.get("kind") == "reference":
            key = (entry.get("outfit_id"), entry.get("view"))
            if key in active_views:
                errors.append(f"{image_id}: duplicate active reference view {key}.")
            active_views.add(key)
        try:
            with Image.open(path) as image:
                if image.format != "PNG" or path.suffix.lower() != ".png":
                    errors.append(f"{image_id}: expected an actual .png file.")
                image.load()
                if active:
                    low, high = image.convert("RGBA").getchannel("A").getextrema()
                    if low != 0 or high == 0:
                        errors.append(f"{image_id}: needs transparent pixels and visible content.")
        except (OSError, ValueError) as exc:
            errors.append(f"{image_id}: unreadable image: {exc}")

    for image_id, entry in by_id.items():
        refs = entry.get("reference_image_ids", [])
        if not isinstance(refs, list) or any(not isinstance(ref, str) or ref not in by_id for ref in refs):
            errors.append(f"{image_id}: invalid reference_image_ids.")
        derived = entry.get("derived_from")
        if derived is not None and (not isinstance(derived, str) or derived not in by_id):
            errors.append(f"{image_id}: unknown derived_from image.")

    if complete:
        target_jobs = [jobs[outfit_id]] if outfit_id in jobs else list(jobs.values()) if outfit_id is None else []
        if not target_jobs:
            errors.append("No outfits to check for completeness.")
        for job in target_jobs:
            job_id, revision = job["id"], job.get("identity_revision")
            current = [entry for entry in by_id.values()
                       if entry.get("outfit_id") == job_id and entry.get("identity_revision") == revision]
            views = {entry.get("view") for entry in current
                     if entry.get("kind") == "reference" and entry.get("status") in ACTIVE}
            missing = REQUIRED_VIEWS - views
            if missing:
                errors.append(f"{job_id}: missing views: {', '.join(sorted(missing))}")
            candidates = [entry for entry in current if entry.get("kind") == "candidate"
                          and entry.get("candidate_round") == job.get("candidate_round")
                          and entry.get("status") != "superseded"]
            if len(candidates) != 3:
                errors.append(f"{job_id}: expected exactly three candidates in the current round.")
            selected = [entry for entry in candidates if entry.get("status") == "selected"]
            chosen = by_id.get(job.get("selected_candidate_id"))
            master = by_id.get(job.get("master_reference_id"))
            if len(selected) != 1 or chosen is None or chosen not in selected:
                errors.append(f"{job_id}: expected one selected current candidate matching selected_candidate_id.")
            if (master is None or master not in current or master.get("kind") != "reference"
                    or master.get("view") != "midshot" or master.get("status") not in ACTIVE
                    or master.get("derived_from") != job.get("selected_candidate_id")):
                errors.append(f"{job_id}: master_reference_id must identify the active midshot copy.")
            elif chosen is not None:
                source = image_paths.get(chosen["id"])
                target = image_paths.get(master["id"])
                if source and target and hashlib.sha256(source.read_bytes()).digest() != hashlib.sha256(target.read_bytes()).digest():
                    errors.append(f"{job_id}: master PNG must be an unchanged copy of the selected candidate.")
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", type=Path)
    parser.add_argument("--outfit", help="Outfit ID to require when checking completeness")
    parser.add_argument("--complete", action="store_true", help="Require all nine views and the selected anchor")
    args = parser.parse_args()
    errors = check_manifest(args.manifest, args.outfit, args.complete)
    for error in errors:
        print(f"ERROR: {error}")
    if not errors:
        print("Asset checks passed. Visual review and explicit user approval are still required.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
