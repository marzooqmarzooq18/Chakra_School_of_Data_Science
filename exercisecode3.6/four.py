timestamps = [
    "2025-09-01 08:15:00","2025-09-01 08:30:00","2025-09-01 08:45:00",
    "2025-09-01 09:05:00","2025-09-01 09:15:00","2025-09-01 09:45:00",
    "2025-09-01 10:00:00"
]

hours = [t[11:13] for t in timestamps]   # take only HH part
peak = max(set(hours), key=hours.count)  # find hour with max logins
print("Peak hour:", peak, "Logins:", hours.count(peak))