# Example file for working with loops
employees = [
    {'name': 'Alice', 'age': 20, 'role': 'teacher'},
    {'name': 'Bob', 'age': 21, 'role': 'teacher'},
    {'name': 'Carol', 'age': 22, 'role': 'teacher'},
    {'name': 'Damien', 'age': 23, 'role': 'student'},
    {'name': 'Elizabeth', 'age': 24, 'role': 'student'},
    {'name': 'Katherine', 'age': 25, 'role': 'teacher'},
    {'name': 'Jennifer', 'age': 26, 'role': 'student'},
    {'name': 'Javi', 'age': 27, 'role': None},

]

for employee in employees:
    print(employee['name'], employee['age'], employee['role'], sep='\t')



# for loop with dict
students_names = {
    'Alice': '2018059',
    'Javi': '2018007',
    'Damien': '2018022',
    'Elizabeth': '2018035',
    'Katherine': '2018040',
    'Jennifer': '2018043',
}

for name in students_names:
    print(name, students_names[name], sep='\t')


# for loop with range and len
students = ['Alice', 'Javi', 'Damien']

for i in range(len(students)):
    print(i + 1,students[i])
# or
for student in students:
    print(student)