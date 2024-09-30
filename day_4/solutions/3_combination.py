import paramiko
import requests

# Establish an SSH connection to the remote server
def connect_to_remote_server(hostname, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname, username=username, password=password)
    return client

# Get system stats from the remote server using psutil
def get_remote_system_stats(client):
    stdin, stdout, stderr = client.exec_command('python3 -c "import psutil; print(psutil.cpu_percent(), psutil.virtual_memory().percent, psutil.disk_usage(\'/\').percent)"')
    output = stdout.read().decode().strip()
    cpu, memory, disk = map(float, output.split())
    return cpu, memory, disk

# Send the system stats to a web server using an HTTP POST request
def send_data_to_server(system_stats):
    url = 'http://example.com/api/system_stats'  # Replace with the actual URL
    data = {
        'cpu_usage': system_stats[0],
        'memory_usage': system_stats[1],
        'disk_usage': system_stats[2]
    }
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print("Data successfully sent to server")
    else:
        print(f"Failed to send data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Replace with your server's hostname and credentials
    hostname = 'your_remote_server_ip'
    username = 'your_username'
    password = 'your_password'

    # Connect to the remote server via SSH
    client = connect_to_remote_server(hostname, username, password)

    # Get system stats from the remote server
    system_stats = get_remote_system_stats(client)
    print("System Stats from Remote Server:", system_stats)

    # Send the system stats to the web server
    send_data_to_server(system_stats)

    # Close the SSH connection
    client.close()
