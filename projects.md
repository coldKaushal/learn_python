# Projects

## How to make a good project
1. A project always have lots of pieces of code that needs to execute on demand.
2. So, we create a main function, which is executed only
3. Any other work that needs to be done, will be done by main function.
4. We try to keep the code modular -> that means we group logical part in functions

example
Lets assume there is railway corp
railywat corp has several works
for example: Ticket checker, Train driver, cleaning staff, kitchen staff.

all these are like our function
only 1 will start the work, i am the admin (this is like main function)
i will call whoever i want to do the work, whenver needed.


## Good practice
Pactice 1
always write code that needs to run under main
inside

```python
if __name__ == "__main__":
    <code>
```

Practice 2:
Always create functions to write one type of logical part -> this improves redability and maintanibility and less space.

Practice 3:
Always create meaningful variable names and function names

example of bad name
```python
def abc(n, m):
    return n+m
```
example of good name
```python
def addition(number1, number2):
    return number1 + number2
```

## Project 1: Calculator

We will ask user what type of operation they want to perform.
For this, we will give 4 options
Option 1: Addition
Option 2: Subtraction
Option 3: Multiplication
Option 4: Division

Now user can pick one of these options, by providing input like, 1, 2, 3 or 4.
But if user provides anything else, we will print invalid and exit the program.
Else, we will ask 2 numbers from user.
Then based on the option they selected, we will do that operation and return the result.