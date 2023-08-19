# This is a comment
'''
Important Links:
- https://docs.python.org/
- https://docs.python.org/3/library/functions.html#print
- https://docs.python.org/3/library/stdtypes.html#string-methods

Lecture Notes:
- https://cs50.harvard.edu/python/2022/notes/0/

Lecture Problem set:
- https://cs50.harvard.edu/python/2022/psets/0/
'''
# Ask user for their name
name = input("What is yout name? ")

# Say hello to user
print("Hello,", name)
print("Hello, " + name)
print("Hello, ", end="")
print(name)
print("Hello,", name, sep=":")
print("Hello, \"Friends\"")  # Escape Sequence
print(f"Hello, {name}")  # This is the F string
