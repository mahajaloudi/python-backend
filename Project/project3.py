
import os
from PIL import Image
from concurrent.futures import ThreadPoolExecutor


class ImageProcessor:
    def __init__(self, input_dir, output_dir):
        self.input_dir = input_dir
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def _get_images(self):
        """Find all image files in the input directory"""
        valid_extensions = (".jpg", ".jpeg", ".png", ".bmp", ".gif")
        return [
            os.path.join(self.input_dir, f)
            for f in os.listdir(self.input_dir)
            if f.lower().endswith(valid_extensions)
        ]

    def resize(self, width, height):
        """Resize images to specific dimensions"""
        images = self._get_images()
        for img_path in images:
            try:
                with Image.open(img_path) as img:
                    resized = img.resize((width, height))
                    filename = os.path.basename(img_path)
                    resized.save(os.path.join(self.output_dir, filename))
                    print(f"✅ Resized {filename}")
            except Exception as e:
                print(f"❌ Error resizing {img_path}: {e}")

    def grayscale(self):
        """Convert images to grayscale"""
        images = self._get_images()
        for img_path in images:
            try:
                with Image.open(img_path) as img:
                    gray = img.convert("L")
                    filename = os.path.basename(img_path)
                    gray.save(os.path.join(self.output_dir, filename))
                    print(f"✅ Grayscale {filename}")
            except Exception as e:
                print(f"❌ Error grayscaling {img_path}: {e}")

    def rotate(self, angle):
        """Rotate images by a specified angle"""
        images = self._get_images()
        for img_path in images:
            try:
                with Image.open(img_path) as img:
                    rotated = img.rotate(angle, expand=True)
                    filename = os.path.basename(img_path)
                    rotated.save(os.path.join(self.output_dir, filename))
                    print(f"✅ Rotated {filename}")
            except Exception as e:
                print(f"❌ Error rotating {img_path}: {e}")

    def process_concurrent(self, func, *args):
        """Process images in parallel using threads"""
        images = self._get_images()
        with ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(func, img_path, *args) for img_path in images
            ]
            for future in futures:
                future.result()

    def watermark(self, text, position=(10, 10)):
        """Add a simple text watermark"""
        from PIL import ImageDraw, ImageFont

        images = self._get_images()
        for img_path in images:
            try:
                with Image.open(img_path) as img:
                    draw = ImageDraw.Draw(img)
                    font = ImageFont.load_default()
                    draw.text(position, text, fill="white", font=font)
                    filename = os.path.basename(img_path)
                    img.save(os.path.join(self.output_dir, filename))
                    print(f"✅ Watermarked {filename}")
            except Exception as e:
                print(f"❌ Error watermarking {img_path}: {e}")



def main():
    input_dir = input("Enter input directory: ").strip()
    output_dir = input("Enter output directory: ").strip()
    processor = ImageProcessor(input_dir, output_dir)

    while True:
        print("\n=== Image Processing Utility ===")
        print("1. Resize Images")
        print("2. Convert to Grayscale")
        print("3. Rotate Images")
        print("4. Add Watermark")
        print("5. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            w = int(input("Enter width: "))
            h = int(input("Enter height: "))
            processor.resize(w, h)
        elif choice == "2":
            processor.grayscale()
        elif choice == "3":
            angle = int(input("Enter rotation angle: "))
            processor.rotate(angle)
        elif choice == "4":
            text = input("Enter watermark text: ")
            processor.watermark(text)
        elif choice == "5":
            print("👋 Exiting Image Processor...")
            break
        else:
            print("❌ Invalid choice, try again.")


if __name__ == "__main__":
    main()
