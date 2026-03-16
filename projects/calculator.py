# use this as a reference and write all the functions.
# Run the file and verify.
# def addition(num1, num2):
#     return num1 + num2


print("Welcome to calculator app")
print("Pick one of these options to perform calculation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

option = int(input("Enter your option: "))
if check_valid_operation(option) ==  False:
    print("Invalid option, exiting the app")
    exit()

number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
result = 0
if option == 1:
    result = addition(number1, number2)
if option == 2:
    result = subtraction(number1, number2)
if option == 3:
    result = multiply(number1, number2)
if option == 4:
    result = divide(number1, number2)

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




