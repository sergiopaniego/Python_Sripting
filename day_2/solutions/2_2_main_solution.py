# main.py
import file_operations

# List all files in the current directory
file_operations.list_files_in_directory('.')

# Backup a specific file
file_operations.backup_file('example.txt', 'backup_folder')
