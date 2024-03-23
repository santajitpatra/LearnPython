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