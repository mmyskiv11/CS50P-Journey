'''
Einstein - make a program to calculate Einstein energy formula where E=mc^2.
- https://cs50.harvard.edu/python/2022/psets/0/einstein/
'''
# Mass is inputted by user
m = int(input("input mass in kg: "))
c = 300_000_000
E = m*(c**2)
print(f"E: {E}")
