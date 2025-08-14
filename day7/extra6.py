class Student:
    # Class variable shared by all instances
    school_name = "Default High School"

    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, score):
        """
        Add a validated grade between 0 and 100.
        """
        if 0 <= score <= 100:
            self.grades.append(score)
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def average_grade(self):
        """
        Calculate and return the average grade.
        Returns 0 if no grades present.
        """
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def student_info(self):
        """
        Return a string with the student's info.
        """
        avg = self.average_grade()
        return (f"Student: {self.name}, School: {Student.school_name}, "
                f"Average Grade: {avg:.2f}")


# Example usage
student1 = Student("Alice")
student1.add_grade(85)
student1.add_grade(92)
student1.add_grade(78)

student2 = Student("Bob")
student2.add_grade(101)  # Invalid
student2.add_grade(88)

print(student1.student_info())
print(student2.student_info())
