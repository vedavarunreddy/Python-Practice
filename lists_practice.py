'''
A simple fruit game using lists
'''
def fruit_game():
    fruit_list = []

    fruit = input("Enter the name of a fruit: ").capitalize()
    fruit_list.append(fruit)

    while fruit != "Quit":
        fruit = input("Enter fruit: ").capitalize()
        fruit_list.append(fruit)
        
        if fruit == "Quit":
            guess = input("Guess a fruit: ")
            if guess in fruit_list:
                print("Congrats, you guessed correctly")
            else:
                print("Sorry, thats not the correct answer")
            
            fruit_list.pop()           
            print(f"\nThe fruit list was: {fruit_list}")    

# fruit_game()

####################################
