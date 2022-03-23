class student_info:
    def __init__(self, name, major, gpa, is_on_probation):  # Initializing of class; self refers to the actual object; Class definition
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self): # Object Function Definition
        if self.gpa >= 3.5:
            return True
        else:
            return False
