

# while True means that it will always be true condition
# uncontrolled loop -> infinite loop
# while True:
#     print("I will eat ice cream")
#     condition = input("Do you want to continue? (yes/no): ")
#     if condition == "yes":
#         continue
#     elif condition == "no":
#         break
#     else:
#         print("Oye, i asked yes or no")
#         exit()

# print("Loop ended gracefully")


# while False means that it will never be true condition hence it will never execute the code block inside it
# while False:
#     print("I will eat ice cream")


# Question:
# We will ask a user a number between 0 - 10
# And there will a number already defined by the system.
# If the user guesses the number correctly, we will print "You won" else we will keep asking the number until the user guesses it correctly.


# result = 7
# number = int(input("Guess the number between 0 and 10: "))

# while number != result:
#     print("Wrong guess, try again!")
#     number = int(input("Guess the number between 0 and 10: "))

# print("You won!")

# This will run forever
# while True:
#     print("i want to eat ice cream")

# This will run once
# if True:
#     print("I want to eat ice cream")

# Question 7 solution

# name = input("Tell me your name: ")
# subjects = int(input("Tell me total subjects: "))
# result = 0
# counter = 0

# while counter < subjects:
#     marks = int(input("Tell me your marks: "))
#     result += marks 
#     counter += 1

# percentage = result / subjects
# print("Your percentage is: ", percentage)

# Guess game: There will be a system generated number, with value 58.
# We will take a number from user, if the number is greater than system generated number we will print, "You won"
# else, we will continue to ask a number from user.

# if number is greater than system wala number => loop mei nahi jana chaiye

# result = 58
# number = int(input("Enter your number: "))

# while number <= result:
#     print("Wrong guess, try again!")
#     number = int(input("Enter your number: "))

# print("You won!")

# steps:
# 1. result = "pineapple"
# 2. retries = 3
# 3. create a while loop with condition retries > 0
#     3a. in this loop, we will take their guessed password
#     3b. We will check if guessed password matches result, if yes we will print and exit.
#     3c. else, we will reduce retries by 1
# 4. when loop is over, that means retries are exhausted and we print and return.

result = "pineapple"
retries = 3
while retries > 0:
    guessed_password = input("Enter your guessed password: ")
    if guessed_password == result:
        print("You guessed it right!")
        exit()
    else:
        print("Wrong password, try again!")
        retries =  retries - 1

print("You have exhausted all your retries, better luck next time!")
