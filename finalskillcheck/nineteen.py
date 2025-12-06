import time
import random
from functools import wraps

def retry_with_backoff(retries=3, delay=1, backoff=2, exceptions=(Exception,)):
    """
    Retries a function call upon failure with exponential backoff.

    Args:
        retries (int): Maximum number of retry attempts.
        delay (float): Initial wait time in seconds.
        backoff (float): Multiplier for wait time after each failure.
        exceptions (tuple): Exceptions that trigger a retry.
    """
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            wait = delay
            for attempt in range(1, retries + 1):
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    if attempt == retries:
                        print(f"All {retries} attempts failed.")
                        raise
                    print(f"Attempt {attempt} failed with {type(e).__name__}: {e}. Retrying in {wait}s...")
                    time.sleep(wait)
                    wait *= backoff
        return wrapper
    return decorator


# Example 1 – Random Failure Simulation
@retry_with_backoff(retries=3, delay=1, backoff=2)
def unstable_task():
    """Simulates random failure (70% failure chance)."""
    if random.random() < 0.7:
        raise ValueError("Simulated failure")
    return "Success!"


# Example 2 – Network Retry Simulation
@retry_with_backoff(retries=4, delay=0.5, backoff=1.5, exceptions=(ConnectionError,))
def connect_to_server():
    """Always fails with ConnectionError."""
    raise ConnectionError("Network unavailable")


# Run the examples
print("Running unstable_task()...")
try:
    print(unstable_task())
except Exception as e:
    print(f"Final Error: {e}")

print("\nRunning connect_to_server()...")
try:
    connect_to_server()
except Exception as e:
    print(f"Final Error: {e}")
