
def validate_format(student,name,grade):
    if type(student) is  not tuple:
        return False,f'{student} student is not a tuple'
    if len(student) != 2:
        return False, f'{student} student data must contain 2 values"'
    if not isinstance(name, str):
        return False, f'{student} student name is not a string'
    if not isinstance(grade, int):
        return False, f'{student} student grade is not a integer'
    return True,""

def validate_grade(grade,student):
    if grade < 0 or grade > 100:
        return False, f'{student} grade is not between 0 and 100'
    else:
        return True,""


def validate_student(student, name, grade):
    valid, msg = validate_format(student, name, grade)
    if not valid:
        return False, msg
    valid, msg = validate_grade(grade,student)
    if not valid:
        return False, msg
    return True, ""