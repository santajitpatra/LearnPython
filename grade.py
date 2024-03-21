score1 = int(input("Enter your score: "))

if score1 >= 90:
    print("Your grade is an A!")
elif score1 >= 80:
    print("Your grade is a B!")
elif score1 >= 70:
    print("Your grade is a C!")
elif score1 >= 60:
    print("Your grade is a D!")
else:
    print("Your grade is an F!")
    

#Score with if statements normal
score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("Your grade is an A!")
elif score >= 80 and score < 90:
    print("Your grade is a B!")
elif score >= 70 and score < 80:
    print("Your grade is a C!")
elif score >= 60 and score < 70:
    print("Your grade is a D!")
else:
    print("Your grade is an F!")