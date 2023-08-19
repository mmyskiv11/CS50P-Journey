def main():
    name = input("What's your name? ").strip().title()
    hello()


def hello():
    print("Hello,", name)


main()
