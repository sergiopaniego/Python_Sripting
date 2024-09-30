import requests

# Read the downloaded log file
with open('./system_stats.log', 'r') as file:
    log_data = file.read()

# Example of parsing the log data (you may need to adjust this based on your output format)
cpu_usage = log_data.splitlines()[0]  # Extract CPU usage from the first line
memory_usage = log_data.splitlines()[1]  # Extract memory usage from the second line

# Create the JSON payload
data = {
    'cpu_usage': cpu_usage,
    'memory_usage': memory_usage
}

# Send a POST request to the API
response = requests.post('http://example.com/api/system_stats', json=data)

# Print the status of the request
if response.status_code == 200:
    print("Data sent successfully!")
else:
    print(f"Failed to send data! Status code: {response.status_code}")
