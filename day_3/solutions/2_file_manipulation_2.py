# Sample content for logfile.log:
# 2024-09-28 10:00:00 INFO Starting process
# 2024-09-28 10:05:00 WARNING Low memory
# 2024-09-28 10:10:00 ERROR Failed to connect

# Step 1: Read the log file and filter for lines containing "WARNING"
with open("logfile.log", "r") as log_file:
    print("Filtered log entries (WARNING):")
    for line in log_file:
        if "WARNING" in line:
            print(line.strip())
