class CNode:
    """A node in a circular linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    """Circular Linked List with insertion, deletion, traversal, and loop detection."""
    def __init__(self):
        self.head = None

    def insert(self, data):
        """Insert a new node at the end while maintaining circular links."""
        new_node = CNode(data)
        if self.head is None:
            # First node points to itself
            self.head = new_node
            new_node.next = self.head
        else:
            # Traverse to last node
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def delete(self, key):
        """Delete a node by value while maintaining circular structure."""
        if self.head is None:
            return  # Empty list

        current = self.head
        prev = None

        # Case 1: Deleting the head node
        if current.data == key:
            # If only one node
            if current.next == self.head:
                self.head = None
                return

            # Move to last node to reconnect the tail
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return

        # Case 2: Deleting non-head node
        current = self.head
        while current.next != self.head:
            prev = current
            current = current.next
            if current.data == key:
                prev.next = current.next
                return

    def traverse(self, limit=None):
        """Display nodes safely (limit traversal to avoid infinite loop)."""
        if self.head is None:
            print("List is empty.")
            return

        current = self.head
        count = 0
        while True:
            print(current.data, end=" -> ")
            current = current.next
            count += 1
            if limit and count >= limit:
                print("...")
                break
            if current == self.head:
                print("(back to head)")
                break

    def has_loop(self):
        """Detect if a loop exists using Floyd’s Cycle Detection (Tortoise and Hare)."""
        slow = self.head
        fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def __repr__(self):
        """Readable string representation for debugging."""
        if not self.head:
            return "CircularLinkedList([])"

        result = []
        current = self.head
        while True:
            result.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(result) + " -> (back to head)"


# -------------------- Test Section --------------------
if __name__ == "__main__":
    cll = CircularLinkedList()

    # Example 1 – Circular Insertion and Traversal
    cll.insert(10)
    cll.insert(20)
    cll.insert(30)
    print("Traversal (limit=6):")
    cll.traverse(limit=6)

    # Example 2 – Loop Detection
    print("\nHas loop:", cll.has_loop())

    # Example 3 – Deletion
    print("\nAfter deleting 20:")
    cll.delete(20)
    cll.traverse(limit=4)

    # Reflection
    print("\nReflection:")
    print("Floyd’s algorithm is elegant because it uses two pointers moving at different speeds.")
    print("If they meet, a loop exists. It is efficient since it uses O(1) extra space and runs in O(n) time.")
