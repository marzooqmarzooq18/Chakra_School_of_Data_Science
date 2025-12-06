class Student:
    school_name = "ABC Public School"

s1 = Student()
s2 = Student()

# Adding a new variable directly to one object
s1.name = "Asha"
s1.marks = 90

print(s1.school_name, s1.marks)