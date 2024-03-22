name = input("What is your name? ")

match name:
    case "Alice" | "Alicia" | "ALICE" | "alicia":
        print("Hi, Alice.")
    case "Bob":
        print("Hi, Bob.")
    case "Carol":
        print("Hi, Carol.")
    case _:
        print("Hello, stranger.")