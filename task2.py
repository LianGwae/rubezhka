calculator = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y,
    '^': lambda x, y: x ** y,
}

print("Please chose the task you want to perform:")
print("1. Addition")
print("2. Multiplication")
print("3. Division")
print("4. Exponentiation")

user_input = input("User Input: ")

try:
    operation = calculator[user_input]
    num1, num2 = map(float, input("Please enter two numbers for operation, comma separated\n").split(','))
    result = operation(num1, num2)
    print("Result:", result)
except Exception as e:
    print("Error:", str(e))