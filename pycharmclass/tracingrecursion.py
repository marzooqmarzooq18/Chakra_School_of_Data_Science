# main.py
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

# a small lambda used inside a function
def compute_and_print(n):
    f = lambda x: x + 10
    result = factorial(n)
    print("lambda result:", f(result))
    return result

compute_and_print(4)
