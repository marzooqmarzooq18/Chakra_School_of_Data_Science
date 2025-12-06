# smart_copy.py
import os

# Ask the user for a file to copy
source = input("Enter the source filename to copy: ")

# Create backup folder if not present
backup_folder = "backup"
os.makedirs(backup_folder, exist_ok=True)

# Create full destination path
destination = os.path.join(backup_folder, os.path.basename(source))

try:
    # Open source and destination in binary mode
    with open(source, "rb") as src_file, open(destination, "wb") as dest_file:
        while True:
            # Read 4 KB at a time
            chunk = src_file.read(4096)
            if not chunk:  # End of file
                break
            dest_file.write(chunk)

    # Compare sizes for verification
    src_size = os.path.getsize(source)
    dest_size = os.path.getsize(destination)

    print("\n--- Copy Report ---")
    print(f"Source size: {src_size} bytes")
    print(f"Destination size: {dest_size} bytes")

    if src_size == dest_size:
        print("Verification: Copy successful! Both files have the same size.")
    else:
        print("Verification failed: Sizes do not match.")

# Handle common errors
except FileNotFoundError:
    print("Error: Source file not found. Please check the filename or path.")

except PermissionError:
    print("Error: Permission denied while reading or writing the file.")

except IsADirectoryError:
    print("Error: The given path is a directory, not a file.")

except Exception as e:
    print("Unexpected error:", e)
