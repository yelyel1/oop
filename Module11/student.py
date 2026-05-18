class Student:
    def __init__(self, student_id, name, course):
        self.student_id = student_id
        self.name = name
        self.course = course

    def display_info(self):
        print(self.student_id, self.name, self.course)
        #mgm