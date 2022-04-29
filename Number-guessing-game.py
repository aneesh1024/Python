# Method 1

import random
win_num = random.randint(1,100)
num = 1
num_guess = int(input("Guess the number between 1 and 100 : "))
while win_num != num_guess:
    if num_guess < win_num:
        print("Too Low")
    else:
        print("Too High")
    num_guess = int(input("Guess Again : "))
    num+=1
print(f"Congrats ! You guessed the correct number in {num} tries")

# Method 2

import random
win_num = random.randint(1,100)
guess = 1
num_guess = int(input("Guess the number between 1 and 100 : "))
game_over = False
while not game_over:
    if win_num == num_guess:
        print(f"Congrats ! You guessed the correct number in {num} tries")
        game_over = True
    elif num_guess < win_num:
        print("Too Low")
        num_guess = int(input("Guess Again : "))
    else:
        print("Too High")
        num_guess = int(input("Guess Again : "))
    guess += 1

