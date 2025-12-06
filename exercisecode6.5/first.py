# fault_safe_reader.py

# Ask user for the filename
filename = input("Enter the filename to read: ")

try:
    # Try opening the file in read mode
    with open(filename, "r") as file:
        # Read and print the contents
        content = file.read()
        print("\n--- File Contents ---")
        print(content)

# Handle specific errors
except FileNotFoundError:
    print(" Error: The file was not found. Please check the name or path.")

except PermissionError:
    print("Error: You don’t have permission to open this file.")

# Handle any other unexpected errors
except Exception as e:
    print(" An unexpected error occurred:", e)
