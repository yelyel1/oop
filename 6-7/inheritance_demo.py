class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        print(self.name, "makes a sound")
class Dog(Animal):
    def bark(self):
        print(self.name, "barks")

dog1 = Dog("Buddy")
dog1.speak()
dog1.bark()
#MGM