def calculate(n1, n2, op):
    """
    Perform a calculation based on the operator.
    
    :param n1: First number
    :param n2: Second number
    :param op: Operator (+, -, *, /, ^)
    :return: Result of the calculation
    """
    if op == '+':
        result = n1 + n2
    elif op == '-':
        result = n1 - n2
    elif op == '*':
        result = n1 * n2
    elif op == '/':
        if n2 == 0:
            raise ValueError('Cannot divide by zero')
        result = n1 / n2
    elif op == '^':
        result = n1 ** n2
    else:
        raise ValueError('Invalid operator')

    # Convert to integer if the result is a whole number
    if isinstance(result, float) and result.is_integer():
        result = int(result)

    return result

def get_number(prompt):
    """
    Get a valid number from the user.
    
    :param prompt: Prompt to display to the user
    :return: Valid number as a float
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_operator():
    """
    Get a valid operator from the user.
    
    :return: Valid operator (+, -, *, /, ^)
    """
    valid_operators = ['+', '-', '*', '/', '^']
    while True:
        op = input('Enter operator (+,-,*,/,^): ')
        if op in valid_operators:
            return op
        print("Invalid operator. Please enter one of: +, -, *, /, ^")

def again():
    """
    Ask the user if they want to perform another calculation.
    
    :return: True if the user wants to continue, False otherwise
    """
    while True:
        calc_again = input('Do you want to calculate again? (Y/N): ').upper()
        if calc_again == 'Y':
            return True
        elif calc_again == 'N':
            print('See you later.')
            return False
        else:
            print("Invalid input. Please enter Y or N.")

def main():
    """
    Main function to run the calculator.
    """
    print("Welcome to the Calculator!")
    while True:
        try:
            number1 = get_number('Enter first number: ')
            op = get_operator()
            number2 = get_number('Enter second number: ')
            
            print(f"Calculating: {number1} {op} {number2}")
            result = calculate(number1, number2, op)
            print('Result =', result)
            
            if not again():
                break  # Exit the loop if the user doesn't want to continue
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

# Start the program
if __name__ == "__main__":
    main()