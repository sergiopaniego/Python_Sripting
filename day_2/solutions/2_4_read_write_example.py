import json

# Step 1: Create a JSON file with employee data
employee_data = [
    {"name": "Alice", "age": 30, "department": "HR"},
    {"name": "Bob", "age": 25, "department": "Engineering"},
    {"name": "Charlie", "age": 35, "department": "Marketing"}
]

# Write the data to a JSON file
with open("employees.json", "w") as file:
    json.dump(employee_data, file, indent=4)

print("Initial employee data saved to 'employees.json'")

# Step 2: Read the JSON file and print the data
with open("employees.json", "r") as file:
    employees = json.load(file)
    print("\nEmployee data read from 'employees.json':")
    for employee in employees:
        print(employee)

# Step 3: Modify some data (e.g., change Bob's age)
for employee in employees:
    if employee["name"] == "Bob":
        employee["age"] = 26  # Change Bob's age

# Step 4: Save the modified data back to the JSON file
with open("employees.json", "w") as file:
    json.dump(employees, file, indent=4)

print("\nModified employee data saved back to 'employees.json'")
