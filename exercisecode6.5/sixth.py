# grade_aggregator.py
import csv

filename = "grades.csv"

totals = {}
counts = {}
malformed_rows = 0

try:
    # Try to open the CSV file
    with open(filename, "r") as f:
        reader = csv.DictReader(f)

        for row_num, row in enumerate(reader, start=1):
            try:
                # Ensure required keys are present
                if not all(k in row for k in ("name", "subject", "score")):
                    raise KeyError("Missing one or more required columns")

                name = row["name"].strip()
                score_str = row["score"].strip()

                # Convert score to number
                score = float(score_str)

                # Aggregate per student
                totals[name] = totals.get(name, 0) + score
                counts[name] = counts.get(name, 0) + 1

            except (KeyError, ValueError):
                malformed_rows += 1
                print(f"Skipping malformed row #{row_num}: {row}")
                continue

    # After reading, print summary
    print("\n--- Grade Summary ---")
    for name in totals:
        avg = totals[name] / counts[name]
        print(f"{name:10s} → {avg:.2f}")

    print(f"\nMalformed rows skipped: {malformed_rows}")

except FileNotFoundError:
    print("Error: grades.csv not found. Please check the filename.")

except Exception as e:
    print("Unexpected error:", e)
