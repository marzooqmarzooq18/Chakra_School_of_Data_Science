class CustomRange:
    def __init__(self, start, stop=None, step=1):
        """
        Initializes the CustomRange object similar to Python's range().
        Handles:
        - CustomRange(stop)
        - CustomRange(start, stop)
        - CustomRange(start, stop, step)
        """

        # Handle single-argument form: CustomRange(stop)
        if stop is None:
            self.start = 0
            self.stop = start
        else:
            self.start = start
            self.stop = stop

        # Validate step
        if step == 0:
            raise ValueError("step argument must not be zero")

        self.step = step
        self.current = self.start  # Initialize iteration state

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Generate the next number in the sequence or raise StopIteration."""
        # Ascending sequence
        if self.step > 0 and self.current >= self.stop:
            raise StopIteration
        # Descending sequence
        if self.step < 0 and self.current <= self.stop:
            raise StopIteration

        # Store current value to return
        value = self.current
        # Move to the next value
        self.current += self.step
        return value

    def __repr__(self):
        """Return a readable string representation of the object."""
        return f"CustomRange({self.start}, {self.stop}, {self.step})"


# -------------------- Test Cases --------------------

# Example 1 - Ascending sequence
print("Ascending:")
for n in CustomRange(1, 6):
    print(n, end=" ")
print()  # Expected Output: 1 2 3 4 5

# Example 2 - Descending sequence
print("Descending:")
for n in CustomRange(10, 3, -2):
    print(n, end=" ")
print()  # Expected Output: 10 8 6 4

# Example 3 - Single argument
print("Single argument:")
print(list(CustomRange(4)))  # Expected Output: [0, 1, 2, 3]

# Example 4 - Invalid step
try:
    list(CustomRange(1, 5, 0))
except ValueError as e:
    print(e)  # Expected Output: step argument must not be zero


# -------------------- Reflection --------------------
print("Difference between iterator and iterable in my design:")
print("An iterable is an object that can return an iterator using __iter__().")
print("An iterator is the object that actually produces values one by one using __next__().")
print("In this design, CustomRange is both — it returns itself as the iterator and keeps track of state.")
