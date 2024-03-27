'''
Its my modules file to import specific functions for other programs.
'''

def full_time_salary(experience):
    ANNUAL_PAY = 25000 #25000 dollars/ $
    if 2 <= experience < 4:
        BONUS = 500
        pay = (ANNUAL_PAY * 1.5) + BONUS
    elif 4 <= experience < 10:
        BONUS = 1000
        pay = (ANNUAL_PAY * 2) + BONUS
    elif experience >= 10:
        BONUS = 1500
        pay = (ANNUAL_PAY * 3) + BONUS
    else:
        BONUS = 200
        pay = ANNUAL_PAY + BONUS
    return pay

def hourly_time_salary(hrs_worked):
    HOURLY_PAY = 25 #25 dollars/ $
    pay = hrs_worked * HOURLY_PAY
    return pay


