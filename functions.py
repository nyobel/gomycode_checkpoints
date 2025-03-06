# Functions to perform basic operations
def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero"
    return num1 / num2

# Dictionary to assign operation functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    first_num = float(input("Enter the first number: "))

    while True:
        print("\nAvailable operation options: ")
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation from the list above: ")
        
        if operation_symbol not in operations:
            print("Invalid operation. Please try again.")
            continue  # Ask for input again if operation is invalid
        
        second_num = float(input("Enter the second number: "))

        # Retrieve the function from the dictionary
        calculation_function = operations[operation_symbol]

        # Perform the calculation
        answer = calculation_function(first_num, second_num)

        print(f"\n{first_num} {operation_symbol} {second_num} = {answer}")

        # Ask if the user wants to continue with the result
        should_continue = input("Would you like to continue with the result? (yes/no): ").lower()

        if should_continue == "yes" or should_continue == "y":
            first_num = answer  # Update first_num with the last answer
        else:
            print("\nStarting a new calculation...\n")
            calculator()  # Restart the calculator
            break  # Exit the current loop to start fresh

# Start the calculator
calculator()
