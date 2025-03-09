#importing libraries
import math

class Calculator:
    def __init__(self):
        # initialize an empty dictionary for operations
        self.operators = {}

        # Initialize the dictionary with basic mathematical operations
        self.add_operation("+", lambda a, b: a + b)
        self.add_operation("-", lambda a, b: a - b)
        self.add_operation("*", lambda a, b: a * b)
        self.add_operation("/", lambda a, b: a / b)


    def add_operation(self, operation_symbol, operation_function):
        # Check if the operation_function is callable
        if not callable(operation_function):
            raise ValueError("The operation function must be callable")
        # Add the operation symbol and its corresponding function to the dictionary
        self.operators[operation_symbol] = operation_function


    def calculate(self, num1, operation_symbol, num2):
        # Validate that both num1 and num2 are numbers
        if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
            print(f"Error: Both inputs must be numbers.")
            raise ValueError("Non-numeric input provided. Please enter a number and try again.")
        
        # Check if operation symbol exists in the dictionary
        if operation_symbol not in self.operators:
            print(f"Error: The operation symbol {operation_symbol} is not supported by the program.")
            raise ValueError("Invalid operation symbol.")
    
        # Check for division by zero
        if operation_symbol == '/' and num2 == 0:
            print("Error: Please enter a number apart from 0. Division by 0 is not applicable in this program.")
            raise ValueError("Division by zero.")
        
        #Retrieve the function corresponding to the operation symbol
        operation_function = self.operators[operation_symbol]

        #Execute the operation function with num1 and num2
        result = operation_function(num1, num2)
        return result
    

# define advanced mathematical functions separately
def exponentiation(a, b):
    return a ** b

def square_root(a, dummy=None): 
    #The "dummy" parameter is used as a placeholder so that the function's signature matches this two-argument interface.
    return math.sqrt(a)
        
def logarithm(a, base=None):
    return math.log(a) if base is None else math.log(a, base)

#create an instance of the class
calc = Calculator()

#add advanced operations to the calculator add_operation dictionary
exponent = calc.add_operation("^", exponentiation)
sqrt = calc.add_operation("sqrt", square_root)
log = calc.add_operation("log", logarithm)


# Main program loop
while True:
    print("\n--- Calculator ---")
    # Ask the user if they want to quit
    choice = input("Enter 'q' to quit or press Enter to continue: ")
    if choice.lower() == 'q':
        break

    try:
        # Get the first number from the user
        num1 = float(input("Enter the first number: "))
        # Get the operator symbol
        operation_symbol = input("Enter an operator (e.g., +, -, *, /, ^, sqrt, log): ")
        # Get the second number from the user
        num2 = float(input("Enter the second number: "))
        
        # Perform the calculation using the Calculator instance
        result = calc.calculate(num1, operation_symbol, num2)
        print("Result:", result)
    
    except Exception as e:
        # If an error occurs, print the error and continue the loop
        print("Error:", e)
