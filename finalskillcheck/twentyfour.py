class LRUCache:
    def __init__(self, capacity: int):
        # Maximum number of items cache can hold
        self.capacity = capacity
        self.cache = {}          # Stores key → value
        self.usage_order = []    # Tracks order of keys (oldest → newest)

    def get(self, key):
        # Retrieve value if key exists
        if key in self.cache:
            # Move the key to the end (most recently used)
            self.usage_order.remove(key)
            self.usage_order.append(key)
            return self.cache[key]
        # Key not found
        return -1

    def put(self, key, value):
        # Insert or update a value in the cache
        if key in self.cache:
            # Update existing value and move it to the end
            self.cache[key] = value
            self.usage_order.remove(key)
        elif len(self.cache) >= self.capacity:
            # Cache full → remove least recently used (first in list)
            oldest = self.usage_order.pop(0)
            del self.cache[oldest]
        # Insert new key at the end (most recent)
        self.cache[key] = value
        self.usage_order.append(key)

    def __repr__(self):
        # Display cache content and order
        return f"LRUCache({self.cache}, order={self.usage_order})"


# Test Case 1 – Basic Usage
cache = LRUCache(3)
cache.put("A", 1)
cache.put("B", 2)
cache.put("C", 3)
print(cache)          # A, B, C in order
cache.get("A")        # Access A → becomes most recent
cache.put("D", 4)     # Evict least used (B)
print(cache)

# Test Case 2 – Access and Update
cache2 = LRUCache(2)
cache2.put("X", 100)
cache2.put("Y", 200)
cache2.get("X")       # X becomes most recent
cache2.put("Z", 300)  # Evict least used (Y)
print(cache2)
