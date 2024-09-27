import os
import shutil
from pathlib import Path

# List all files in the current directory
print("Files in current directory:")
for file_name in os.listdir('.'):
    print(file_name)

# Move a file to a backup folder
source_file = Path('example.txt')
backup_folder = Path('backup')

# Create backup folder if it doesn't exist
backup_folder.mkdir(exist_ok=True)

# Move the file
shutil.move(str(source_file), str(backup_folder / source_file.name))

print(f"{source_file} moved to {backup_folder}")