class CustomStack:
    """
    A simple implementation of a Stack (LIFO) data structure.
    Provides standard stack operations with encapsulated internal storage.
    """

    def __init__(self):
        self.__items = []  # private list to store stack elements

    def push(self, item):
        """Add an element to the top of the stack."""
        self.__items += [item]  # using concatenation instead of append()

    def pop(self):
        """Remove and return the top element. Raise error if empty."""
        if self.is_empty():
            raise IndexError("Stack is empty. Cannot pop.")
        top_item = self.__items[-1]
        self.__items = self.__items[:-1]  # remove last element
        return top_item

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            raise IndexError("Stack is empty. Nothing to peek.")
        return self.__items[-1]

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.__items) == 0

    def size(self):
        """Return the total number of elements in the stack."""
        return len(self.__items)

    def __repr__(self):
        """Return a readable string showing stack contents."""
        return f"CustomStack({self.__items})"


# -------------------- Test Section --------------------
if __name__ == "__main__":
    # Example 1 – Basic Operations
    s = CustomStack()
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushes:", s)
    print("Top element:", s.peek())
    s.pop()
    print("After pop:", s)
    print("Size:", s.size())

    # Example 2 – Multiple Data Types
    s2 = CustomStack()
    s2.push("apple")
    s2.push("banana")
    s2.push(42)
    print("Mixed type stack:", s2)

    # Example 3 – Edge Case: Empty pop
    try:
        empty_stack = CustomStack()
        empty_stack.pop()
    except IndexError as e:
        print("Error:", e)

    # Reflection
    print("\nHow encapsulation improves reliability:")
    print("Encapsulation hides the internal storage (__items), preventing accidental modification.")
    print("Users must interact only through methods like push() and pop(), ensuring safe and controlled access.")
