import os
import shutil

# Step 1: Create a text file and write data to it
with open("example.txt", "w") as file:
    file.write("This is the original file.\n")

# Step 2: Copy the file to another file
shutil.copy("example.txt", "example_copy.txt")

# Step 3: Delete the original file
os.remove("example.txt")

# Verify the results
print("Files after exercise 1:")
print("example.txt exists:", os.path.exists("example.txt"))
print("example_copy.txt exists:", os.path.exists("example_copy.txt"))
