import paramiko

# Connect to the remote server
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Replace with your server's IP, username, and password
client.connect('your_server_ip', username='your_username', password='your_password')

# Run CPU and memory monitoring commands
stdin, stdout, stderr = client.exec_command('top -bn1 | grep "Cpu(s)" && free -m')

# Print the command output
output = stdout.read().decode()
print(output)

# Save the output to a log file on the remote server
client.exec_command('echo "{}" > /tmp/system_stats.log'.format(output))

client.close()

# Connect and create an SFTP session
sftp = client.open_sftp()

# Download the log file to the local system
sftp.get('/tmp/system_stats.log', './system_stats.log')

sftp.close()
client.close()
