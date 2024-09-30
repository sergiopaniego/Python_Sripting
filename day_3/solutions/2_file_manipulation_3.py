from datetime import datetime

def log_message(message, log_file="logfile.log"):
    # Get the current time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write the message to the log file
    with open(log_file, "a") as f:
        f.write(f"{current_time} - {message}\n")

# Example usage of the function
log_message("This is the first log entry.")
log_message("This is the second log entry.")

# Verify the results by reading the log file
print("Log entries:")
with open("logfile.log", "r") as log_file:
    for line in log_file:
        print(line.strip())
