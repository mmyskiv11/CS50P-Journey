'''
Making Faces - converting emoticons to emoji.
- https://cs50.harvard.edu/python/2022/psets/0/faces/
'''


def main():
    message = str(input("Insert your message: "))
    print(convert(message))


def convert(i):
    i = i.replace(":(", "🙁")
    i = i.replace(":)", "🙂")
    return i


main()
