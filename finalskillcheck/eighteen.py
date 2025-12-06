import time
from functools import wraps

def log_function_call(func):
    """
    Decorator that logs execution details of a function:
    - Function name
    - Arguments and keyword arguments
    - Execution time in milliseconds
    - Return value
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        duration = (end_time - start_time) * 1000  # convert to milliseconds
        print(f"[LOG] Function: {func.__name__} | Args: {args} | Kwargs: {kwargs} | Time: {duration:.4f} ms | Return: {result}")
        return result
    return wrapper


# -------------------------------
# Test Functions
# -------------------------------

@log_function_call
def add(a, b):
    """Adds two numbers"""
    return a + b


@log_function_call
def compute_sum(n):
    """Computes the sum of numbers from 0 to n-1"""
    total = 0
    for i in range(n):
        total += i
    return total


@log_function_call
def profile(name, age):
    """Returns a dictionary with profile info"""
    return {"name": name, "age": age}


# -------------------------------
# Function Calls (Testing)
# -------------------------------

add(5, 10)
compute_sum(100000)
profile("Iniya", 30)
