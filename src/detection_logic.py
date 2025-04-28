import os
import csv
from datetime import datetime

# Initialize a set to keep track of previous object IDs
last_ids = set()

def log_event(event_type, object_id, log_file_path='logs/events.csv'):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Ensure the log directory exists
    os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
    # Append event to CSV
    with open(log_file_path, 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([timestamp, event_type, object_id])

def update_tracking_events(current_ids, log_file_path='logs/events.csv'):
    global last_ids
    current_set = set(current_ids)

    # Identify new and missing IDs
    new_ids = current_set - last_ids
    missing_ids = last_ids - current_set

    # Log events for new IDs
    for id in new_ids:
        log_event('new', id, log_file_path)

    # Log events for missing IDs
    for id in missing_ids:
        log_event('missing', id, log_file_path)

    # Update last_ids for next frame
    last_ids = current_set
