# list of words (sample)
words = [
    'data', 'science', 'python', 'analytics', 'machine', 'learning',
    'model', 'visualization', 'algorithm', 'deep', 'neural', 'network',
    'statistics', 'regression', 'classification', 'decision', 'tree',
    'clustering', 'feature', 'engineering', 'analysis'
]

# helper to check primality
def is_prime(n):
    if n < 2:
        return False
    i = 2
    # The condition i * i <= n checks for divisibility up to the square root of n for efficiency.
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# set comprehension: keep words whose length is a prime number
prime_length_words = {word for word in words if is_prime(len(word))}

print(prime_length_words)