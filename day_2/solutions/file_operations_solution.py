# file_operations.py

from pathlib import Path
import shutil

def list_files_in_directory(directory_path):
    """List all files in a given directory."""
    path = Path(directory_path)
    for file in path.iterdir():
        print(file.name)

def backup_file(file_path, backup_dir):
    """Move a file to a backup directory."""
    file = Path(file_path)
    backup_dir = Path(backup_dir)
    backup_dir.mkdir(exist_ok=True)
    shutil.move(str(file), str(backup_dir / file.name))
