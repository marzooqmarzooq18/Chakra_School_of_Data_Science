def deep_clone(obj):
    """Recursively creates a deep copy of the given Python object."""

    if isinstance(obj, dict):
        # Clone each key and value recursively
        return {deep_clone(k): deep_clone(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        # Clone each item in the list
        return [deep_clone(x) for x in obj]
    elif isinstance(obj, tuple):
        # Clone each item and return as a new tuple
        return tuple(deep_clone(x) for x in obj)
    elif isinstance(obj, set):
        # Clone each element in the set
        return {deep_clone(x) for x in obj}
    else:
        # For immutables (int, float, str, bool, None) return as is
        return obj


# Test Case 1 – Nested List and Dict
data = {"a": [1, 2, {"b": (3, 4)}]}
clone = deep_clone(data)
data["a"][2]["b"] = (99, 100)

print("Original:", data)
print("Clone   :", clone)

# Test Case 2 – Set and Tuple Mix
s = ({1, 2}, (3, 4, 5))
clone_s = deep_clone(s)

print("\nAre structures equal:", s == clone_s)
print("Are they the same object:", s[0] is clone_s[0])
