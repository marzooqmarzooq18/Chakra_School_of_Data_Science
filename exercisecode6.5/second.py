# safe_appender.py
from datetime import datetime

try:
    # Open the file in append mode ("a") — it adds new lines without deleting old ones
    with open("activity_log.txt", "a") as log_file:
        # Get current timestamp in ISO format
        timestamp = datetime.now().isoformat(timespec='seconds')
        message = "Program executed successfully."

        # Write one line (timestamp + message)
        log_file.write(f"{timestamp} - {message}\n")
        print("Log entry added to activity_log.txt")

except PermissionError:
    print("Error: You don’t have permission to write to this file.")

except Exception as e:
    print("Unexpected error:", e)
