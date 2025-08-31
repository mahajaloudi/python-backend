
import numpy as np
import pandas as pd
from PIL import Image, ImageFilter


print("=== NumPy Example ===")
arr = np.array([10, 20, 30, 40, 50])
print("Original Array:", arr)
print("Array + 5:", arr + 5)
print("Mean:", np.mean(arr))
print("Standard Deviation:", np.std(arr))
print()


print("=== Pandas Example ===")

df = pd.read_csv("dataset.csv")

print("\nDataset:\n", df)
print("\nBasic Statistics:\n", df.describe())


high_scorers = df[df["Score"] > 85]
print("\nStudents with Score > 85:\n", high_scorers)


print("\nAverage Age:", df["Age"].mean())


high_scorers.to_csv("high_scorers.csv", index=False)
print("\nFiltered data saved to high_scorers.csv")
print()


print("=== Pillow Example ===")
try:
    
    img = Image.open("input.jpg")
    print("Original image mode:", img.mode)
    print("Original image size:", img.size)

    
    gray_img = img.convert("L")
    gray_img.save("output_gray.jpg")
    print("Grayscale image saved as output_gray.jpg")

    
    resized_img = img.resize((200, 200))
    resized_img.save("output_resized.jpg")
    print("Resized image saved as output_resized.jpg")

    
    blurred_img = img.filter(ImageFilter.BLUR)
    blurred_img.save("output_blur.jpg")
    print("Blurred image saved as output_blur.jpg")

except FileNotFoundError:
    print("⚠️ Please make sure 'input.jpg' exists in the folder.")

print("\n=== Task Completed ✅ ===")
