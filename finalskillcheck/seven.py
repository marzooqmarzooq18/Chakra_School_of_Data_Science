class PrimeIterator:
    def __init__(self, limit: int):
        """
        Initialize the PrimeIterator with a limit.
        Starts checking from 2 (the first prime number).
        """
        if not isinstance(limit, int) or limit <= 1:
            raise ValueError("limit must be greater than 1")

        self.limit = limit
        self.current = 2  # Start checking from 2

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next prime number or raise StopIteration."""
        while self.current <= self.limit:
            if self._is_prime(self.current):
                prime = self.current
                self.current += 1
                return prime
            self.current += 1

        # When limit exceeded, stop iteration
        raise StopIteration

    def _is_prime(self, n: int) -> bool:
        """Check if a number is prime using O(√n) logic."""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        # Check only odd divisors up to √n
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def __repr__(self):
        return f"PrimeIterator(limit={self.limit})"


# -------------------- Test Cases --------------------

# Example 1 - Basic iteration using for loop
print("Primes up to 15:")
for p in PrimeIterator(15):
    print(p, end=" ")
print()  # Expected Output: 2 3 5 7 11 13

# Example 2 - Manual next() calls
print("\nManual iteration:")
prime_gen = PrimeIterator(10)
print(next(prime_gen))   # Expected 2
print(next(prime_gen))   # Expected 3
print(list(prime_gen))   # Expected [5, 7]

# Example 3 - Invalid input
try:
    PrimeIterator(0)
except ValueError as e:
    print("\nError:", e)  # Expected Output: limit must be greater than 1


# -------------------- Reflection --------------------
print("\nHow iteration state and algorithm optimization work together:")
print("The iterator keeps track of its current position (state) using self.current.")
print("Each call to __next__() resumes from where it left off, checking the next numbers for primality.")
print("The _is_prime() method uses √n optimization and skips even numbers for efficiency.")
print("Together, they allow efficient generation of primes without storing large lists.")
