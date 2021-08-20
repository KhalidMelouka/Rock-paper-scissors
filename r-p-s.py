from random import randint

print("""
    welcome to rock, paper, scissors. You'll be facing your own computer. 
    if you want to quit, just write <quit>. Enjoy playing.
""")



machine_input = ["rock", "paper", "scissors"]

rand_choice = machine_input[randint(0, len(machine_input)-1)]

keep_play = True

user_score = 0 
computer_score = 0 
while keep_play:
    rand_choice = machine_input[randint(0, len(machine_input)-1)]

    choice = input("rock, paper, scissors: ").lower()


    if choice == rand_choice:
        print(f"both {choice}. try again")
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "rock" and rand_choice == "paper":
        print(f"you chose {choice} and computer chose {rand_choice}. Computer wins")
        computer_score += 1
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "rock" and rand_choice == "scissors":
        print(f"you chose {choice} and computer chose {rand_choice}. You win")
        user_score += 1
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "paper" and rand_choice == "rock":
        print(f"you chose {choice} and computer chose {rand_choice}. You win!")
        user_score += 1 
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "paper" and rand_choice == "scissors":
        print(f"you chose {choice} and computer chose {rand_choice}. Computer wins!")
        computer_score += 1
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "scissors" and rand_choice == "rock":
        print(f"you chose {choice} and computer chose {rand_choice}. Computer wins!")
        computer_score += 1
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "scissors" and rand_choice == "paper":
        print(f"you chose {choice} and computer chose {rand_choice}. You win!")
        user_score += 1
        print(f"user: {user_score} -- computer: {computer_score}")

    elif choice == "quit":
        print("thank you for playing")
        keep_play = False




