a = int(input("a: "))
b = int(input("b: "))

print(f"a: {a}, b: {b}")

b = b - a
a = b + a
b = a - b

print(f"a: {a}, b: {b}")
