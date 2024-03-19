def main():
    x2 = int(input("What is the x value? "))
    print("x squared is", square(x2))

def square(n):
    return n ** 2

main()

# decimal numbers with commas
x1 = float(input("What is the x value? "))
y1 = float(input("What is the y value? "))

z1= round(x1 + y1, 2)

print(f"The sum of {x1} and {y1} is {z1:,}")

# calculating the sum of two numbers
x = int(input("What is x? "))
y = int(input("What is y? "))

# z = int(x) + int(y)
# print(f"The sum of {x} and {y} is {z}")

print(f"The sum of {x} and {y} is {x + y}")
