class Node:
    """Represents a single element in the linked list."""
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    """Manages the overall chain of nodes and provides core operations."""
    def __init__(self):
        self.head = None  # Reference to the first node

    def insert_at_end(self, data):
        """Adds a new node to the end of the list."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        # Traverse to the last node
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_beginning(self, data):
        """Adds a new node to the front of the list (O(1) operation)."""
        new_node = Node(data)
        new_node.next = self.head  # New node's next points to the old head
        self.head = new_node       # Update the head to the new node

    def delete_value(self, value):
        """Removes the first node matching the given value. Handles edge cases."""
        current = self.head

        # Case 1: Empty list
        if current is None:
            return

        # Case 2: Deleting the head node
        if current.data == value:
            self.head = current.next  # Move head to the next node
            return

        # Case 3: Deleting a node in the middle or end
        previous = None
        while current and current.data != value:
            previous = current
            current = current.next

        # If the value was not found
        if current is None:
            return

        # Reroute the pointers: previous node skips the current node
        previous.next = current.next

    def traverse(self):
        """Prints all node data sequentially."""
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next

        # Print the data in the required format
        print(" -> ".join(output) + " -> None")

    def size(self):
        """Returns the total number of nodes."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        """Returns a human-readable representation of the list."""
        output = []
        current = self.head
        while current:
            output.append(str(current.data))
            current = current.next
        return " -> ".join(output)


# --- Example 1 - Insertion and Traversal ---
print("--- Example 1: Insertion and Traversal ---")
ll = LinkedList()
ll.insert_at_end(10)      # List: 10
ll.insert_at_end(20)      # List: 10 -> 20
ll.insert_at_beginning(5) # List: 5 -> 10 -> 20
print("Input:")
print("ll = LinkedList()")
print("ll.insert_at_end(10)")
print("ll.insert_at_end(20)")
print("ll.insert_at_beginning(5)")
print("ll.traverse()")
print("Output:")
ll.traverse()
# Expected Output: 5 -> 10 -> 20 -> None
print("-" * 30)

# --- Example 2 - Deletion ---
print("--- Example 2: Deletion ---")
print("Input:")
print("ll.delete_value(10)")
ll.delete_value(10) # Remove 10 (middle node)
print("ll.traverse()")
print("Output:")
ll.traverse()
# Expected Output: 5 -> 20 -> None
print("-" * 30)

# --- Example 3 - Size Check ---
print("--- Example 3: Size Check ---")
print("Input:")
print('print("Size:", ll.size())')
print("Output:")
print("Size:", ll.size())
# Expected Output: Size: 2
print("-" * 30)