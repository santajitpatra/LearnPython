x = int(input("What is x? "))
y = int(input("What is y? "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{y} is greater than {x}")
# elif x == y:
else:
    print(f"{x} is equal to {y}")