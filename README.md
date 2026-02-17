# Python beginner class

### Variables
variables are jars or containers. 

Just like we can store anything in jar, like dal, rice, sugar etc. In variables we can store data. 

So, a variable is a jar and the data that we store is our dal, rice etc.

example

```python
number1 = 10
```

### Data types
Just like, there can be different types of things that can be stored in jar, for example dal, rice, water, oil etc etc. There can be different types of data.

In python data can be
1. Integer
2. Decimal
3. String

#### Integer
integers, are whole numbers from negative to positive
example, 10, -10, 0 etc

```python3
number1 = 10
print(type(number1))
```


### Conditional

Conditional statements.

Syntax

```python
if <condition1>:
    <code 1>
elif <condition2>:
    <code 2>
elif ...
else
```

example
```python
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

if number1 > number2:
    print("I won!")
elif number2 > number3:
    print("You won!")
else:
    print("It's a tie!")
```

### Comparison operator
```python
==

>

<

!=
```


## Project 1

We will ask user, what operation they want to do, like addition, subtraction, multiplication and division.
Based on what user wants, we will do that operation.
Then we will take 2 numbers from user and apply that operation. 

Q1: You will ask user their password.
If password is equal to 12345678 then you will print, "Access granted"
else, you have to print
"Access denied"


Q2: You will ask, user their marks out of 100.
If mark is above 90. We will tell them that their grade is A.
If mark is above 80, then grade is B
If mark is above 70, grade is C
if mark is above 60, grade is D.
if mark is above 40, grade is E.
else, grade is F

Q3: we will ask, what is the weather and the temperature.

If weather is sunny and temperature is less than 30, then we will go out and play.
If weather is sunny, but temperature is above 30, we will put sunscreen
else, if it is not sunny and is raining, then we will take umbrella and go out.
else if it is thunderstorm, then stay inside.
else go work.


### Arrays
is a data type.
which is a collection of other data types.


type of array is a list
to get total number of elements in an array we use len(variable_name)
to print complete array we just print the variable print(variable_name)

say length of array is N
then range is [0, N)
positive range -> [0, N)
negative range -> [-1, -N] -> gives opposite list.

-1 means last element.


### Loops

#### for loop

for <range>:
    <code block>


for index in range(0, 4):
    print(index)



index = 0 and end at 3

when index value is 0, the code runs for this index value
after the code in indentation ends, the value of index needs to be incremented only if it hasn't reached the end.
and then code will run again, index = 1, then again index needs to be incremented only if it hasn't reached the end.
index = 2, then again code will run, again index needs to be incremented...
index =3, then again code will run, again index needs to be incremented. 

then loop will end.


Q4:
You will ask user a number 5 times.
And return the sum of all 5 numbers.

Q5:
You will ask user a number 7 times.
And return the multiplication of all 7 numbers.


Step:
1. create a variable "result" with value of 1.
2. Create a loop that runs 7 times
    2a. In that loop take a number from user and store it in a variable, called "num"
    2b. we will multiple result with that number and store the valure in "result"
3. Print the final result.


Step:
1. Take a number from user, and store it in n.
2. result = n
3. Create a loop that runs for 6 times.
    3a. Take a number from the user and store in a variable
    3b. multiply that number with result and store in the result.
4. print the result.


Q6:
Print # triangle of 10 lines



Step:
1. Create a loop that runs 10 times, denoting 10 lines.
    1a. In each iteration, print "#" number of line times.

Hint: to print "#" 5 times, we can write
print("#"*5)


#### while loop



for loop -> you have to write "I want to eat ice cream" 10 times

while loop -> you have to write "I want to eat ice cream" until i tell you to stop.

syntax:

```python
while <condition>:
    <code block>
    <optionally i can add a breaking condition"
```



Question 7

Guess game: There will be a system generated number, with value 58.
We will take a number from user, if the number is greater than system generated number we will print, "You won"
else, we will continue to ask a number from user.


Steps

1. Create a system generated number with value 58.

2. Take a number from user

3. Create a while loop that runs if the number is less than or equal to the system generated number.

    3a. Print -> Try again

    3b. Take the number from user again
    
4. Print -> You won