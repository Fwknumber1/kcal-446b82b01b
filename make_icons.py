# One-off: draws the app icon (progress ring on dark) at 4x and downsamples. Run: python make_icons.py
from PIL import Image, ImageDraw
BG, TRACK, ACC = (13, 14, 11), (42, 45, 38), (200, 240, 90)
def icon(px):
    s = px * 4
    im = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(im)
    pad, w = int(s * .2), int(s * .1)
    box = (pad, pad, s - pad, s - pad)
    d.arc(box, 0, 360, fill=TRACK, width=w)
    d.arc(box, -90, 160, fill=ACC, width=w)          # ~70% of the ring
    r = w // 2
    import math
    for ang in (-90, 160):                            # round caps
        cx = s / 2 + (s / 2 - pad - r) * math.cos(math.radians(ang))
        cy = s / 2 + (s / 2 - pad - r) * math.sin(math.radians(ang))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=ACC)
    return im.resize((px, px), Image.LANCZOS)
for n in (180, 192, 512):
    icon(n).save(f"icon-{n}.png")
