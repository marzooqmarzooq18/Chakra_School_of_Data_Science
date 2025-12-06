import re

reviews = [
    "Excellent product, super fast delivery!",
    "Service was excellent and the delivery was fast.",
    "Excellent support and excellent fast delivery.",
    "The product is excellent, fast delivery, and well packaged.",
    "Excellent! Fast delivery, happy with the support.",
    "Excellent product and fast delivery.",
    "Excellent service, fast delivery ensured.",
    "Excellent, super fast delivery!"
]

# Regex: check if both "excellent" and "fast delivery" appear in text
# r"(?i)(?=.*excellent)(?=.*fast delivery)"
# (?i): Makes the entire pattern case-insensitive.
# (?=.*excellent): A positive lookahead that asserts 'excellent' (with anything before it) is present in the string.
# (?=.*fast delivery): Another positive lookahead that asserts 'fast delivery' (with anything before it) is present in the string.
# Since the lookaheads don't consume characters, they check for the presence of the two phrases anywhere in the string, regardless of their order.
pattern = r"(?i)(?=.*excellent)(?=.*fast delivery)"

# Filter the reviews: re.search checks if the pattern is found anywhere in the string.
positive_reviews = [r for r in reviews if re.search(pattern, r)]

print(positive_reviews)