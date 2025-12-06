# Take input
score = int(input("Enter the student's score (0 to 100): "))

# Nested if statements for grading
if score >= 90:
    grade = "A"
elif score >= 75:
    if score <= 79:
        grade = "B-"
    else:
        grade = "B"
elif score >= 50:
    grade = "C"
else:
    if score < 30:
        grade = "F"
    else:
        grade = "D"

# Print the grade
print("Grade:", grade)