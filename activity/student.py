class Student:
    def __init__(self, name, grade_level, classes):
        self.name = name 
        self.grade_level = grade_level
        self.classes = classes
    def add_class(self, new_class):
        self.classes.append(new_class)
        return self.classes
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.grade_level} enrolled in {self.get_num_classes()} classes"

# First instance
student_1 = Student("Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ])
student_1.add_class("Painting") 
student_1.get_num_classes()
student_1.summary() 

# Second instance
student_2 = Student("Claire", "freshman",[ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science" ])
student_2.add_class("Painting")
student_2.get_num_classes() 
student_2.summary()
