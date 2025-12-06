def prime_generator(n):
    # go from 2 up to n
    for num in range(2, n + 1):
        is_prime = True

        # check if num has any divisor
        # Optimization: only check divisibility up to the square root of num.
        # The range goes from 2 up to int(num ** 0.5) (inclusive).
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            yield num  # yield prime number one by one

# Example usage
n = 30
print(f"Prime numbers up to {n}:")
for prime in prime_generator(n):
    print(prime, end=" ")
print() # for a final newline