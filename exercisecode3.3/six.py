from collections import Counter

emails = [
    'alice@gmail.com', 'bob@yahoo.com', 'carol@gmail.com', 'david@outlook.com', 'eve@gmail.com',
    'frank@yahoo.com', 'grace@company.com', 'ajay@company.com', 'sam@company.com',
    'helen@gmail.com', 'ian@yahoo.com', 'jack@company.com', 'kate@company.com',
    'laura@outlook.com', 'mike@gmail.com', 'nancy@yahoo.com', 'olive@company.com'
]

# Step 1: Extract domains from each email
# The expression splits the email at the '@' symbol and takes the second element (index 1), which is the domain.
domains = [email.split('@')[1] for email in emails]

# Step 2: Count frequency of each domain
domain_counts = Counter(domains)

# Step 3: Get top 5 most common domains
top_5 = domain_counts.most_common(5)

print(top_5)