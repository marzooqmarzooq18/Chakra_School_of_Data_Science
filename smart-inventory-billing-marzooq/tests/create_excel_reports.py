import pandas as pd
import os

os.makedirs("tests/results", exist_ok=True)

# Test Case Definitions
test_cases = [
    ["TC01", "Add Product", "Check if product is added to CSV correctly", "Pass/Fail"],
    ["TC02", "View Products", "Ensure product list displays all entries", "Pass/Fail"],
    ["TC03", "Create Bill", "Bill file must be generated correctly", "Pass/Fail"]
]

# Save as test_cases.xlsx
df_cases = pd.DataFrame(test_cases, columns=["ID", "Test Name", "Description", "Expected Result"])
df_cases.to_excel("tests/test_cases.xlsx", index=False)

# Empty Results File Template
df_results = pd.DataFrame(columns=["Test Name", "Status"])
df_results.to_excel("tests/results/test_results.xlsx", index=False)

print("Excel test files created successfully!")
