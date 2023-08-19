# This is a comment
'''
Important Links:
- https://docs.python.org/
- https://docs.python.org/3/library/functions.html
- https://docs.python.org/3/library/functions.html#print
- https://docs.python.org/3/library/stdtypes.html#string-methods

Lecture Notes:
- https://cs50.harvard.edu/python/2022/notes/0/

Lecture Problem set:
- https://cs50.harvard.edu/python/2022/psets/0/
'''
# Ask user for their name and fav book
name = input("What is yout name? ")
book = input("What is your favorite book title? ").strip().title()

# Say hello to user
print("Hello,", name)
print("Hello, " + name)
print("Hello, ", end="")
print(name)
print("Hello,", name, sep=":")
print("Hello, \"Friends\"")  # Escape Sequence
print(f"Hello, {name}")  # This is the F string

# String Method
# Remove user's whitespace
name = name.strip()
print(f"Hello, {name}")

# Capitalize first letter
name = name.capitalize()
print(f"Hello, {name}")

# Capitalizing using title based capitalization
name = name.title()
print(f"Hello, {name}")

# Removing Whitespace and capitalize user's name
name = name.strip().title()
print(f"Hello, {name}")
print(f"My favorite book is \"{book}\"")

first, last = name.split(" ", maxsplit=1)
print(f"Hello, {last}")
