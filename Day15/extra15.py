
import numpy as np
import pandas as pd
from PIL import Image, ImageFilter

# Exercise 1: 
print("=== Exercise 1: NumPy Array Manipulation ===")


arr = np.random.randint(1, 101, size=(10, 10))
print("Array:\n", arr)


print("\nMean:", np.mean(arr))
print("Median:", np.median(arr))
print("Standard Deviation:", np.std(arr))


print("\nMain Diagonal:", np.diag(arr))


print("\nValues > 80:", arr[arr > 80])


arr[arr < 30] = 0
print("\nArray after replacing values < 30 with 0:\n", arr)



# Exercise 2
print("\n=== Exercise 2: Pandas Data Analysis ===")


data = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Ethan", "Fiona", "George"],
    "Age": [25, 30, 28, 40, 35, 29, 32],
    "Department": ["HR", "IT", "Finance", "IT", "Finance", "HR", "IT"],
    "Salary": [3000, 5000, 4500, 6000, 7000, 3200, 5500]
}
df = pd.DataFrame(data)
print("\nEmployee Data:\n", df)


df["Bonus"] = df["Salary"] * 0.10
print("\nWith Bonus:\n", df)


dept_avg = df.groupby("Department")[["Salary", "Bonus"]].mean()
print("\nAverage Salary and Bonus by Department:\n", dept_avg)


highest_salary = df.loc[df.groupby("Department")["Salary"].idxmax()]
print("\nHighest Salary in Each Department:\n", highest_salary)


df["AgeGroup"] = pd.cut(df["Age"], bins=[20, 30, 40, 50], labels=["20-29", "30-39", "40-49"])
pivot = pd.pivot_table(df, values="Salary", index="Department", columns="AgeGroup", aggfunc="mean")
print("\nPivot Table (Avg Salary by Department & Age Group):\n", pivot)



# Exercise 3:
print("\n=== Exercise 3: Image Filter Application ===")

try:
    
    img = Image.open("input.jpg")

    
    blur = img.filter(ImageFilter.BLUR)
    contour = img.filter(ImageFilter.CONTOUR)
    emboss = img.filter(ImageFilter.EMBOSS)

    
    w, h = img.size
    collage = Image.new("RGB", (w * 2, h * 2))

    collage.paste(img, (0, 0))           
    collage.paste(blur, (w, 0))          
    collage.paste(contour, (0, h))       
    collage.paste(emboss, (w, h))        

    
    collage.save("output_collage.jpg")
    print("Collage saved as output_collage.jpg ✅")

except FileNotFoundError:
    print("⚠️ Please add an 'input.jpg' image in the folder.")

print("\n=== All Exercises Completed ✅ ===")
