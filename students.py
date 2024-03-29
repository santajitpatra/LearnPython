import csv

name = input("What is your name? ")
location = input("What is your location? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "location"])
    writer.writerow({"name": name, "location":location})










# import csv

# students = []

# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "location": row["location"]})


# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['location']}")








# with open("students.csv") as file:
#     for line in file:
#         row = line.strip().split(",")
#         print(f"{row[0]} is in {row[1]}")