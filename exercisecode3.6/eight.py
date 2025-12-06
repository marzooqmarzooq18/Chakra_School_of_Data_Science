from datetime import datetime, timedelta

dates = ["2025-09-01","2025-09-02","2025-09-04","2025-09-05",
         "2025-09-07","2025-09-08","2025-09-11"]

# Convert to datetime
dates = [datetime.strptime(d, "%Y-%m-%d") for d in dates]

missing = []
for i in range(len(dates)-1):
    day = dates[i] + timedelta(days=1)
    while day < dates[i+1]:
        missing.append(day.strftime("%Y-%m-%d"))
        day += timedelta(days=1)

print("Missing Dates:", missing)