# Simple Calculator

from messages import initial_menu, operation_message
from operations import soma, subtraction, division, multiplication

operations = ["Sum", "Subtraction", "Multiplication", "Division"]
operation_symbol = ["+", "-", "*", "/"]
operation_dict = {'1': soma,
                  '2': subtraction,
                  '3': multiplication,
                  '4': division
                  }

num1 = num2 = 0
chosen_menu = 0
result = 0


def read_menu() -> int:
    """
    Reads number and selects a menu.
    :return: integer representing the chosen menu.
    """

    return int(input())


def read_numbers() -> tuple:
    """
    Reads two numbers and unpacks them.
    :return: a tuple containing two numbers.
    """
    number1 = float(input())
    number2 = float(input())

    return number1, number2


initial_menu()

# Get a valid menu
while True:
    chosen_menu = read_menu()
    if chosen_menu in range(1, 5):
        operation_message(chosen_menu)
        break
    print("Not a valid menu.")
num1, num2 = read_numbers()

# Select operation
for key_dict in str(chosen_menu):
    result = operation_dict[key_dict](num1, num2)

# Output the result.
print("{0} {1} {2} = {3}".format(num1, operation_symbol[chosen_menu - 1], num2, result))
