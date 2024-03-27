# '''
# functions that call other functions
# '''

# def terminal_1():
#     return "Go to terminal 1"

# def terminal_2():
#     return "Go to terminal 2"

# def terminal_3():
#     return "Go to terminal 3"

# def trip_type():
#     while True:
#         type_of_trip = input("""Is your flight a budget/ domestic or international?. Press N 
#                             to return to home page: """)
#         if type_of_trip.lower() == "budget":
#             print(terminal_1())
#         elif type_of_trip.lower() == "domestic":
#             print(terminal_2())
#         elif type_of_trip.lower() == "international":
#             print(terminal_3())
#         else:
#             print("Leaving this page.")
#             break

# trip_type()


'''
A function that makes BMI calculator.
'''
def BMI_calculator():
    print("I will calculate your BMI! ")
    weight = float(input("What is your weight?: "))
    height = float(input("What is your height?: "))
    BMI = weight / (height * height)
    return BMI

def BMI_results():
    res = BMI_calculator()
    if res < 18.5:
        print("You are underweight.")
    elif 18.5 < res < 25:
        print("You are within the healthy range.")
    else:
        print("Try exercising and eating veggies. You are in the overweight/ obese category.")

def BMI_loop():
    while True:
        try:
            check_BMI_y_n = input("Would you like to check your BMI? Y/N: ").lower()
            if check_BMI_y_n == "n":
                break
            else:
                BMI_results()
        except Exception as e:
            print(e)
            print("Some error happened, lets run the programme again!")

BMI_loop()

