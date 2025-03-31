import math_tools

# Get two numbers from the user
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Ask which operation to perform
operation = input("Choose an operation (add, subtract, multiply, divide): ").strip().lower()

# Perform the calculation
if operation == "add":
    result = math_tools.add(a, b)
elif operation == "subtract":
    result = math_tools.subtract(a, b)
elif operation == "multiply":
    result = math_tools.multiply(a, b)
elif operation == "divide":
    try:
        result = math_tools.divide(a, b)
    except ValueError as e:
        result = f"Error: {e}"
else:
    result = "Invalid operation."

# Show the result
print("Result:", result)