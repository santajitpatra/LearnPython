import re


name = input("What is your name? ").strip()
if matchs:= re.search(r"^(.+), ?(.+)$", name):
# if matchs:= re.search(r"^(.+), *(.+)$", name):
    name = matchs.group(2) + " " + matchs.group(1)
print(f"Hello, {name}")
