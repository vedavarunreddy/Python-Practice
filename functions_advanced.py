def person_info(name, age, nationality):
    print("Welcome:", name)
    print("You are:", age)
    print("You are:", nationality)

number = int(input("Amount: "))
for i in range(number):
    name = input("Enter your name: ").capitalize()
    age = input("Enter your age: ")
    nationality = input("Enter your nationality: ").capitalize()
    person_info(name, age, nationality)
    

'''
creating a function that accepts a score as a paramater
'''
score = int(input("Enter your test score to check your grade: "))
def grade_checker(score):
    if 0 <= score <= 50:
        outcome = "Below passing, practice more to improve your grade."
    elif 50 < score <= 70:
        outcome = "Barely passing the class..."
    elif 70 < score <= 90:
        outcome = "You have a passing grade - for now!"
    else:
        outcome = "You are the San-ti, smashing it!"
    return outcome

print(grade_checker(score))


'''
create a function to add on extra flight charges for upgrading and for bags
'''
base_fare = int(input("What is your base fare price?: "))
def flight_charges(base_fare):
    upgrade_choice = input("Would you like to upgrade? Y/N : ").lower()
    additional_baggage = int(input("Would you like extra bags? Is so, enter b/w 0 and N: "))
    additional_baggage_cost_per_unit = 35
    baggage_cost = additional_baggage * additional_baggage_cost_per_unit
    tax = 1.08
    
    if upgrade_choice == "y" or "yes":
        base_fare += 99
        if baggage_cost == 0:
            base_fare = (base_fare + baggage_cost) * tax #tax and total cost
            return base_fare
        elif baggage_cost > 0:
            base_fare = (base_fare + baggage_cost) * tax
            return base_fare
    elif upgrade_choice == "n" or "no":
        if baggage_cost == 0:
            base_fare = (base_fare + baggage_cost) * tax #tax and total cost
            return base_fare
        elif baggage_cost > 0:
            base_fare = (base_fare + baggage_cost) * tax
            return base_fare

print(flight_charges(base_fare))

'''
bank balance function 
'''

def bank_balance(balance):
    if balance >= 500:
        return True
    else:
        return False

def num_of_customers(): 
    num_of_customers = int(input("Num of customers: "))
    return num_of_customers

def customer_loop(cust_count):
    for i in range(cust_count):
        balance = int(input("Hey what is your balance in the bank?: "))
        name = input("What is your name?: ")
        balance_check = bank_balance(balance)
        if balance_check:
            print(f"Don't worry {name.capitalize()}, you have funds")
        else:
            print(f"Your account is low {name.capitalize()}. Consider depositing some funds.")

cust_count = num_of_customers()
customer_loop(cust_count)


     