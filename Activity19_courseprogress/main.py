from progress import Student

def main():
    students = [
        Student("Arun", 10),
        Student("Meera", 12),
        Student("John", 8)
    ]

    # Update their progress
    students[0].update_progress(7)
    students[1].update_progress(5)
    students[2].update_progress(8)

    print("Course Progress Tracker\n")
    for s in students:
        print(f"{s.name} → {s.progress_percent():.1f}% complete")

if __name__ == "__main__":
    main()
