from grade_data import students
from grade_validation import validate_student
from Grade_ranking import ranking_grade
def main():
    grades = 0
    approved_students = []
    for student in students:
        name, grade = student
        valid,msg = validate_student(student,name,grade)
        if valid:
            ranking_grade(name,grade)
            approved_students.append(name)
            grades += grade
        else:
            print(msg)
    print(f'the average grade of the students is : {grades/len(approved_students)}')
main()