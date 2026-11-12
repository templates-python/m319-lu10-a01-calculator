"""Task 4: import the functions add and mul from calc under the aliases addition and multiplication."""


# Add import statement for add as addition and mul as multiplication from calc

def add(num1, num2):
    """
    Builds the sum of two numbers and prints the result
    :param num1: first number
    :param num2: second number
    :return: None
    """
    print(num1 + num2)


def mul(num1, num2):
    """
    Miltiplies of two numbers and prints the result
    :param num1: first number
    :param num2: second number
    :return: None
    """
    print(num1 * num2)


def main():
    """
    Calls the local and the imported add and mul functions.
    """
    add(5, 5)
    mul(5, 5)
    print(addition(5, 5))  # function add from module calc
    print(multiplication(5, 5))  # function mul from module calc


if __name__ == '__main__':
    main()