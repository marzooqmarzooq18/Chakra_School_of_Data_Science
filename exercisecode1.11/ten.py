words = ["eat", "tea", "tan", "ate", "nat", "bat"]  # The list of words to be grouped

# Outer loop: Iterates through each word to start a new potential group
for i in range(len(words)):

    # Initialize a 'group' with the current word (words[i]). This word will be the 'key' or head of the group.
    group = [words[i]]

    # Inner loop: Iterates through the remaining words (starting from the one after the 'key' word)
    for j in range(i + 1, len(words)):

        # Anagram check: Sort both the 'key' word and the current word (words[j])
        # If the sorted versions are identical, they are anagrams.
        if sorted(words[i]) == sorted(words[j]):
            # If they are anagrams, add the current word (words[j]) to the 'group'
            group.append(words[j])

    # Print the group found for the current 'key' word (words[i])
    # Note: This simple structure will print duplicate groups (e.g., ['eat', 'tea', 'ate'] and then ['tea', 'ate'])
    # because it doesn't remove the words once they are grouped.
    print(group)