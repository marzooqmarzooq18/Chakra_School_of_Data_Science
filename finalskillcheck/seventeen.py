# Mini JSON Parser without using json.loads or eval()

import re


def mini_json_parser(json_str):
    """Converts a JSON-formatted string into its Python object equivalent."""

    json_str = json_str.strip()

    def parse_value(s):
        s = s.strip()

        # String
        if s.startswith('"') and s.endswith('"'):
            return s[1:-1].replace('\\"', '"').replace('\\\\', '\\')

        # Boolean
        if s == "true":
            return True
        if s == "false":
            return False

        # Null
        if s == "null":
            return None

        # Number (float or int)
        if re.match(r"^-?\d+\.\d+$", s):
            return float(s)
        if re.match(r"^-?\d+$", s):
            return int(s)

        # Array
        if s.startswith("[") and s.endswith("]"):
            inner = s[1:-1].strip()
            if not inner:
                return []
            parts = split_json(inner)
            return [mini_json_parser(p) for p in parts]

        # Object
        if s.startswith("{") and s.endswith("}"):
            inner = s[1:-1].strip()
            if not inner:
                return {}
            result = {}
            pairs = split_json(inner)
            for pair in pairs:
                if ":" not in pair:
                    raise ValueError(f"Invalid JSON pair: {pair}")
                k, v = pair.split(":", 1)
                key = mini_json_parser(k)
                val = mini_json_parser(v)
                result[key] = val
            return result

        # Invalid case
        raise ValueError(f"Invalid JSON format: {s}")

    def split_json(s):
        """Splits JSON content by commas, respecting nested levels."""
        depth = 0
        items = []
        start = 0
        for i, c in enumerate(s):
            if c in "[{":
                depth += 1
            elif c in "]}":
                depth -= 1
            elif c == "," and depth == 0:
                items.append(s[start:i].strip())
                start = i + 1
        if start < len(s):
            items.append(s[start:].strip())
        return items

    return parse_value(json_str)


# -------------------------------
# Test Cases
# -------------------------------

# Example 1 – Basic Dictionary
json_text1 = '{"name": "Indu", "age": 30, "active": true}'
print(mini_json_parser(json_text1))
# Output: {'name': 'Indu', 'age': 30, 'active': True}

# Example 2 – Nested Object
json_text2 = '{"course": {"title": "Python", "level": "Advanced"}, "modules": ["OOP", "Recursion"]}'
print(mini_json_parser(json_text2))
# Output: {'course': {'title': 'Python', 'level': 'Advanced'}, 'modules': ['OOP', 'Recursion']}

# Example 3 – Null and Boolean Handling
json_text3 = '[true, false, null]'
print(mini_json_parser(json_text3))
# Output: [True, False, None]

# Example 4 – Number Recognition
json_text4 = '{"x": 3.14, "y": 42}'
print(mini_json_parser(json_text4))
# Output: {'x': 3.14, 'y': 42}
