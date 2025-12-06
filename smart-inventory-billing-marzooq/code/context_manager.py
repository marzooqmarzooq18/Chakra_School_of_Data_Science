# context_manager.py
import os
from code.logger import log_error


class SafeFile:
    """Context manager for safe file handling with error logging."""

    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        try:
            # Ensure the folder exists before opening
            os.makedirs(os.path.dirname(self.filepath), exist_ok=True)
            self.file = open(self.filepath, self.mode, newline='', encoding='utf-8')
            return self.file
        except Exception as e:
            log_error(f"Error opening file {self.filepath}: {e}")
            raise

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if self.file:
                self.file.close()
        except Exception as e:
            log_error(f"Error closing file {self.filepath}: {e}")
