from datetime import datetime

# Input data: (user, login_time, logout_time)
sessions = [
    ("user1", "2025-09-01 08:00:00", "2025-09-01 08:45:00"),
    ("user2", "2025-09-01 09:30:00", "2025-09-01 10:15:30"),
    ("user1", "2025-09-01 11:00:00", "2025-09-01 11:20:00"),
    ("user3", "2025-09-01 08:15:00", "2025-09-01 09:00:00")
]

for user, login, logout in sessions:
    # Convert string to datetime objects
    login_time = datetime.strptime(login, "%Y-%m-%d %H:%M:%S")
    logout_time = datetime.strptime(logout, "%Y-%m-%d %H:%M:%S")

    # Calculate duration in minutes
    duration = (logout_time - login_time).total_seconds() / 60

    # Print result
    print(user, "was online for", duration, "minutes")