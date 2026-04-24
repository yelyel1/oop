name = input("Enter student name: ")
course = input("Enter course: ")
with open("students.txt", "a") as file:
    file.write(name + "," + course + "\n")
print("\nStudent Records")
with open("students.txt", "r") as file:
    for line in file:
        print(line.strip())
        #MGM