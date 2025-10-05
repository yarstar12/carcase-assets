import os
from PIL import Image

# Папка с исходными изображениями
SRC = "/Users/yaroslavgorskolepov/Desktop/CAR_CASEBOT/cars"
# Папка, куда положим миниатюры (в том же репозитории)
DST = "./thumbs/cars"

# Параметры генерации
MAX_SIZE = 256   # пикселей по большей стороне
QUALITY = 80     # качество WEBP

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

def make_thumb(src_path, dst_path):
    try:
        with Image.open(src_path) as im:
            im = im.convert("RGBA")
            im.thumbnail((MAX_SIZE, MAX_SIZE))
            im.save(dst_path, "WEBP", quality=QUALITY, method=6)
            print("✅", dst_path)
    except Exception as e:
        print("⚠️", src_path, "->", e)

for root, _, files in os.walk(SRC):
    rel = os.path.relpath(root, SRC)
    out_dir = os.path.join(DST, rel)
    ensure_dir(out_dir)
    for f in files:
        if f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
            src = os.path.join(root, f)
            base, _ = os.path.splitext(f)
            dst = os.path.join(out_dir, base + ".webp")
            if not os.path.exists(dst):
                make_thumb(src, dst)

print("✅ Все миниатюры сохранены в:", os.path.abspath(DST))
