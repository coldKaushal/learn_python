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

name = input("Tell me your name: ")

subjects = int(input("Tell me total subjects: "))
result = 0
for subject in range(0, subjects):
    marks = int(input("Tell me your marks: "))
    result += marks

print("Total percentage of student is: ", result/subjects)
