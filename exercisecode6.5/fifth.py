# transactional_writer.py
import os

final_file = "report.txt"
temp_file = "report.tmp"

try:
    print("Starting transactional write...")

    # Step 1: Write safely to a temporary file first
    with open(temp_file, "w") as temp:
        temp.write("Report generated successfully.\n")
        temp.write("Summary of operations:\n")
        temp.write("- All processes completed.\n")

        # 🧪 Simulate a failure (for testing only)
        # Uncomment this line to test failure behavior
        # raise Exception("Simulated failure during write!")

        temp.write("- End of report.\n")

    # Step 2: Replace the old file only after successful write
    os.replace(temp_file, final_file)
    print("Transaction complete. report.txt updated safely.")

except Exception as e:
    print("Error occurred during write:", e)

    # Step 3: Cleanup temporary file so no corruption remains
    if os.path.exists(temp_file):
        os.remove(temp_file)
    print("Transaction failed. Original report.txt remains intact.")
