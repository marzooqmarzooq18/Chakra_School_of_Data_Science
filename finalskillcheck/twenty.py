class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        # Open the file when entering the 'with' block
        self.file = open(self.filename, self.mode)
        print(f"[OPEN] {self.filename} opened in {self.mode} mode.")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # Always close the file safely
        if self.file:
            self.file.close()
            if exc_type:
                print(f"[CLOSE] {self.filename} closed safely after exception: {exc_val}")
            else:
                print(f"[CLOSE] {self.filename} closed successfully.")
        # Returning False lets the exception propagate
        return False


# Example 1 – Normal File Write
with FileManager("sample.txt", "w") as f:
    f.write("Hello Chakra School of Data Science!")
print("File written successfully.")


# Example 2 – Exception Handling
try:
    with FileManager("data.txt", "w") as f:
        f.write("Testing error handling...")
        raise ValueError("Intentional error inside context")
except ValueError:
    print("Exception handled outside the context.")
