# add your Student class here!
class Student:
    def __init__(self, name, grade_level, classes):
        self.name = name 
        self.grade_level = grade_level
        self.classes = classes
    def add_class(self, new_class):
        self.classes.append(new_class)
    
    def get_num_classes(self):
        return len(self.classes)
    
    def summary(self):
        return f"{self.name} is a {self.grade_level} enrolled in {self.get_num_classes} classes"
    
samara = Student("Samara", "junior", [ "Pre-Calc", "English III", "World History", "Gym", "Chemistry", "Music Composition" ])

print(samara.get_num_classes())