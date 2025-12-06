class QueueUsingStacks:
    """
    A queue implemented using two stacks (FIFO behavior using LIFO stacks).
    """

    def __init__(self):
        self._in_stack = []   # stack for enqueue operations
        self._out_stack = []  # stack for dequeue operations

    def enqueue(self, item):
        """Add an element to the end of the queue."""
        self._in_stack.append(item)

    def dequeue(self):
        """Remove and return the front element of the queue."""
        if self.is_empty():
            raise IndexError("Queue is empty. Cannot dequeue.")

        # If out_stack is empty, transfer all elements from in_stack to out_stack
        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack.pop()

    def peek(self):
        """Return the front element without removing it."""
        if self.is_empty():
            raise IndexError("Queue is empty. Nothing to peek.")

        if not self._out_stack:
            while self._in_stack:
                self._out_stack.append(self._in_stack.pop())

        return self._out_stack[-1]

    def is_empty(self):
        """Check if the queue is empty."""
        return len(self._in_stack) == 0 and len(self._out_stack) == 0

    def size(self):
        """Return the total number of elements in the queue."""
        return len(self._in_stack) + len(self._out_stack)

    def __repr__(self):
        """Readable string for debugging."""
        return f"QueueUsingStacks(in={self._in_stack}, out={self._out_stack})"


# -------------------- Test Section --------------------
if __name__ == "__main__":
    # Example 1 – Basic Flow
    q = QueueUsingStacks()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    print("Dequeue:", q.dequeue())  # 10
    print("Peek:", q.peek())        # 20
    q.enqueue(40)
    print("Dequeue:", q.dequeue())  # 20
    print("Queue State:", q)        # in=[40], out=[30]

    # Example 2 – Edge Case (Empty Queue)
    try:
        empty_q = QueueUsingStacks()
        empty_q.dequeue()
    except IndexError as e:
        print("Error:", e)

    # Example 3 – Multiple Operations
    q2 = QueueUsingStacks()
    for num in [1, 2, 3, 4]:
        q2.enqueue(num)
    print("Size after enqueues:", q2.size())
    print("Dequeued:", q2.dequeue())
    print("Peek after dequeue:", q2.peek())
    print("Queue now:", q2)

    # Reflection
    print("\nHow two LIFO structures form a FIFO design:")
    print("By transferring elements from the input stack to the output stack,")
    print("we reverse their order so the first inserted element is the first to be removed,")
    print("achieving queue-like FIFO behavior using only stack operations.")
