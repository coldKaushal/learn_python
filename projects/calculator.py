# use this as a reference and write all the functions.
# Run the file and verify.
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        print("undefined")
        exit()
    return num1 / num2
def check_valid_operation(option):
    if option >= 1 and option <= 4:
        return True
    return False

# this is called refactoring
def calculator(option, num1, num2):
    result = 0
    if option == 1:
        result = addition(num1, num2)
    if option == 2:
        result = subtraction(num1, num2)
    if option == 3:
        result = multiply(num1, num2)
    if option == 4:
        result = divide(num1, num2)
    return result

def print_menu():
    print("Welcome to calculator app")
    print("Pick one of these options to perform calculation")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")


# main function
if __name__ == "__main__":
    print_menu()
    option = int(input("Enter your option: "))
    if check_valid_operation(option) ==  False:
        print("Invalid option, exiting the app")
        exit()

    number1 = int(input("Enter first number: "))
    number2 = int(input("Enter second number: "))

    result = calculator(option, number1, number2)
    print("The result is: ", result)

## TODOs
# In total we need to write 5 functions.
# 1st function -> check_valid_operation -> this function will take option as parameter
# and return true if option is between 1 and 4, else return false.

# 2nd function -> addition -> this function will take 2 numbers as parameter and return their sum.

# 3rd function -> subtraction -> this function will take 2 numbers as parameter
# and return their difference.

# 4th function -> multiply -> this function will take 2 numbers as parameter and return their product.

# 5th function -> divide -> this function will take 2 numbers as parameter and return their 
# quotient. if second number is 0, then it should return "undefined" and exit the program.




