
def get_student_with_more_classes(claire, samara):
    if claire.get_num_classes() > samara.get_num_classes():
        return claire.name
    return samara.name
