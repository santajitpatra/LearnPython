names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names, reverse=True):
    print(f"Hello, {name}")





# name = input("What is your name? ").strip().title()


# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")
# # file.close()






# names = []

# for _ in range(5):
#     name = input("What is your name? ").strip().title()
#     names.append(name)

# for name in sorted(names):
#     print(f"Hello, {name}!")