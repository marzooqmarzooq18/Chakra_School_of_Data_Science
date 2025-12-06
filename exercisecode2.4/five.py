def unique_word_count(feedback):
    words = set()  # store unique words

    for sentence in feedback:
        sentence = sentence.lower()  # make lowercase
        word_list = sentence.split()  # split by spaces
        for word in word_list:
            words.add(word)  # add to set (unique)

    return len(words)


# Example
feedback = [
    "Good service and quality",
    "Quality was excellent and service was prompt",
    "Service could improve in punctuality",
    "Customer service and support are good",
    "Quality, price, and service meet expectations",
    "Excellent quality with prompt delivery",
    "Friendly staff and good product quality",
    "Could improve the quality of packaging",
    "The service was slow but quality was good",
    "Good value for money and excellent service"
]

print(unique_word_count(feedback))