def ranking_grade(name,grade):
        if grade >= 90:
            print(f'{name} got {grade} Excellent')
        elif 89>grade >=60:
            print(f'{name} got {grade} passed')
        else:
            print(f'{name} got {grade} failed')