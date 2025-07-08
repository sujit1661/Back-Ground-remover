from rembg import remove
from PIL import Image
import os
input_path = input("Enter the image file path: ").strip()
if not os.path.isfile(input_path):
    print("Error: File not found!")
else:
    image = Image.open(input_path)
    output_image = remove(image)
    output_path = os.path.splitext(input_path)[0] + "_no_bg.png"
    output_image.save(output_path)
    print(f"✅ Background removed successfully!\n📂 Image saved as: {output_path}")
