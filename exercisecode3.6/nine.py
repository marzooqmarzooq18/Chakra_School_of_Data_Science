from datetime import datetime

# Sample input (user, start, end)
events = [
    ("user1", "2025-09-01 08:00:00", "2025-09-01 08:30:00"),
    ("user1", "2025-09-01 09:00:00", "2025-09-01 09:40:00"),
    ("user2", "2025-09-03 10:30:00", "2025-09-03 10:50:00"),
    ("user2", "2025-09-04 11:00:00", "2025-09-04 11:30:00"),
    ("user3", "2025-09-05 12:00:00", "2025-09-05 12:45:00")
]

# Dictionary to store total duration and count per user
user_data = {}

for user, start, end in events:
    # Convert strings to datetime
    start_time = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    # Duration in seconds
    duration = (end_time - start_time).total_seconds()

    # Add to dictionary
    if user not in user_data:
        user_data[user] = {"total": 0, "count": 0}
    user_data[user]["total"] += duration
    user_data[user]["count"] += 1

# Compute averages
print("Average Event Duration per User (seconds):")
for user in user_data:
    avg = user_data[user]["total"] / user_data[user]["count"]
    print(user, ":", avg)