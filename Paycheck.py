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
    bi_weekly_max_hours = 80
    # your hourly pay
    hourly_pay = float(input("how much do you earn per hour? "))
    # total number of hours worked
    hours_worked = float(input("how many hours did you work? "))
    # To check how many weeks you worked
    week = int(input("How many weeks did you work? "))
    # maximum weeks one can work before receiving paycheck
    max_week = 2
    
# checks how many hours and weeks worked
    if hours_worked < weekly_max_hour  and week < max_week  and week >0 and hours_worked >0 and hourly_pay >0:
        earning_before_tax= hourly_pay * hours_worked + weekly_vacation_pay
        earning_after_tax= earning_before_tax -(Total_tax*earning_before_tax)
        print(f"this is your first week and your pay is:{earning_before_tax} ") 
        print(f"{earning_after_tax}: after tax.")
   
    if hours_worked == weekly_max_hour  and week < max_week  and week  and hourly_pay >0:
        earning_before_tax1= hourly_pay * hours_worked + weekly_vacation_pay
        earning_after_tax1 = earning_before_tax1 -(Total_tax*earning_before_tax1)
        print(f"You have only worked one week in two weeks and your pay is:{earning_before_tax1} and") 
        print(f"{earning_after_tax1}: after tax.")
   
        
    elif hours_worked >weekly_max_hour  and hours_worked < bi_weekly_max_hours and week < max_week and week >0 :
        over_time = (hourly_pay * 1.5) * hours_worked + weekly_vacation_pay
        earning_after_tax2 = over_time - (Total_tax * over_time)
        print(f'Hello!, this is your first week and you worked overtime and have earned: {over_time}  ')
        print(f'{earning_after_tax2} after tax deduction') 

    elif hours_worked >weekly_max_hour  and hours_worked == bi_weekly_max_hours and week == max_week :
        total_pay = hourly_pay  * hours_worked + (weekly_vacation_pay*2)
        earning_after_tax2 = total_pay - (Total_tax * total_pay)
        print(f'Hello!, this is your second  week and you have earned: {total_pay} in total  ')
        print(f'{earning_after_tax2} after tax deduction')


    elif hours_worked > weekly_max_hour and hours_worked == bi_weekly_max_hours and week < max_week and week>0:
        over_time1 = (hourly_pay * 1.5) * hours_worked + weekly_vacation_pay
        earning_after_tax2 = over_time1 - (Total_tax * over_time1)
        print(f'Hello!, this is your first week and you worked overtime and have earned: {over_time1}  ')
        print(f'{earning_after_tax2} after tax deduction')


    elif hours_worked > weekly_max_hour and hours_worked < bi_weekly_max_hours and week == max_week:
        total_pay = hourly_pay * hours_worked + (weekly_vacation_pay * 2)
        earning_after_tax2 = total_pay - (Total_tax * total_pay)
        print(f'Hello!, this is your second  week and you have earned: {total_pay} in total  ')
        print(f'{earning_after_tax2} after tax deduction')

    elif hours_worked < weekly_max_hour   and week == max_week and hourly_pay >0:
        earning_before_tax3 = (hourly_pay * hours_worked) + (weekly_vacation_pay*2)
        earning_after_tax3 = earning_before_tax3 - (Total_tax*earning_before_tax3)
        print(f"Hi! {earning_before_tax3} is your two weeks pay before tax")
        print(f"{earning_after_tax3} after tax deductions.") 

    elif hours_worked == weekly_max_hour   and week == max_week  :
        earning_before_tax4 = (hourly_pay * hours_worked) + (weekly_vacation_pay * 2)
        earning_after_tax4 = earning_before_tax4 - (Total_tax*earning_before_tax4)
        print(f"Hi you did not work overtime! your two weeks pay is {earning_before_tax4} before tax")
        print(f" ${earning_after_tax4} after tax deductions.")

    elif hours_worked > weekly_max_hour  and hours_worked > bi_weekly_max_hours and week == max_week :
        total_overtime = (hourly_pay * 1.5) * hours_worked + (weekly_vacation_pay*2)
        earning_after_tax5 = total_overtime - (Total_tax*total_overtime)
        print(f"Your total earning in two weeks including your overtime before tax is ${total_overtime}")
        print(f"${earning_after_tax5}: after tax deduction")
    
    elif hours_worked > weekly_max_hour  and hours_worked > bi_weekly_max_hours and week < max_week and week >0 :
        total_overtime = (hourly_pay * 1.5) * hours_worked + (weekly_vacation_pay*2)
        earning_after_tax5 = total_overtime - (Total_tax*total_overtime)
        print(f"Your total earning in one week and including your overtime before tax is ${total_overtime}")
        print(f"${earning_after_tax5}: after tax deduction")

 # checks if you input zero hour
    elif hours_worked <=0 and week >=0 and hourly_pay >=0:
        print("you have zero hours worked enjoy your break")
# checks if you input zero week  
    elif hours_worked >= 0 and week <= 0 and hourly_pay >= 0:
        print("you have not worked this week enjoy your break")
# checks if you input zero hourly pay  
    elif hours_worked >= 0 and week >= 0 and hourly_pay <=0:
        print(" you have not come to work ")
        
# checks if the week is more than maximum week  
    else :
        if week > max_week and hours_worked >=0 and hourly_pay >=0:
            print("please check with the HR!")

my_pay()










