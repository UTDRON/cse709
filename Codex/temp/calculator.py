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

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

def display_menu():
    print("Menu:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit (E)")

def get_user_choice():
    while True:
        choice = input("Enter your choice: ").strip().upper()
        if choice in ['1', '2', '3', '4', '5', 'E']:
            return choice
        else:
            print("Error: Invalid choice. Please enter a valid operation from the menu.")

def get_numbers():
    while True:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            return num1, num2
        except ValueError:
            print("Error: Please enter numeric values.")

def main():
    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 'E':
            print("Thank you for using Simple Calculator!")
            break

        num1, num2 = get_numbers()

        if choice == '1':
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
