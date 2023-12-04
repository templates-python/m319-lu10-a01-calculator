#Add import statement for calculator in math_operations package
from math_operations import calculator
def main():
    print(calculator.add(5,5)) # function add from module calc
    print(calculator.mul(5,5)) # function mul from module calc

if __name__ == '__main__':
    main()
