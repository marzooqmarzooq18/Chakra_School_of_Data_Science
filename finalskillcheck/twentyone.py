import time

class ExecutionTimer:
    def __init__(self, label="Block"):
        self.label = label
        self.start_time = None

    def __enter__(self):
        # Record start time when entering the block
        self.start_time = time.time()
        print(f"[TIMER] Started '{self.label}'...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Record end time and calculate duration
        end_time = time.time()
        elapsed_ms = (end_time - self.start_time) * 1000
        print(f"[TIMER] Block '{self.label}' took {elapsed_ms:.2f} ms")
        # Return False to allow exceptions to propagate
        return False


# Example 1 – Simple Computation
with ExecutionTimer("Summation Loop"):
    total = sum(range(1_000_000))


# Example 2 – With Exception Handling
try:
    with ExecutionTimer("Division Test"):
        result = 10 / 0
except ZeroDivisionError:
    print("Handled exception outside the block.")


# Example 3 – Multiple Timed Blocks
with ExecutionTimer("List Comprehension"):
    [x ** 2 for x in range(100_000)]

with ExecutionTimer("Sleep Demo"):
    time.sleep(0.5)
