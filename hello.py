def main():
    name1 = input("What is your name? ")
    print(hello(name1))

def hello(to="World"):
    return f"Hello, {to}"


if __name__ == '__main__':
    main()



# # Ask User for their name and print "Hello, [name]!"
# name = input("What is your name? ").strip().title()

# # Print "Hello, [name]!"
# print("Hello, " + name + "!")
# # or 
# print(f"Hello, {name}!")