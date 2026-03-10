
number1 = 30
number2 = 20

#multiple -> 6

if number1 > number2:
    print("Yes")
else:
    print("No")



name = "kaushal"
if name == "kaushal":
    print("Hello, Kaushal!")
else:
    print("Hello, stranger!")


# normal if else
if number1 > number2:
    print("Yes")
elif name == "kaushal":
    print("Hello, Kaushal!")
else:
    print("Else")


number1 = 30
number2 = 20
number3 = 10
number4 = 5

#nested
if number1 > number2:
    if number3 > number4:
        print("number1 is greater than number2 and number3 is greater than number4")
    else:
        print("number1 is greater than number2 but number3 is not greater than number4")
else:
    print("number1 is not greater than number2")

if number1 > number2:
    print("number1 is greater than number2")
elif number3 > number4:
    print("number3 is greater than number4")
else:
    print("number1 is not greater than number2 and number3 is not greater than number4")


if number3 > number1:
    print("number3 is greater than number1")
else:
   print("number3 is not greater than number1")


# normal if else

# if condition is true -> we do stuff
# elif = if upar condition is false and this condition is true -> then we do stuff
    

# nested

# if condition is true -> then we have another condition.


# summary 

# multiple if else = 2 or more independent if else statements in a code.
# normal if else = 1 if else statement in a code.
# nested if else = an if else statement inside another if else statement.



# there are 2 conditions to meet, if both conditions are true we do one then thing else we dont do anything anything

# weather = "sunny"
# temperature = 30

# user se hum weather lenge, aur temperature lenge. agr dono same hai, 
# toh hum print karenge "Go outside and play". 
# else we will print "Stay inside and study"

# weather = input("Enter the weather: ")
# temperature = int(input("Enter the temperature: "))

# if weather == "sunny":
#     if temperature == 30:
#         print("Go outside and play")
#     else:
#         print("Stay inside and study")
# else:
#     print("Stay inside and study")



# if weather == "sunny" and temperature == 30:
#     print("Go outside and play")
# else:
#     print("Stay inside and study")


# if weather == "sunny" or temperature == 30:
#     print("Go outside and play")
# else:
#     print("Stay inside and study")
