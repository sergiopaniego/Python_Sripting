import subprocess

# Step 1: Execute 'ls' and redirect the output to a file
with open("directory_list.txt", "w") as file:
    subprocess.run(["ls", "-l"], stdout=file)

# Step 2: Count the number of lines in the generated file
result = subprocess.run(["wc", "-l", "directory_list.txt"], capture_output=True, text=True)

# Print the result
print(f"The file 'directory_list.txt' has {result.stdout.strip()} lines")
