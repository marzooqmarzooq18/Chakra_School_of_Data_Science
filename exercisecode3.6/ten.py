from datetime import datetime, timedelta

# Sample input
start_date = "2025-09-01"
interval_days = 7
occurrences = 6

# Convert string to datetime
date = datetime.strptime(start_date, "%Y-%m-%d")

# Generate recurring dates
dates = []
for i in range(occurrences):
    dates.append(date.strftime("%Y-%m-%d"))
    date += timedelta(days=interval_days)

# Print result
print("Recurring Event Dates:")
for d in dates:
    print(d)