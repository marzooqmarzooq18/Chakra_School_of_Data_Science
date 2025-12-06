from student import Student

def main():
    students = [
        Student("Arun", [90, 80, 88]),
        Student("Meera", [70, 65, 70]),
        Student("John", [50, 52, 48])
    ]

    print("Student Grade Analyzer\n")

    topper = None
    top_avg = 0

    for s in students:
        avg = s.calc_average()
        g = s.grade()
        print(f"{s.name}: {avg:.1f}% → Grade {g}")
        if avg > top_avg:
            top_avg = avg
            topper = s

    print(f"\nTopper → {topper.name} ({top_avg:.1f}%)")

if __name__ == "__main__":
    main()
