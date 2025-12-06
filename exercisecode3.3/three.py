import re

kyc_text = """
Customer1: PAN: CEGPS1234K
Customer2: pan: abcpd1234z
Invalid entry: XABCD1234Z

Applicant1: XYWOP8899N, Agent: adops1234I

PAN noted: MNOPQ2345L, pan found: LMNAB9876X

Manager: ABCCD4321F, Supervisor: QWERT6789J

Not a PAN: 1234ABCDE

Extra: UVWXY7654V, abcde4321z, valid: GHIJK1234M

Wrong: 2134XY7120, PAN: PQREW1234T

Reference: POITY5678K
"""

# Regex for PAN numbers (case-insensitive)
# The standard PAN format is: 5 letters, 4 digits, 1 letter (e.g., ABCDE1234F)
# r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b"
# \b: Word boundary
# [A-Z]{5}: Exactly 5 uppercase letters (A-Z)
# [0-9]{4}: Exactly 4 digits (0-9)
# [A-Z]{1}: Exactly 1 uppercase letter (A-Z)
# The re.IGNORECASE flag makes it work for both upper and lower case letters.
pattern = r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b"

matches = re.findall(pattern, kyc_text, flags=re.IGNORECASE)

print(matches)