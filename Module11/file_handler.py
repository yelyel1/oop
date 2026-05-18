def save_student(student):
    with open("students.txt", "a") as file:
        file.write(
            student.student_id + "," +
            student.name + "," +
            student.course + "\n"
        )


def view_students():
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, course = line.strip().split(",")
                print(student_id, name, course)

    except FileNotFoundError:
        print("No records found.")
        #mgm