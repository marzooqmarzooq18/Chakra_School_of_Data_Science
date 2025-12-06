class DNode:
    """A node in a doubly linked list."""
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    """Doubly Linked List supporting insertion, deletion, and traversal."""
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_end(self, data):
        """Insert a node at the end (tail) of the list."""
        new_node = DNode(data)
        if self.tail is None:  # Empty list
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def insert_at_beginning(self, data):
        """Insert a node at the beginning (head) of the list."""
        new_node = DNode(data)
        if self.head is None:  # Empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_value(self, value):
        """Delete the first node that matches the given value."""
        current = self.head

        while current:
            if current.data == value:
                # Case 1: Deleting the head
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                    else:
                        self.tail = None  # List became empty

                # Case 2: Deleting the tail
                elif current == self.tail:
                    self.tail = current.prev
                    if self.tail:
                        self.tail.next = None

                # Case 3: Deleting a middle node
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return  # Exit after deleting first match
            current = current.next

    def traverse_forward(self):
        """Print all nodes from head to tail."""
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def traverse_backward(self):
        """Print all nodes from tail to head."""
        current = self.tail
        while current:
            print(current.data, end=" <-> ")
            current = current.prev
        print("None")

    def size(self):
        """Return the total number of nodes."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def __repr__(self):
        """Readable representation of the list."""
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return " <-> ".join(values) + " <-> None"


# -------------------- Test Section --------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()

    # Example 1 – Insertion and Forward Traversal
    dll.insert_at_end(10)
    dll.insert_at_end(20)
    dll.insert_at_beginning(5)
    print("Forward traversal:")
    dll.traverse_forward()  # 5 <-> 10 <-> 20 <-> None

    # Example 2 – Backward Traversal
    print("Backward traversal:")
    dll.traverse_backward()  # 20 <-> 10 <-> 5 <-> None

    # Example 3 – Deletion
    print("After deleting 10:")
    dll.delete_value(10)
    dll.traverse_forward()  # 5 <-> 20 <-> None

    # Example 4 – Size and Representation
    print("Size of list:", dll.size())
    print("List representation:", dll)

    # Reflection
    print("\nHow maintaining bidirectional links improves traversal flexibility:")
    print("By keeping both 'next' and 'prev' references, we can move forward and backward easily.")
    print("This allows efficient traversal from either end and simplifies node deletion handling.")
