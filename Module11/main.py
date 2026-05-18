from student import Student
from file_handler import save_student, view_students

def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    student = Student(student_id, name, course)
    save_student(student)
    print("Student added successfully")


def search_student():
    search_id = input("Enter Student ID to search: ")
    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, course = line.strip().split(",")
                if student_id == search_id:
                    print("Student Found:")
                    print(student_id, name, course)
                    return
        print("Student not found")
    except FileNotFoundError:
        print("No records available")


def main():
    while True:
        print("\nSTUDENT INFORMATION SYSTEM")
        print("1 Add Student")
        print("2 View Students")
        print("3 Search Student")
        print("4 Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
    #mgm