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
    # Check for divisibility up to the square root of n (i * i <= n is more efficient than i <= n**0.5)
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

# set comprehension: keep words whose length is a prime number
# The expression: {word for word in words if is_prime(len(word))}
# 1. Iterates over each 'word' in the 'words' list.
# 2. Checks if the length of the word (len(word)) is a prime number using the is_prime function.
# 3. If True, the word is added to the set (which automatically handles duplicates).
prime_length_words = {word for word in words if is_prime(len(word))}

print(prime_length_words)