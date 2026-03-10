# Python beginner class

# Variables
variables are jars or containers. 

Just like we can store anything in jar, like dal, rice, sugar etc. In variables we can store data. 

So, a variable is a jar and the data that we store is our dal, rice etc.

example

```python
number1 = 10
```

# Data types
Just like, there can be different types of things that can be stored in jar, for example dal, rice, water, oil etc etc. There can be different types of data.

In python data can be
1. Integer
2. Decimal
3. String

## Integer
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

### Arithemtic operator
```
+ 
-
/
*
% -> modulo

7 ko 2 se divide toh remainder -> 1
7%2 = 1
10%3 = 1
12%4 = 0
even % 2 = 0
number%2 =1  -> odd


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
example:
```python
numbers_array = [1,2,3,4]
```

### Loops

#### for loop

Syntax
```python
for <range>:
    <code block>
```
example
```python
for index in range(0, 4):
    print(index)
```


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

##### Concept of stepping

```python
# stepping of 2
for index in range(0, N, 2):
    <code>
```


#### while loop

for loop -> you have to write "I want to eat ice cream" 10 times

while loop -> you have to write "I want to eat ice cream" until i tell you to stop.

syntax:

```python
while <condition>:
    <code block>
    <optionally i can add a breaking condition"
```
example

```python
while True:
    print("I will eat ice cream")
    condition = input("Do you want to continue? (yes/no): ")
    if condition == "yes":
        continue
    elif condition == "no":
        break
    else:
        print("Oye, i asked yes or no")
        exit()
print("Loop ended gracefully")
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

Question 7

There is a password to a device, which is confidential. Password is "pineapple". The user will attempt to unlock the device by writing the password. If the user enters correct password, we print "Device is unlocked" else user can retry. But, can only retry 3 times. If user is unable to guess password in 3 tries, we print "Device locked permanently".

"intuition"
1. i will need a variable to store the actual password
2. i will need to ask user their guessed password.
3. i need to keep track of retries, i will need a variable to store the number of attempts made by user.
4. if user guesses correctly withing allowed retires, we print "Device Unlocked" and exit.
5. If number of attempts are exhausted, then we print "Device unlocked permanently" and exit.

steps:
1. result = "pineapple"
2. for loop from 0 to number of retries which is 3.
    2.a. In loop, we take their guessed password.
    2.b. Then we check if the guessed password is equal to the actual password. If yes, we print and exit
    2.c If not equal, we continue the loop
3. If loop is over, we print and exit


steps:
1. result = "pineapple"
2. retries = 3
3. create a while loop with condition retries > 0
    3a. in this loop, we will take their guessed password
    3b. We will check if guessed password matches result, if yes we will print and exit.
    3c. else, we will reduce retries by 1
4. when loop is over, that means retries are exhausted and we print and return.


### Functions

maths mei formulas
f(x) = 2x+5 calculate this for value of x = 10

2(10) + 5 = 25

programming language mei such formulas are called functions.

function is a piece of code, which executes on demand.


there is a person, ticket collector.
Ticket collector, whenever a person comes, he checks the ticket and if ticket is not present, he takes the fine,


1 person aya => ticket collector operates.

function name is calculator, which takes 2 number and adds it, and return the sum.
f(x, y) = x + y

```python
def function_name(param1, param2, ...):
    <code>
    return <something>
```

a function takes something, does something and returns something

here something can be even nothing.

example for a additon function.

the return statement, exits the function only and returning the value
but exit, quits the entire programming, halting everything.
```python
def addition(number1, number2):
    result = number1 + number2
    return result

result = addition(10, 20)
```

example of a function that returns nothing
```python
def addition(number1, number2):
    result = number1 + number2
    print(result)

addition(10, 20)
```

Always remember, a function is called only on demand.
"If there is any error inside function, it won't be caught unless it is called"

HomeWork 1:
Go over everything we have done, and find as many functions as you can that we used, for example print(), type(), len()

how to spot a function
it has a name, followed by round brackets.

HomeWork 2:
Create a subtract function and call it.

