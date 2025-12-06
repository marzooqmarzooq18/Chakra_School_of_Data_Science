# multitype_processor.py
import csv

# Step 1: Create a custom exception
class UnsupportedFormatError(Exception):
    """Raised when the file format is not supported."""
    pass

# Step 2: Ask for filename
filename = input("Enter the filename: ")

try:
    # Step 3: Check file extension
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            lines = f.readlines()
            print("\n--- TXT File Report ---")
            print(f"Total lines: {len(lines)}")
            print("First 3 lines:")
            for line in lines[:3]:
                print(line.strip())

    elif filename.endswith(".csv"):
        with open(filename, "r", newline="") as f:
            reader = csv.reader(f)
            rows = list(reader)

            print("\n--- CSV File Report ---")
            if rows:
                print("Header:", rows[0])
                print(f"Number of data rows: {len(rows) - 1}")
            else:
                print("CSV file is empty.")

    else:
        # Step 4: Raise custom error for unsupported files
        raise UnsupportedFormatError("Unsupported file format. Only .txt or .csv allowed.")

# Step 5: Handle errors
except FileNotFoundError:
    print(" Error: File not found. Check the filename or path.")

except PermissionError:
    print("Error: You don’t have permission to read this file.")

except UnsupportedFormatError as e:
    print(" ", e)

except Exception as e:
    print("Unexpected error:", e)
