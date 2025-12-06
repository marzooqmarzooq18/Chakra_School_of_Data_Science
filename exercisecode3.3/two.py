import re

email_data = """
Hi team,

Reach Alice at alice@company.com and Bob at bob.smith@company.com.

We also work with info@company.org and xyz@sample.net.

Carol Johnson: carol.johnson@company.com

Group mail: support@company.com

Other emails: xyz.staff@COMPANY.com, test.user@sample.com

For info, write to sales@company.COM and admin@company.com.

Review: ajay@sample.com, manager@company.com

Backup: hr@company.com

Reception: reception@Company.com

Tech: tech@company.org, help@company.com
"""

# Extract all @company.com emails (case-insensitive)
pattern = r"\b[A-Za-z0-9._%+-]+@company\.com\b"
matches = re.findall(pattern, email_data, flags=re.IGNORECASE)

# Convert all to lowercase & remove duplicates
unique_emails = sorted(set([m.lower() for m in matches]))

print(unique_emails)