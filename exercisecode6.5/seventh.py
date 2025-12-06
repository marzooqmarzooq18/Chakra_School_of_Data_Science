# config_report.py
import json
import os

# Step 1 — Set safe default values
DEFAULTS = {
    "input_file": "data.txt",
    "output_file": "summary.txt",
    "max_lines": 100
}

used_defaults = []  # to track which defaults were applied

# Step 2 — Load and validate config.json
try:
    with open("config.json", "r") as f:
        config = json.load(f)
except FileNotFoundError:
    print("Error: config.json not found. Using all defaults.")
    config = DEFAULTS.copy()
    used_defaults = list(DEFAULTS.keys())
except json.JSONDecodeError as e:
    print(f"JSON format error: {e}. Using all defaults.")
    config = DEFAULTS.copy()
    used_defaults = list(DEFAULTS.keys())

# Step 3 — Validate keys and types
def get_config_value(key, expected_type):
    value = config.get(key)
    if not isinstance(value, expected_type):
        print(f"Invalid or missing '{key}', using default: {DEFAULTS[key]}")
        used_defaults.append(key)
        return DEFAULTS[key]
    return value

input_file = get_config_value("input_file", str)
output_file = get_config_value("output_file", str)
max_lines = get_config_value("max_lines", int)

# Step 4 — Process input file
try:
    with open(input_file, "r") as f:
        lines = []
        for i, line in enumerate(f):
            if i >= max_lines:
                break
            lines.append(line.rstrip())

        line_count = len(lines)
        first_line = lines[0] if lines else "(no content)"

    # Step 5 — Write summary to output file
    with open(output_file, "w") as out:
        out.write("=== File Summary ===\n")
        out.write(f"Input file: {input_file}\n")
        out.write(f"Lines read: {line_count}\n")
        out.write(f"First line preview: {first_line}\n")

        if used_defaults:
            out.write("\nDefaults used for: " + ", ".join(set(used_defaults)) + "\n")
        else:
            out.write("\nNo defaults were used.\n")

    print(f"Summary written to {output_file}")

except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
except PermissionError:
    print(f"Error: Permission denied for reading or writing files.")
except Exception as e:
    print(f"Unexpected error: {e}")
