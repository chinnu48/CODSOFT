# Function to perform addition
def add(x, y):
    return x + y

# Function to perform subtraction
def subtract(x, y):
    return x - y

# Function to perform multiplication
def multiply(x, y):
    return x * y

# Function to perform division
def divide(x, y):
    return x / y

# Main function to run the calculator
def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    # Take input from the user
    choice = input("Enter choice(1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"The result of {num1} + {num2} is: {add(num1, num2)}")
        elif choice == '2':
            print(f"The result of {num1} - {num2} is: {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The result of {num1} * {num2} is: {multiply(num1, num2)}")
        elif choice == '4':
            if num2 != 0:
                print(f"The result of {num1} / {num2} is: {divide(num1, num2)}")
            else:
                print("Error! Division by zero.")
    else:
        print("Invalid input! Please select a valid operation.")

# Run the calculator
calculator()
