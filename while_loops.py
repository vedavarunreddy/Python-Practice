'''
mini-bot that accepts messages and ends when you type 'done'.
'''
def mini_bot():
    message_counter = 0
    while True:
        try:
            user_message = input("Say something to me, I am a bot. End the conversation by typing 'done': ")
            message_counter += 1
            if user_message.lower() == "done":
                print(f"You have spoken to me a total of {message_counter} times! I am learning well.")
                break
            else:
                print("We the San-Ti have got your message.")
        except Exception:
            print('Something went wrong, try again', Exception)

mini_bot()


'''
Create an account login function, the user has 2 passwords, either provides access.
'''
def login():
    correct_passwords_list = ['yellow', 'red']
    tries = 1
    max_tries = 11
    while tries <= 10:
        password = input("Enter your password: ")
        tries = tries + 1
        if password in correct_passwords_list:
            print('Welcome aboard -- San-Ti lords')
            break
        else:
            print(f'You have {max_tries - tries} chances left! Perilious situation this!')

login()

'''
Discount to first 3 customers - of 20%.
'''
def discount_customers():
    customer_num = 1
    max_customer_num = 4
    while customer_num != max_customer_num:
        customer = input(f"Enter your name: ").capitalize()
        print(f"You are our customer number {customer_num}. Enjoy 20% on us, {customer}")
        customer_num += 1
    print(f'\nSorry we only had discounts available to {customer_num} customers. All done')

discount_customers()

'''
5 tries only. If the user enters python then print the num of tries he took!
'''

def programming_languages():
    tries = 0
    while tries < 5:
        language_entered = input("Enter a programming language: ").lower()
        tries = tries + 1
        if language_entered == "python":
            print(f'You have guessed accurately in {tries} try Padawan. Progress on to next level! ')
            break
        else:
            print('Wrong programming guess')
            if tries == 5:
                print('You have had your tries - demoted to level 1.')
    
programming_languages()