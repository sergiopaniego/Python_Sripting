import re

# Read the file
with open('re_example_data.txt', 'r') as file:
    log_data = file.read()

# 1. Find and print all lines containing the word ERROR
error_lines = re.findall(r'.*ERROR.*', log_data)
print("Lines containing 'ERROR':")
for line in error_lines:
    print(line)

# 2. Count the number of WARNING messages in the text
warning_count = len(re.findall(r'WARNING', log_data))
print(f"\nNumber of 'WARNING' messages: {warning_count}")

# 3. Replace all occurrences of INFO with LOG and print the modified text
modified_text = re.sub(r'INFO', 'LOG', log_data)
print("\nModified text (INFO replaced by LOG):")
print(modified_text)

# 4. Extract all the log levels (INFO, WARNING, ERROR) from the text and print them as a list
log_levels = re.findall(r'(INFO|WARNING|ERROR)', log_data)
print("\nExtracted log levels:")
print(log_levels)

# Create a dictionary to hold lists for each log level
log_dict = {
    'ERROR': [],
    'WARNING': [],
    'INFO': []
}

# Use regex to find each line and classify them by log level
log_lines = re.findall(r'(INFO|WARNING|ERROR): (.*)', log_data)

for log_level, message in log_lines:
    log_dict[log_level].append(message)

# Print the grouped log messages by log level
for level, messages in log_dict.items():
    print(f"{level}: {messages}")

