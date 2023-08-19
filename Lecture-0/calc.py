'''
Related link:
- https://docs.python.org/3/library/functions.html#round
'''
x = int(input("Enter the value of X: "))
y = int(input("Enter the value of Y: "))

print(x + y)

a = float(input("Enter the value of A: "))
b = float(input("Enter the value of B: "))

c = round(a + b)

print(c)
print(f"{c:,}")

# Division
foo = float(input("Enter the value of foo: "))
bar = float(input("Enter the value of bar: "))

res = foo / bar

print(res)
print(f"{res:.2f}")
