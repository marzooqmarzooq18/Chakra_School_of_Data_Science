sentences = [
    "Data Science is fun",
    "Python makes Data science powerful",
    "Fun with Python"
]

word_count = {}

for sentence in sentences:
    # Convert the sentence to lowercase
    sentence = sentence.lower()
    # Split the sentence into a list of words
    words = sentence.split()

    for word in words:
        # Check if the word is already a key in the dictionary
        if word in word_count:
            # If it exists, increment its count
            word_count[word] = word_count[word] + 1
        else:
            # If it's a new word, add it to the dictionary with a count of 1
            word_count[word] = 1

print(word_count)