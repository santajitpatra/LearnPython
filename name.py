import sys

if len(sys.argv) < 2:
    sys.exit("Usage: python3 name.py <name>")
# elif len(sys.argv) > 2:
#     print("TOO MANY ARGUMENTS")
#     sys.exit(1)

for arg in sys.argv[1:]:
    print("Hello, my name is ",arg)

# print("Hello, my name is", sys.argv[1])