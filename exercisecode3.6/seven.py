# List of timestamps
timestamps = [
    "2025-09-01 08:15:00", "2025-09-01 08:15:00", "2025-09-01 09:30:00",
    "2025-09-02 12:00:00", "2025-09-01 09:30:00", "2025-09-03 08:00:00",
    "2025-09-01 12:00:00", "2025-09-04 10:00:00", "2025-09-04 10:00:00",
    "2025-09-05 11:00:00", "2025-09-05 11:00:00", "2025-09-06 09:15:00"
]

# Create an empty list to store duplicates
duplicates = []

# Check each timestamp
for time in timestamps:
    # Count how many times it appears
    if timestamps.count(time) > 1:
        # If not already in duplicates list, add it
        if time not in duplicates:
            duplicates.append(time)

# Print duplicates
print("Duplicate Timestamps:")
for d in duplicates:
    print(d)