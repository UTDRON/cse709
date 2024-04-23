'''
Write a Python program to create a simple calculator. The calculator should be able to perform addition, subtraction, multiplication, and division operations on two numbers entered by the user. The program should keep running until the user chooses to exit.

Your program should:

Display a menu of operations for the user to choose from: Addition (+), Subtraction (-), Multiplication (*), Division (/), or Exit (E).
Prompt the user to select an operation from the menu.
If the user selects an arithmetic operation, prompt the user to enter two numbers.
Perform the selected operation on the two numbers and display the result.
If the user selects "Exit", terminate the program.
Handle invalid input gracefully, displaying appropriate error messages if the user enters invalid choices or non-numeric inputs.
Constraints:

The program should handle both integer and floating-point inputs.
Division by zero should be handled gracefully with an appropriate error message.
Ensure the program continues running until the user chooses to exit.
Consider implementing the calculator logic as functions for better organization and reusability of code.
'''

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        raise ValueError("Cannot divide by zero")
    return num1 / num2

def display_menu():
    print("Calculator Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("E. Exit")

def get_user_choice():
    choice = input("Enter your choice: ")
    return choice.upper()

def get_user_numbers():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    return num1, num2

def calculate():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 'E':
            print("Exiting the calculator...")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice. Please try again.")
            continue

        try:
            num1, num2 = get_user_numbers()

            if choice == '1':
                result = add(num1, num2)
                print(f"The result of addition is: {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"The result of subtraction is: {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"The result of multiplication is: {result}")
            elif choice == '4':
                try:
                    result = divide(num1, num2)
                    print(f"The result of division is: {result}")
                except ValueError as e:
                    print(str(e))
        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculate()
