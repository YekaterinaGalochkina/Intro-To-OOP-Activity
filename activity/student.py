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
samara = Student("Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ])
samara.add_class("Painting") 
samara.get_num_classes()
samara.summary() 

# Second instance
claire = Student("Claire", "freshman",[ "Algebra", "Writing", "Contemporary World Issues", "Gym", "Earth Science" ])
claire.add_class("Painting")
claire.get_num_classes() 
claire.summary()
