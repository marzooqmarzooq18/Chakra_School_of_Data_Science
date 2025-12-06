def count_passing(subjects):
    result = {}

    for subject in subjects:  # go through each subject
        marks = subjects[subject]  # get the list of marks
        count = 0
        for mark in marks:  # check each mark
            if mark >= 50:  # passing condition
                count = count + 1
        result[subject] = count  # store the passing count

    return result


# Example
subjects = {
    'Math': [67, 45, 81, 90, 50, 49, 77],
    'English': [55, 64, 42, 78, 80, 66, 55],
    'Science': [73, 84, 40, 59, 67, 88, 39],
}

print(count_passing(subjects))