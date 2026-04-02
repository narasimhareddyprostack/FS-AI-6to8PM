import random

sys_guess=random.randint(1,50)

is_guess=True
while is_guess:
    user_guess=int(input("Enter Number to Guess:"))

    if user_guess==sys_guess:
        print("Guess is Right")
        is_guess=False
    elif user_guess>sys_guess:
        print("Too High")
    else:
        print("Too Low")

