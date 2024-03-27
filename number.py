def main():
    x= get_int("Please enter a number: ")
    print("Thank you for entering a number. The number is", x)

def get_int(value):
    while True:
        try:
            x = int(input(value))
        except ValueError:
            # print("Oops!  That was no valid number.  Try again...")
            pass
        else:
            break
    return x

main()