"""
        The goal of this application is to assist you in
        calculating how much money you will receive in each
        paycheck after taxes have been deducted.
        You have to know the total deduction removed such as CCP,EI,Tax 
        which can always be seen on your paystub
        and again this is designed for bi-weekly pay 
        and I use the 'max_week to specifically show that we can only work 
        maximum of two weeks.1 means first week and 2 means second week.
        So, when you are asked how many weeks you have to choose only 1 or 2.
"""

def my_pay():

    weekly_vacation_pay= 45.47
    # Tota deduction in percentage
    Total_tax = 0.2046
    weekly_max_hour = 40.0
    # your hourly pay
    hourly_pay = float(input("how much do you earn per hour? "))
    # total number of hours worked
    hours_worked = float(input("how many hours did you work? "))
    # To check how many weeks you worked
    week = int(input("How many weeks did you work? "))
    # maximum week one can work before receiving paycheck
    max_week = 2

    if hours_worked <= weekly_max_hour and week < max_week  and week >0:
        earning_before_tax1= hourly_pay * hours_worked + weekly_vacation_pay
        earning_after_tax1 = earning_before_tax1 -(Total_tax*earning_before_tax1)
        print(f"this is your first week and your pay is:{earning_before_tax1}") 
        
    elif hours_worked >weekly_max_hour  and week < max_week and week >0:
        over_time = (hourly_pay * 1.5) * hours_worked + weekly_vacation_pay
        earning_after_tax2 = over_time - (Total_tax * over_time)
        print(f'Hello!, this is your first week and you have earned: {over_time}  ')
        print(f'{earning_after_tax2} after tax deduction') 

    elif hours_worked < weekly_max_hour  and week == max_week and week >0:
        earning_before_tax3 = (hourly_pay * hours_worked) + (weekly_vacation_pay*2)
        earning_after_tax3 = earning_before_tax3 - (Total_tax*earning_before_tax3)
        print(f"Hi! your earning is {earning_before_tax3} before tax")
        print(f"{earning_after_tax3} after tax deductions.") 

    elif hours_worked >=weekly_max_hour  and week == max_week and week >0:
        earning_before_tax4 = (hourly_pay * hours_worked) + (weekly_vacation_pay * 2)
        earning_after_tax4 = earning_before_tax4 - (Total_tax*earning_before_tax4)
        print(f"Hi! you earnig is {earning_before_tax4} before tax and {earning_after_tax4} after tax deductions.")
    elif hours_worked ==0 and week == 0:
        print("enjoy your break")
    else :
        if week > 2 and hours_worked >0 and hourly_pay >0:
            print("week can't be more than 2 thanks!")
        
           

my_pay()










