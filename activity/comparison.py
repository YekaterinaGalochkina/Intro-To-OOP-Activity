
def get_student_with_more_classes(student_2, student_1):
    if student_2.get_num_classes() > student_1.get_num_classes():
        return student_2.name
    return student_1.name
