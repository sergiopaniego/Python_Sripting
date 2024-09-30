#  Fetch Data from an API using Requests
import requests

def fetch_data():
    response = requests.get('https://api.example.com/data')
    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data:", response.status_code)
        return None

# 2. Process the Data using Pandas

import pandas as pd

def process_data(data):
    df = pd.DataFrame(data)
    # Perform any necessary data transformations
    processed_data = df.describe()  # Example: Get statistical summary
    return processed_data

# 3. Generate a Report

def generate_report(processed_data):
    report_file = 'report.txt'
    with open(report_file, 'w') as f:
        f.write(str(processed_data))
    return report_file


# 4. Upload the Report using Paramiko

import paramiko

def upload_report(report_file, remote_path, hostname, port, username, password):
    try:
        # Create an SSH client
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        # Connect to the remote server
        ssh.connect(hostname, port, username, password)
        
        # Use SFTP to upload the report
        sftp = ssh.open_sftp()
        sftp.put(report_file, remote_path)
        sftp.close()
        
        print(f"Uploaded {report_file} to {remote_path} on {hostname}")
    except Exception as e:
        print(f"Failed to upload report: {e}")
    finally:
        ssh.close()


# 5. Schedule the Workflow using APScheduler

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def automated_task():
    data = fetch_data()
    if data:
        processed_data = process_data(data)
        report_file = generate_report(processed_data)
        
        # Specify the remote server details
        remote_path = '/path/on/remote/server/report.txt'
        hostname = 'your_remote_host'
        port = 22  # Default SSH port
        username = 'your_username'
        password = 'your_password'
        
        upload_report(report_file, remote_path, hostname, port, username, password)

# Schedule the automated task every hour
scheduler.add_job(automated_task, 'interval', hours=1)
scheduler.start()

# Keep the script running
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
