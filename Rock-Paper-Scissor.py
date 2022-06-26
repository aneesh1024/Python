import random
print("\t\t\t---------------------")
print("\t\t\t|ROCK PAPER SCISCOR |")
print("\t\t\t---------------------")
start = input("Start the game ? : ")
while start.lower() == 'y' or start.lower() == 'yes':
    player_win = 0
    cpu_win = 0
    # Determining the choice of cpu
    cpu_choice = random.randint(1,3)
    if cpu_choice == 1:
        cpu_choice = 'r'
    if cpu_choice == 2:
        cpu_choice = 'p'
    if cpu_choice == 3:
        cpu_choice = 's'
    num_of_games = int(input("How many games you want to play : "))
    for i in range(0,num_of_games):
        print(f"Game no. {i+1}")
        choice = input("Enter your choice(r/p/s) : ")
        if choice == cpu_choice:
            if choice == 'r':
                print("Both player and CPU chose Rock")
            elif choice == 'p':
                print("Both player and CPU chose Paper")
            elif choice == 's':
                print("Both player and CPU chose Scissor")
            print("It's a Tie")
        elif choice == 'r' and cpu_choice == 'p':
            print("Player chooses Rock\nCPU chooses Paper")
            print("CPU Wins")
            cpu_win += 1
        elif choice == 'r' and cpu_choice == 's':
            print("Player chooses Rock\nCPU chooses Scissor")
            print("Player Wins")
            player_win += 1
        elif choice == 'p' and cpu_choice == 'r':
            print("Player chooses Paper\nCPU chooses Rock")
            print("Player Wins")
            player_win += 1
        elif choice == 'p' and cpu_choice == 's':
            print("Player chooses Paper\nCPU chooses Scissor")
            print("CPU Wins")
            cpu_win += 1
        elif choice == 's' and cpu_choice == 'p':
            print("Player chooses Scissor\nCPU chooses Paper")
            print("Player Wins")
            player_win += 1
        elif choice == 's' and cpu_choice == 'r':
            print("Player chooses Scissor\nCPU chooses Rock")
            print("CPU Wins")
            cpu_win += 1
    print(f"CPU WIns = {cpu_win}\nPlayer Wins ={player_win}")
    if player_win > cpu_win:
        print("Player Wins this Match:)")
    elif player_win < cpu_win:
        print("CPU Wins this match, Better luck next time")
    else:
        print("TIE !!!")
    start = input("Play another game ?(y/n) : ")
