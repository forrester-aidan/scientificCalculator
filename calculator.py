import math  # Imports the Math library into the file


def calculator_menu():  # Initializes the menu and displays it on the screen
    print("Calculator Menu\n---------------\n0. Exit Program\n1. Addition\n2. Subtraction"
          "\n3. Multiplication\n4. Division\n5. Exponentiation\n6. Logarithm\n7. Display Average\n")


def calculations():  # Function that links all the other functions into one menu, used for input options
    calculator_menu()
    totalAmount = 0.0
    numberOfCalculations = 0
    x = 0
    while x < 1:
        value = int(input("Enter Menu Selection: "))
        if value == 0:
            exit_program()
        elif value == 1:
            totalAmount = addition()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 2:
            totalAmount += subtraction()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 3:
            totalAmount += multiplication()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 4:
            totalAmount += division()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 5:
            totalAmount += exponentiation()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 6:
            totalAmount += logarithm()
            numberOfCalculations += 1
            calculator_menu()
        elif value == 7:
            if numberOfCalculations == 0:
                print("\nError: No calculations yet to average!\n")
            else:
                average(totalAmount, numberOfCalculations)
        else:
            print("\nError: Invalid selection!\n")


def exit_program():  # Exits the program
    print("\nThanks for using this calculator. Goodbye!")
    quit()


def addition():  # Asks for both operands and computes the sum
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = operand1 + operand2
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def subtraction():  # Asks for both operands and computes the difference
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = operand1 - operand2
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def multiplication():  # Asks for both operands and computes the product
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = operand1 * operand2
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def division():  # Asks for both operands and computes the quotient
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = operand1 / operand2
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def exponentiation():  # Takes one operand and puts it to the power of the other
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = operand1 ** operand2
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def logarithm():  # Takes the log base of an operand with the other and computes the result
    operand1 = float(input("Enter first operand: "))
    operand2 = float(input("Enter second operand: "))
    result = math.log(operand2, operand1)
    print("\nCurrent Result: " + str(result) + "\n")
    return result


def average(total, numberOfCalculations):  # Displays the average of all calculations made in the program
    print("\nSum of calculations: " + str(total))
    print("Number of calculations: " + str(numberOfCalculations))
    result = round(total / numberOfCalculations, 2)
    print("Average of calculations: " + str(result) + "\n")


if __name__ == '__main__':  # Begins the program
    print("Current Result: 0.0\n")
    calculations()
