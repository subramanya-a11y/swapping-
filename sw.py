a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print("before swapping:")
print("first number =", a)
print("second number =", b)
a, b = b, a
print("after swapping:")
print("first number =", a)
print("second number =", b)