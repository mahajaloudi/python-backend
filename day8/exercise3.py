

class Person:
    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email

    def display_info(self):
        print(f"ID: {self.id}, Name: {self.name}, Email: {self.__email}")

    def get_email(self):
        return self.__email



class Student(Person):
    def __init__(self, id, name, email, major, gpa):
        super().__init__(id, name, email)
        self.major = major
        self.gpa = gpa
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)

    def __lt__(self, other):
        return self.gpa < other.gpa



class Professor(Person):
    def __init__(self, id, name, email, department, courses_teaching):
        super().__init__(id, name, email)
        self.department = department
        self.courses_teaching = courses_teaching

    def __repr__(self):
        return f"Professor(id={self.id}, name='{self.name}', dept='{self.department}')"



print("🔹 Exercise 3: University System")
s1 = Student("S1", "Tom", "tom@uni.edu", "CS", 3.9)
s2 = Student("S2", "Jerry", "jerry@uni.edu", "Math", 3.5)
prof = Professor("P1", "Dr. Smith", "smith@uni.edu", "Physics", ["Quantum", "Astro"])

s1.enroll("OOP")
s2.enroll("Calculus")

s1.display_info()
s2.display_info()

print("GPA comparison:", s1 < s2)  
print("Professor (repr):", repr(prof))
