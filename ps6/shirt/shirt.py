import sys
import os
from PIL import Image, ImageOps

# Ensures there are 2 arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")


in_file = sys.argv[1]
out_file = sys.argv[2]
ext = os.path.splitext(in_file)[1]

# Ensures the file paths end with a valid extension and
# both files have the same extension
if ext != ".jpg" and ext != ".jpeg" and ext != ".png":
    sys.exit("Invalid input")
elif out_file.endswith(ext) == False:
    sys.exit("Input and output have different extensions")

# Creates new image
try:
    # Opens images
    overlay = Image.open("shirt.png")
    im = Image.open(in_file)

    # Crop and resize
    im = ImageOps.fit(im, overlay.size, method=Image.Resampling.BICUBIC, bleed=0.0, centering=(0.5, 0.5))

    # Overlay the shirt
    im.paste(overlay, box=None, mask=overlay)

    # Save image
    im.save(out_file)
except FileNotFoundError:
    sys.exit("File does not exist")