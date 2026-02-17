
print("Select which operation you want to do:")
print("1. Add two numbers")
print("2. Subtract two numbers")
print("3. Multiply two numbers")
print("4. Divide two numbers")


operation_choice = input("Enter the number corresponding to the operation: ")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# indentation is important in python, make sure to indent the code block under the if statement
if operation_choice == '1':
    result = num1 + num2
    print(result)
elif operation_choice == '2':
    result = num1 - num2
    print(result)
elif operation_choice == '3':
    result = num1 * num2
    print(result)
elif operation_choice == '4':
    if num2 != 0:
        result = num1 / num2
        print(result)
    else:
        print("Error: Cannot divide by zero.")
else:
    print("Invalid choice. Please select a valid operation.")




