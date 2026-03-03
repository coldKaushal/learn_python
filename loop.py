
# dessert_train = ["ice cream", "cake", "cookies", "brownies", "pie"]
# for index in range(0, 5):
#     print(index)
#     print(dessert_train[index])

# print("loop ended at index: ", index)


# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
# num4 = int(input("Enter fourth number"))
# num5 = int(input("Enter fifth number"))


# print(num1 + num2 + num3 + num4 + num5)


# number_array = [0, 0, 0, 0, 0]
# for index in range(0, 5):
#     num = int(input("Enter your number"))
#     number_array[index] = num


# print(number_array[0] + number_array[1] + number_array[2] + number_array[3] + number_array[4])
# # 2nd when we will learn functions


# result = 0
# for index in range(0, 5):
#     num = int(input("Enter a number: "))
#     result = result + num

# print("Total sum is: ", result)

# dessert_train = ["ice cream", "cake", "cookies", "brownies", "pie"]

# for dessert in dessert_train:
#     # This makes the copy of array's elements, not actually an element.
#     dessert = "abcd"

# print(dessert_train)



# for index in range(0, 5):
#     # This changes because its an actual element.
#     dessert_train[index] = "abcd"

# print(dessert_train)

# # range(0, 5) is same as making an array [0, 1, 2, 3, 5]

# print(list(range(0, 5)))


# for count in range(1, 6):
#     print("#"*count)

# name = input("Tell me your name: ")

# subjects = int(input("Tell me total subjects: "))
# result = 0
# for subject in range(0, subjects):
#     marks = int(input("Tell me your marks: "))
#     result += marks

# print("Total percentage of student is: ", result/subjects)


# Printing even numbers between 0 and 50
# for number in range(0, 50, 2):
#     print(number)

# print(list(range(0, 50, 2)))

# steps:
# 1. result = "pineapple"
# 2. for loop from 0 to number of retries which is 3.
#     2.a. In loop, we take their guessed password.
#     2.b. Then we check if the guessed password is equal to the actual password. If yes, we print and exit
#     2.c If not equal, we continue the loop
# 3. If loop is over, we print and exit

result = "pineapple"
for retry in range(0, 3):
    guessed_password = input("Enter your guessed password: ")
    if guessed_password == result:
        print("You guessed it right!")
        exit()
    else:
        print("Wrong password, try again!")

print("You have exhausted all your retries, better luck next time!")