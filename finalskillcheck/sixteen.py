# Mini JSON Serializer without using json library

def mini_json_serializer(obj):
    """Convert Python objects into JSON-formatted string."""

    if obj is None:
        return "null"

    elif isinstance(obj, bool):
        return "true" if obj else "false"

    elif isinstance(obj, (int, float)):
        return str(obj)

    elif isinstance(obj, str):
        # Escape backslashes and double quotes
        escaped = obj.replace("\\", "\\\\").replace('"', '\\"')
        return f'"{escaped}"'

    elif isinstance(obj, (list, tuple)):
        # Recursively serialize each element
        items = [mini_json_serializer(el) for el in obj]
        return "[" + ", ".join(items) + "]"

    elif isinstance(obj, dict):
        # Serialize each key and value recursively
        pairs = []
        for k, v in obj.items():
            key_str = mini_json_serializer(k)
            val_str = mini_json_serializer(v)
            pairs.append(f"{key_str}: {val_str}")
        return "{" + ", ".join(pairs) + "}"

    else:
        # Unsupported type
        raise TypeError(f"Type {type(obj)} is not JSON serializable")


# -------------------------------
# Test Cases
# -------------------------------

# Example 1 – Simple Dictionary
data1 = {"name": "Indu", "age": 30, "isStudent": False}
print(mini_json_serializer(data1))
# Output: {"name": "Indu", "age": 30, "isStudent": false}

# Example 2 – Nested Data
data2 = {
    "course": "Python",
    "modules": ["OOP", "Data Structures", "Algorithms"],
    "meta": {"level": "Advanced", "active": True}
}
print(mini_json_serializer(data2))
# Output: {"course": "Python", "modules": ["OOP", "Data Structures", "Algorithms"], "meta": {"level": "Advanced", "active": true}}

# Example 3 – Unsupported Type
try:
    print(mini_json_serializer({1, 2, 3}))
except TypeError as e:
    print(e)
# Output: TypeError: Type <class 'set'> is not JSON serializable
