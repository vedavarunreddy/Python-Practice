from pay_modules import *



def salary_check(name, salary_type):
    if salary_type == "hourly":
        hrs = float(input("Enter num of hrs worked part time: "))
        salary = hourly_time_salary(hrs)
        return salary
    elif salary_type == "salary":
        experience = float(input("Enter approx. num of years you have worked: "))
        salary = full_time_salary(experience)
        return salary
    else:
        return "You are unemployed"

salary_loop = input("Would you like to check your salary: Y/ N: ").lower()

if salary_loop != "n" or salary_loop != "no":
    while salary_loop != "n":
        name = input("Hi there, enter your last name: ").capitalize()
        salary_type = input("Enter your salary type. hourly or salary: ")
        final_salary = salary_check(name, salary_type)
        print(f"Hi there, {name}! Your salary type is '{salary_type}' and your pay is salary is: {final_salary}.")
        salary_loop = input("\nWould you like to check your salary: Y/ N: ").lower()
        if salary_loop != "y" or "yes":
            print("Returning to the home page. ")
else:
    print("Returning to the home page. ")