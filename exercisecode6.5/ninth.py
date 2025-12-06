# dir_backup_rules_no_shutil.py
import os

SOURCE_DIR = "source"
BACKUP_DIR = "backup"
ALLOWED_EXTENSIONS = (".txt", ".csv", ".json")
MAX_SIZE = 2 * 1024 * 1024  # 2 MB

total_files = 0
copied_files = 0
skipped_files = 0


def is_hidden(filename):
    """Return True if filename starts with a dot."""
    return filename.startswith(".")


def copy_file(src_path, dest_path):
    """Copy file manually without shutil."""
    with open(src_path, "rb") as src, open(dest_path, "wb") as dest:
        while True:
            chunk = src.read(1024 * 1024)  # read 1 MB at a time
            if not chunk:
                break
            dest.write(chunk)


try:
    if not os.path.exists(SOURCE_DIR):
        print(f" Source folder '{SOURCE_DIR}' not found!")
    else:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                total_files += 1
                src_path = os.path.join(root, file)

                # Hidden file check
                if is_hidden(file):
                    print(f" Skipped hidden file: {src_path}")
                    skipped_files += 1
                    continue

                # Extension check
                if not file.lower().endswith(ALLOWED_EXTENSIONS):
                    print(f" Skipped (unsupported type): {src_path}")
                    skipped_files += 1
                    continue

                # Size check
                size = os.path.getsize(src_path)
                if size > MAX_SIZE:
                    print(f"Skipped (too large: {size} bytes): {src_path}")
                    skipped_files += 1
                    continue

                # Build destination path
                rel_path = os.path.relpath(src_path, SOURCE_DIR)
                dest_path = os.path.join(BACKUP_DIR, rel_path)
                os.makedirs(os.path.dirname(dest_path), exist_ok=True)

                # Copy manually
                try:
                    copy_file(src_path, dest_path)
                    copied_files += 1
                    print(f"Copied: {src_path} → {dest_path}")
                except Exception as e:
                    print(f"Failed to copy {src_path}: {e}")
                    skipped_files += 1

        # --- Summary ---
        print("\n--- Backup Summary ---")
        print(f"Total files found: {total_files}")
        print(f"Copied: {copied_files}")
        print(f"Skipped: {skipped_files}")

except PermissionError:
    print("Permission denied while accessing a file or folder.")
except Exception as e:
    print("Unexpected error:", e)
