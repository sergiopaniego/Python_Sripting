import os
import glob
from apscheduler.schedulers.background import BackgroundScheduler

def clean_temp_files():
    temp_files = glob.glob('/path/to/temp/files/*')  # Modify path as needed
    for temp_file in temp_files:
        try:
            os.remove(temp_file)
            print(f"Deleted {temp_file}")
        except Exception as e:
            print(f"Error deleting {temp_file}: {e}")

scheduler = BackgroundScheduler()
scheduler.add_job(clean_temp_files, 'interval', hours=1)
scheduler.start()

# Keep the script running
try:
    while True:
        pass
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
