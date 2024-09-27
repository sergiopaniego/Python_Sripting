import csv
import os

def read_employees(file_path):
    employees = []
    if os.path.exists(file_path):
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                employees.append(row)
    return employees

def write_employees(file_path, employees):
    with open(file_path, mode='w', newline='') as file:
        fieldnames = ['name', 'age', 'department']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(employees)

def add_employee(file_path, name, age, department):
    employees = read_employees(file_path)
    employees.append({'name': name, 'age': age, 'department': department})
    write_employees(file_path, employees)

def display_employees(file_path):
    employees = read_employees(file_path)
    for emp in employees:
        print(emp)
