"""User-authorized exact staff-head montage and localized mouth integration.

Requires the bundled Pillow and NumPy runtime. Never overwrites source assets.
The generative face-crop result is preserved separately and only its mouth is used.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import hashlib
import json
import math

import numpy as np
from PIL import Image, ImageChops, ImageDraw, ImageFilter

SCENE = Path(__file__).resolve().parents[1]
PROJECT = SCENE.parents[2]
WORK = SCENE / "work/v04"
WORK.mkdir(parents=True, exist_ok=True)
OUTPUT = WORK / "montage-v01.png"
if OUTPUT.exists():
    raise FileExistsError("Preserve the existing montage; choose a new output version.")

base_path = SCENE / "finals/r01-02/final-v03.png"
staff_path = PROJECT / "characters/holly_willhelm/warcraft-warpath-style/holly_willhelm-base_blue_staff_three_quarter.png"
face_path = SCENE / "finals/r01-02/v04-face/face-v01.png"
base = Image.open(base_path).convert("RGBA")
size = base.size

# The old malformed head covers sky only. Recover that sky locally using fixed
# boundary colors and harmonic interpolation, without changing the shaft below it.
head_mask = Image.new("L", size)
ImageDraw.Draw(head_mask).polygon(
    [(744, 9), (758, 12), (767, 50), (835, 76), (836, 95),
     (795, 117), (788, 167), (756, 174), (712, 169), (699, 183),
     (682, 186), (670, 178), (684, 147), (679, 120), (656, 107),
     (657, 88), (687, 75), (710, 57), (735, 44)], fill=255)
head_mask = head_mask.filter(ImageFilter.MaxFilter(7))
repair_box = (648, 0, 845, 205)
region = np.asarray(base.crop(repair_box).convert("RGB"), dtype=np.float32).copy()
fixed = region.copy()
mask = np.asarray(head_mask.crop(repair_box)) > 0
for y in range(region.shape[0]):
    xs = np.flatnonzero(mask[y])
    if xs.size:
        left, right = int(xs[0]) - 1, int(xs[-1]) + 1
        for x in xs:
            t = (x - left) / (right - left)
            region[y, x] = fixed[y, left] * (1 - t) + fixed[y, right] * t
for _ in range(1600):
    neighbors = (np.roll(region, 1, 0) + np.roll(region, -1, 0)
                 + np.roll(region, 1, 1) + np.roll(region, -1, 1)) * 0.25
    region[mask] = neighbors[mask]
sky_patch = Image.fromarray(np.clip(region, 0, 255).astype(np.uint8)).convert("RGBA")
sky_layer = base.copy()
sky_layer.paste(sky_patch, repair_box[:2])
repair_mask = head_mask.filter(ImageFilter.GaussianBlur(0.7))
repaired = Image.composite(sky_layer, base, repair_mask)

# Isolate the original head and its corner socket, preserving the rigid design.
staff = Image.open(staff_path).convert("RGBA")
source_crop = (1450, 180, 1944, 560)
source_mask = Image.new("L", staff.size)
ImageDraw.Draw(source_mask).rectangle(source_crop, fill=255)
alpha = ImageChops.multiply(staff.getchannel("A"), source_mask)
alpha = alpha.point(lambda a: 0 if a < 32 else min(255, round((a - 32) * 255 / 223)))
staff.putalpha(alpha)

# A similarity transform uses uniform scale and rotation, never warping the head.
scale = 0.4
angle_degrees = -46.0
z = scale * complex(math.cos(math.radians(angle_degrees)), math.sin(math.radians(angle_degrees)))
source_anchor = complex(1480, 355)
target_anchor = complex(689, 170)
translation = target_anchor - z * source_anchor
inv = 1 / z
off = -translation / z
matrix = (inv.real, -inv.imag, off.real, inv.imag, inv.real, off.imag)
head_layer = staff.convert("RGBa").transform(
    size, Image.Transform.AFFINE, matrix,
    resample=Image.Resampling.BICUBIC).convert("RGBA")

# Apply a single restrained night-light color transform to the complete source
# head; its positions, gem count, contours and internal construction are unchanged.
pixels = np.asarray(head_layer).copy()
pixels[:, :, :3] = np.clip(pixels[:, :, :3].astype(np.float32) * 0.86
                           + np.array([2, 4, 4], dtype=np.float32), 0, 255).astype(np.uint8)
head_layer = Image.fromarray(pixels)
result = Image.alpha_composite(repaired, head_layer)

# The generated face patch is mapped back to its original square, but only a
# small feathered mouth region is allowed to affect the final scene.
face_box = (510, 180, 670, 340)
face_patch = Image.open(face_path).convert("RGBA").resize((160, 160), Image.Resampling.LANCZOS)
face_layer = base.copy()
face_layer.paste(face_patch, face_box[:2])
mouth_mask = Image.new("L", size)
ImageDraw.Draw(mouth_mask).polygon(
    [(576, 268), (611, 270), (612, 284), (598, 292), (580, 285)], fill=255)
mouth_mask = mouth_mask.filter(ImageFilter.GaussianBlur(1.2))
result = Image.composite(face_layer, result, mouth_mask)

authorized_mask = ImageChops.lighter(repair_mask, head_layer.getchannel("A"))
authorized_mask = ImageChops.lighter(authorized_mask, mouth_mask)
outside = authorized_mask.point(lambda a: 255 if a == 0 else 0)
difference = ImageChops.difference(result, base)
assert all(ImageChops.multiply(c, outside).getbbox() is None for c in difference.split())
assert result.size == base.size == (1942, 809)
assert result.getchannel("A").getextrema() == (255, 255)

result.save(OUTPUT)
head_layer.save(WORK / "head-layer.png")
repair_mask.save(WORK / "head-repair-mask.png")
mouth_mask.save(WORK / "mouth-edit-mask.png")
authorized_mask.save(WORK / "authorized-edit-mask.png")
result.crop((650, 0, 845, 240)).resize((780, 960), Image.Resampling.LANCZOS).save(WORK / "head-montage-review-4x.png")
result.crop(face_box).resize((960, 960), Image.Resampling.LANCZOS).save(WORK / "face-montage-review-6x.png")

sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
record = {
    "method": "user-authorized non-generative exact head montage and local generated-mouth integration",
    "user_authorization": "Sí, montaje exacto y retoque del rostro (recomendado)",
    "recorded_at": datetime.now(timezone.utc).astimezone(timezone(timedelta(hours=1))).isoformat(),
    "timezone": "Europe/Madrid",
    "base_file": str(base_path), "base_sha256": sha(base_path),
    "staff_file": str(staff_path), "staff_sha256": sha(staff_path),
    "face_file": str(face_path), "face_sha256": sha(face_path),
    "source_head_crop": source_crop,
    "rigid_transform": {"uniform_scale": scale, "rotation_degrees_image_coordinates": angle_degrees,
                        "source_anchor": [source_anchor.real, source_anchor.imag],
                        "target_anchor": [target_anchor.real, target_anchor.imag],
                        "inverse_affine_matrix": matrix},
    "alpha_cleanup": "source alpha below32 removed, remaining alpha remapped linearly; premultiplied-alpha affine resampling",
    "head_color_transform": {"uniform_rgb_scale": 0.86, "rgb_offset": [2, 4, 4]},
    "sky_reconstruction": "fixed-boundary harmonic interpolation inside only old-head mask, 1600 iterations",
    "face_source_box": face_box, "face_target_size": [160, 160],
    "mouth_mask_polygon": [[576, 268], [611, 270], [612, 284], [598, 292], [580, 285]],
    "outside_authorized_mask_pixels_unchanged": True,
    "output_file": str(OUTPUT), "output_sha256": sha(OUTPUT),
    "dimensions": [1942, 809], "visual_review_pending": True
}
(WORK / "montage-v01.json").write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"output": str(OUTPUT), "sha256": record["output_sha256"], "outside_regions_unchanged": True}))
