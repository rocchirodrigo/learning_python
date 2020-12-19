# This file should contain all print messages.

def initial_menu() -> None:
    """
    This should print a welcome message as well as the initial menu
    of operations.
    """
    operations = ["Sum", "Subtraction", "Multiplication", "Division"]

    print("*" * 20)
    print("Calculator 1.0 by rocchirodrigo")
    print("*" * 20)
    print("Choose one operation from the below:")

    for i in range(0, 3 + 1):
        print("{0}. {1}".format((i + 1), operations[i]))
    print("*" * 20)


def operation_message(menu: int) -> None:
    """
    Print selected menu
    :param menu: chosen operation
    :return:
    """
    operations = ["Sum", "Subtraction", "Multiplication", "Division"]
    print(operations[menu - 1] + ". Enter two numbers: ")

def result_message() -> None:

    print("{0} {1} {2} = {3}".format(num1, operation_symbol[chosen_menu - 1], num2, result))
