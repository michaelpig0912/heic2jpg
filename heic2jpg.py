import os
import sys
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()

def convert_to_jpg(input_file, output_file):
    try:
        img = Image.open(input_file)
        img = img.convert("RGB")
        img.save(output_file, "JPEG", quality=95)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error converting {input_file} to {output_file}: {e}")

def main():
    script_directory = os.path.dirname(os.path.abspath(__file__))
    input_directory = os.path.join(script_directory, "image")

    for root, _, files in os.walk(input_directory):
        for file in files:
            file_ext = os.path.splitext(file.lower())[1]
            if file_ext == '.heic':
                input_file = os.path.join(root, file)
                output_file = os.path.splitext(input_file)[0] + ".jpg"
                convert_to_jpg(input_file, output_file)

if __name__ == "__main__":
    main()
