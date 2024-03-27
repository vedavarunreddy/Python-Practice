'''
mini-lottery programme using random module
'''
from random import randint 

def user_random_number():
    while True:
        try:
            number_picked = int(input("Input a non-negative number, you might win the lottery!: "))
            return number_picked
        except Exception as e:
            print(e)
            print("Select a positive number only b/w 0 and 100, and no decimals!")
            continue
        

def computer_generated_number():
    computer_picked_number = randint(1,100)
    return computer_picked_number

def lottery_programme():
    for _ in range(3):
        user_num = user_random_number()
        computer_num = computer_generated_number()
        if user_num == computer_num:
            print(f"You win!\nComputer selected: {computer_num}\nYou selected: {user_num}")
            break
        elif user_num > computer_num:
            print("Too high - Try again!")
        else:
            print("Too low - Try again!")
    print("\nThat is your 3 tries. Unlucky! Perhaps buy another ticket for 3 more goes?")

def lottery_game():
    while True:
        game_play = input("Would you like to play a lottery game against me? Y/N: ").lower()
        if game_play == "y" or game_play == "yes":
            lottery_programme()
        else:
            break

lottery_game()