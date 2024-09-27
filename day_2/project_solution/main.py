import employee_manager as em
import os
import subprocess

file_path = "employees.csv"

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    with open(file_path, mode='w') as file:
        pass

while True:
    print("\nOptions: 1. Add Employee 2. Display Employees 3. Exit")
    choice = input("Choose an option: ")

    try:
        if choice == '1':
            name = input("Enter name: ")
            age = input("Enter age: ")
            department = input("Enter department: ")
            em.add_employee(file_path, name, age, department)
            print("Employee added.")
        elif choice == '2':
            print("Employees:")
            em.display_employees(file_path)
            # Execute a command to list the contents of the CSV file
            subprocess.run(["cat", file_path])  # or "type" for Windows
        elif choice == '3':
            confirm = input("Are you sure you want to delete the file? (y/n): ")
            if confirm.lower() == 'y':
                os.remove(file_path)
                print("File deleted.")
                break
        else:
            print("Invalid option.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Exiting the operation.")

print("Goodbye!")
