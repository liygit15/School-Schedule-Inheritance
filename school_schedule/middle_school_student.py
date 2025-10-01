from .student import Student

class MiddleSchoolStudent(Student):
    def __init__(self,name, grade, classes, gets_transportation=False):

        super().__init__(name,grade,classes)
        self.gets_transportation = gets_transportation

    def display_gets_transportation(self):
        has_transportation = "has" if self.gets_transportation else "has no"
        return f"{self.name} {has_transportation} transportation"

    def summary(self):
        student_summary = super().summary()
        transportation_message = self.display_gets_transportation() 

        return "\n".join((student_summary,transportation_message))
    

    





