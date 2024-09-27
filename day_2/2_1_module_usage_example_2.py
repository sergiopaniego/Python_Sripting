import os
import shutil
from pathlib import Path

# List all files in the current directory
print(os.listdir('.'))

# Create a new directory using pathlib
new_dir = Path('example_dir')
new_dir.mkdir(exist_ok=True)

# Copy a file
shutil.copy('example.txt', 'example_dir/example.txt')
