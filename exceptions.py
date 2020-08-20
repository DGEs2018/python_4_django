import sys

x = int(input("x: "))
y = int(input("y: "))

try:
    result = x/y
except ZeroDivisionError:
    # introducing handling errors
    print("Error: Cannot divide by 0.")
result = x/y

print(f"{x} / {y} = {result}")