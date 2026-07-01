students = [("Dana", 82),("Tom", 55),("Maya", 91),("Ron", 60),("Noa", "88"),("Ben", 120),("Lior", -5), (55, 70),["bob",5 ] ]
approved_students=[]
grades=0
for i in range(len(students)):
    if type(students[i])==tuple:
        if len(students[i])==2:
            if type(students[i][0]) ==str:
                if type(students[i][1]) ==int:
                    if 100 >= students[i][1] >= 0:
                        approved_students.append(students[i])
                        grades+=students[i][1]
                        if students[i][1] > 90:
                            print(f'{students[i][0]} got {students[i][1]} Excellent')
                        elif  89> students[i][1] > 60:
                            print(f'{students[i][0]} got {students[i][1]} Passed')
                        else:
                            print(f'{students[i][0]} got {students[i][1]} Failed')
                    else:
                        print(f'{students[i]} grades are out of range')
                else:
                    print(f'{students[i]} grades are not an integer')
            else:
                print(f'{students[i]} name not an str ')
        else:
            print(f'{students[i]} more then two parameters ')
    else:
        print(f'{students[i]} is not a tuple')
print('class average grades is : ',grades / len(approved_students))
