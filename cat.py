def main():
    number = get_number()
    ask(number)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n > 0:
            break
    return n

def ask(n):
    for _ in range(n):
        print("Hello world 22")

main()

# while loop and break
while True:
    n = int(input("Enter a number: "))
    if n > 0:
        break

for _ in range(n):
    print("Hello world")


# for loop
for i in range(5):
    print("hello bro")


# while loop
i = 0
while i < 5:
    print("hello")
    i += 1