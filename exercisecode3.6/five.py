from datetime import datetime

# Job data (job_id, start_time, end_time)
jobs = [
    (101, "2025-09-01 01:00:00", "2025-09-01 01:20:00"),
    (102, "2025-09-01 02:00:00", "2025-09-01 02:40:00"),
    (103, "2025-09-01 03:00:00", "2025-09-01 03:25:00"),
    (104, "2025-09-02 10:00:00", "2025-09-02 10:45:00"),
    (105, "2025-09-02 11:00:00", "2025-09-02 11:15:00"),
    (106, "2025-09-03 06:30:00", "2025-09-03 07:05:00"),
    (107, "2025-09-03 08:00:00", "2025-09-03 08:25:00"),
    (108, "2025-09-04 14:00:00", "2025-09-04 14:50:00")
]

sla_threshold = 30  # minutes

for job_id, start, end in jobs:
    start_time = datetime.strptime(start, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end, "%Y-%m-%d %H:%M:%S")

    duration = (end_time - start_time).seconds // 60  # in minutes

    if duration > sla_threshold:
        print(f"Job {job_id} exceeded SLA ({duration} mins)")
    else:
        print(f"Job {job_id} OK ({duration} mins)")