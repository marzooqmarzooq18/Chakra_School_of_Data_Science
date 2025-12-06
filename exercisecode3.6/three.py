from datetime import datetime

downtimes = [
    ("2025-09-01 02:00:00", "2025-09-01 02:30:00"),
    ("2025-09-03 15:00:00", "2025-09-03 15:20:00"),
    ("2025-09-05 23:50:00", "2025-09-06 00:10:00")
]

total = 0
for s, e in downtimes:
    total += (datetime.strptime(e, "%Y-%m-%d %H:%M:%S") -
              datetime.strptime(s, "%Y-%m-%d %H:%M:%S")).total_seconds() / 60

print("Total downtime:", total, "minutes")