class HashNode:
    """Represents a single key-value pair in the hash table."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class CustomHashTable:
    """Custom hash table implemented using chaining for collision handling."""
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.table = [None] * capacity  # list of buckets

    def _hash(self, key):
        """Compute hash index using Python’s hash() function and modulo arithmetic."""
        return hash(key) % self.capacity

    def insert(self, key, value):
        """Insert or update a key-value pair into the hash table."""
        index = self._hash(key)
        head = self.table[index]

        # If no collision, simply add
        if head is None:
            self.table[index] = HashNode(key, value)
            return

        # Traverse chain to check if key exists or to append new node
        current = head
        while current:
            if current.key == key:
                current.value = value  # update existing key
                return
            if current.next is None:
                break
            current = current.next

        # Append new node at end of chain
        current.next = HashNode(key, value)

    def get(self, key):
        """Retrieve the value associated with the given key."""
        index = self._hash(key)
        current = self.table[index]

        while current:
            if current.key == key:
                return current.value
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def delete(self, key):
        """Delete a key-value pair by key."""
        index = self._hash(key)
        current = self.table[index]
        prev = None

        while current:
            if current.key == key:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                return
            prev = current
            current = current.next

        raise KeyError(f"Key '{key}' not found.")

    def __repr__(self):
        """Readable representation of the hash table contents."""
        result = []
        for i, node in enumerate(self.table):
            chain = []
            current = node
            while current:
                chain.append(f"({current.key}: {current.value})")
                current = current.next
            if chain:
                result.append(f"[{i}] -> " + " -> ".join(chain))
        return "\n".join(result) if result else "HashTable is empty."


# -------------------- Test Section --------------------
if __name__ == "__main__":
    # Example 1 – Basic Insert & Retrieve
    ht = CustomHashTable(5)
    ht.insert("name", "Iniya")
    ht.insert("course", "Python")
    print(ht.get("name"))  # Output: Iniya
    print(ht)

    # Example 2 – Collision Handling
    ht.insert("eman", "ReversedName")  # May collide with "name"
    print("\nAfter handling collision:")
    print(ht)

    # Example 3 – Delete and Recheck
    ht.delete("name")
    print("\nAfter deleting 'name':")
    print(ht.get("eman"))  # Should still be accessible
    print(ht)

    # Reflection
    print("\nReflection:")
    print("A hash table maps keys to indexes using hash functions.")
    print("When two keys collide, chaining (linked nodes) stores them in the same bucket.")
    print("This method ensures efficient insert, get, and delete operations on average O(1) time.")
