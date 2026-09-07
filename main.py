def greet(name):
    print(f"Hello, {name}!")

greet("World")

def add(a, b):
    return a + b


#function for adding 2 numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
result = add(num1, num2)

print(f"The sum of {num1} and {num2} is: {result}")
