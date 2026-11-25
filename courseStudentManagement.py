courses = [
    {
        "id": "ECE101",
        "name": "Intro to Electrical Engineering",
        "credits": 4,
        "instructor": "Prof. A",
        "capacity": 30,
        "enrolled": 30,
        "meeting": "Mon/Wed 9:00-10:15",
        "prerequisites": [],
    },
    {
        "id": "ECE102",
        "name": "Fundamentals of Programming",
        "credits": 4,
        "instructor": "Prof. B",
        "capacity": 24,
        "enrolled": 18,
        "meeting": "Tue/Thu 11:00-12:50",
        "prerequisites": ["ECE101"],
    },
    {
        "id": "ECE201",
        "name": "Circuits",
        "credits": 4,
        "instructor": "Prof. C",
        "capacity": 20,
        "enrolled": 14,
        "meeting": "Mon/Wed 1:00-2:50",
        "prerequisites": ["ECE101"],
    },
    {
        "id": "ECE220",
        "name": "Embedded Design",
        "credits": 3,
        "instructor": "Prof. D",
        "capacity": 18,
        "enrolled": 18,
        "meeting": "Fri 9:00-11:50",
        "prerequisites": ["ECE102", "ECE201"],
    },
]

def calculate_remaining_seats(course):
    return course["capacity"] - course["enrolled"]


def get_prerequisite_names(course, courses_by_id):
    names = []
    for prerequisite_id in course["prerequisites"]:
        names.append(courses_by_id[prerequisite_id]["name"])
    return ", ".join(names) if names else "None"


def display_available_courses(courses):
    if not courses:
        print("No courses are currently available.")
        return

    courses_by_id = {course["id"]: course for course in courses}
    headers = [
        "Course ID",
        "Course name",
        "Credits",
        "Instructor",
        "Capacity",
        "Enrolled",
        "Seats left",
        "Meeting day/time",
        "Prerequisites",
        "Status",
    ]
    rows = []

    for course in courses:
        remaining_seats = calculate_remaining_seats(course)
        status = "FULL" if remaining_seats == 0 else "Open"
        rows.append(
            [
                course["id"],
                course["name"],
                str(course["credits"]),
                course["instructor"],
                str(course["capacity"]),
                str(course["enrolled"]),
                str(remaining_seats),
                course["meeting"],
                get_prerequisite_names(course, courses_by_id),
                status,
            ]
        )

    widths = [
        max(len(headers[index]), *(len(row[index]) for row in rows))
        for index in range(len(headers))
    ]
    border = "+" + "+".join("-" * (width + 2) for width in widths) + "+"

    def print_row(values):
        print(
            "| "
            + " | ".join(
                value.ljust(widths[index]) for index, value in enumerate(values)
            )
            + " |"
        )

    print(border)
    print_row(headers)
    print(border)
    for row in rows:
        print_row(row)
    print(border)


def main():
    while True:
        print("\nCourse Management")
        print("1. Display available courses")
        print("Q. Quit")
        choice = input("Choose an option: ").strip().lower()

        if choice == "1":
            display_available_courses(courses)
        elif choice == "q":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Enter 1 to display courses or Q to quit.")


if __name__ == "__main__":
    main()
