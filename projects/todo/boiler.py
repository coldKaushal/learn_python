







def validation():

def add_task():

def view_task():

def exit_program():

def menu():

    

# This is the main function of our program, this is where we will call all the other functions, it is like an orchestrator.
def todo_app():
    # This is an infinite loop, because we want to do the process over and over until user exits the program.
    while True:
        menu()
        user_choice = int(input("Enter your option: "))
        validition()
        if user_choice == 1:
            add_task()
        elif user_choice == 2:
            view_task()
        elif user_choice == 3:
            exit_program()

# We are writing this If condition to make sure that this code runs only when we run this file, and not when we import this file in some other file.
if __name__ == "__main__":
    # This is the entry point of our program, this is where our program starts execution.
    todo_app()