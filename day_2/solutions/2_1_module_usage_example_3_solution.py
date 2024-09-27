import os
import sys
import shutil
from pathlib import Path

# List files in the current directory
print("Files in the current directory:")
for file_name in os.listdir('.'):
    print(file_name)

# Create a file with system information
with open('system_info.txt', 'w') as f:
    f.write(f"System platform: {sys.platform}\n")
    f.write(f"Python version: {sys.version}\n")

# Create backup directory if not exists
backup_dir = Path('backup_files')
backup_dir.mkdir(exist_ok=True)

# Move the file to backup folder
shutil.move('system_info.txt', backup_dir / 'system_info.txt')
print(f"File moved to {backup_dir}")
