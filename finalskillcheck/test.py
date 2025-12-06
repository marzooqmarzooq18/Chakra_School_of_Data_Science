

class PrimeIterator:
    """
    An iterator that yields prime numbers from 2 up to and including a given limit.

    This iterator uses incremental generation and tests divisibility only by known primes
    up to the square root of the candidate for efficiency.
    """

    def __init__(self, limit):
        """
        Initialize the PrimeIterator with a given limit.

        Args:
            limit (int): The upper limit for prime number generation. Must be an integer >= 2.

        Raises:
            TypeError: If limit is not an integer.
            ValueError: If limit is less than 2.
        """
        if not isinstance(limit, int):
            raise TypeError("Limit must be an integer.")

        if limit < 2:
            raise ValueError("Limit must be >= 2.")

        self.limit = limit
        self.primes = []
        self._next_candidate = 2

    def __iter__(self):
        """
        Return the iterator object itself.
        """
        return self

    def __next__(self):
        """
        Generate the next prime number up to the limit or raise StopIteration.

        Returns:
            int: The next prime number.

        Raises:
            StopIteration: If there are no more prime numbers within the limit.
        """
        while self._next_candidate <= self.limit:
            n = self._next_candidate
            # Update next candidate: 2 -> 3, then skip evens
            if self._next_candidate == 2:
                self._next_candidate = 3
            else:
                self._next_candidate += 2

            if self._is_prime(n):
                self.primes.append(n)
                return n

        raise StopIteration

    def _is_prime(self, n):
        """
        Check if a number is prime using known primes up to the square root of the number.

        Args:
            n (int): The number to check for primality.

        Returns:
            bool: True if the number is prime, False otherwise.
        """
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False

        sqrt_n = int(n**0.5)
        for p in self.primes:
            if p > sqrt_n:
                break
            if n % p == 0:
                return False
        return True

# Example usage
if __name__ == "__main__":
    try:
        for prime in PrimeIterator(30):
            print(prime)
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")