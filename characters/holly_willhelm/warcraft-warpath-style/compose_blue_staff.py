"""User-authorized non-generative montage of original staff artwork.

Run with Pillow installed. No source assets are overwritten.
"""
from pathlib import Path
import json
from PIL import Image, ImageChops

ROOT = Path(__file__).resolve().parent
SIZE = (1024, 1766)
OFFSET = (0, 200)
SPECS = {
    'front': {
        'staff': 'holly_willhelm-base_blue_staff.png',
        'source_axis': ((35, 395), (1900, 395)),
        'target_axis': ((180, 1200), (850, 70)),
    },
    'three_quarter': {
        'staff': 'holly_willhelm-base_blue_staff_three_quarter.png',
        'source_axis': ((25, 570), (1910, 270)),
        'target_axis': ((220, 1200), (835, 75)),
    },
}


def compose(view, spec):
    base = Image.open(ROOT / f'holly_willhelm_fullbody_{view}.png').convert('RGBA')
    staff = Image.open(ROOT / spec['staff']).convert('RGBA')
    src0, src1 = [complex(*p) for p in spec['source_axis']]
    dst0, dst1 = [complex(*p) for p in spec['target_axis']]
    z = (dst1 - dst0) / (src1 - src0)
    translation = dst0 - z * src0
    inverse = 1 / z
    offset = -translation / z
    matrix = (inverse.real, -inverse.imag, offset.real,
              inverse.imag, inverse.real, offset.imag)
    # Premultiplied-alpha resampling prevents transparent RGB from bleeding.
    layer = staff.convert('RGBa').transform(
        SIZE, Image.Transform.AFFINE, matrix,
        resample=Image.Resampling.BICUBIC).convert('RGBA')
    foreground = Image.new('RGBA', SIZE)
    foreground.paste(base, OFFSET)
    base_alpha = foreground.getchannel('A')
    # Treat the approved solid silhouette as opaque for depth, preserving its
    # original RGBA pixels rather than letting staff show through alpha 253.
    occluder = base_alpha.point(lambda a: min(255, a * 4))
    alpha = ImageChops.multiply(layer.getchannel('A'), ImageChops.invert(occluder))
    layer.putalpha(alpha)
    output = Image.alpha_composite(layer, foreground)
    solid = base_alpha.point(lambda a: 255 if a >= 128 else 0)
    difference = ImageChops.difference(output, foreground)
    unchanged = all(ImageChops.multiply(channel, solid).getbbox() is None
                    for channel in difference.split())
    assert unchanged, 'Approved character pixels changed'
    filename = f'holly_willhelm_base_blue_staff_fullbody_{view}_v05.png'
    output.save(ROOT / filename)
    visible = output.getchannel('A').point(lambda a: 255 if a > 128 else 0)
    box = visible.getbbox()
    assert box and box[0] > 0 and box[1] > 0 and box[2] < SIZE[0] and box[3] < SIZE[1]
    assert output.getchannel('A').getextrema()[0] == 0
    return {'file': filename, 'base': f'holly_willhelm_fullbody_{view}.png',
            **spec, 'canvas_size': SIZE, 'base_offset': OFFSET,
            'inverse_affine': matrix, 'solid_character_pixels_unchanged': unchanged,
            'visible_bbox_alpha_over_128': box,
            'method': 'Pillow similarity transform, original staff behind original character; no generation',
            'approval': 'pending_user_review'}


if __name__ == '__main__':
    report = {v: compose(v, spec) for v, spec in SPECS.items()}
    (ROOT / 'blue_staff_montage.json').write_text(
        json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))
