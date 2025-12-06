from datetime import datetime, timedelta

# Event start times
event_starts = ["2025-09-10 10:30:00", "2025-09-15 14:00:00"]

# Participant check-in times
checkins = [
    ("p1", "2025-09-10 09:45:00"),
    ("p2", "2025-09-10 10:05:00"),
    ("p3", "2025-09-15 13:45:00"),
    ("p4", "2025-09-15 14:31:00"),
    ("p5", "2025-09-10 10:20:00")
]

for event in event_starts:
    event_time = datetime.strptime(event, "%Y-%m-%d %H:%M:%S")
    start_window = event_time - timedelta(minutes=30)

    print("\nEvent at:", event)
    count = 0

    for pid, checkin in checkins:
        checkin_time = datetime.strptime(checkin, "%Y-%m-%d %H:%M:%S")

        if start_window <= checkin_time <= event_time:
            print(pid, "checked in on time at", checkin)
            count += 1

    print("Total on-time participants:", count)