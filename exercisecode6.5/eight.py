# stream_stats.py
import time

# ---------- PART 1: Generate a large log file ----------
NUM_LINES = 10000
log_file = "large_log.txt"

try:
    with open(log_file, "w") as f:
        for i in range(1, NUM_LINES + 1):
            if i % 100 == 0:
                f.write(f"{i}: ERROR - Disk full\n")
            else:
                f.write(f"{i}: INFO - System running normally\n")
    print(f"Generated {NUM_LINES} lines in {log_file}")

except Exception as e:
    print("Error while generating file:", e)


# ---------- PART 2: Stream and Analyze the file ----------
try:
    start_time = time.time()

    total_lines = 0
    error_lines = 0
    longest_line_length = 0

    # Read the file line by line (streaming mode)
    with open(log_file, "r") as f:
        for line in f:
            total_lines += 1
            if "ERROR" in line:
                error_lines += 1
            if len(line) > longest_line_length:
                longest_line_length = len(line)

    end_time = time.time()
    duration = end_time - start_time

    # Print summary report
    print("\n--- Log File Analysis ---")
    print(f"Total lines: {total_lines}")
    print(f"Error lines: {error_lines}")
    print(f"Longest line length: {longest_line_length}")
    print(f"Time taken: {duration:.4f} seconds")

except FileNotFoundError:
    print("Error: The log file was not found.")

except UnicodeDecodeError:
    print("Error: Could not decode the file. Check the file encoding.")

except Exception as e:
    print("Unexpected error:", e)
