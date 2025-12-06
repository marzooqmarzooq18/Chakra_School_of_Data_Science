from datetime import datetime

# Sales data (timestamp, amount)
sales = [
    ("2025-09-06 12:00:00", 100),  # Saturday
    ("2025-09-07 12:30:00", 150),  # Sunday
    ("2025-09-08 13:00:00", 200),  # Monday
    ("2025-10-04 11:00:00", 250),  # Saturday
    ("2025-10-05 15:00:00", 300)   # Sunday
]

weekend_sales = {}

for t, amount in sales:
    dt = datetime.strptime(t, "%Y-%m-%d %H:%M:%S")
    if dt.weekday() in [5, 6]:   # 5=Saturday, 6=Sunday
        month = dt.strftime("%Y-%m")
        weekend_sales[month] = weekend_sales.get(month, 0) + amount

# Show results
for month, total in weekend_sales.items():
    print(month, "Weekend Sales =", total)