# function call
def main():
    name1 = input("What is your name? ")
    hello(name1)


def hello(to="World"):
    print("Hello, ", to)

main()



# Ask User for their name and print "Hello, [name]!"
name = input("What is your name? ").strip().title()

# Print "Hello, [name]!"
print("Hello, " + name + "!")
# or 
print(f"Hello, {name}!")