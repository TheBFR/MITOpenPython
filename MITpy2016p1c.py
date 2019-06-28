annual_salary = input("What is your annual salary ?: ")
portion_saved = .1
total_cost = 1000000
raise_pct = .07
portion_down_payment = 0.25
current_savings = 0
r = .04 #interest rate each month you get current_savings*r/12
months_to_save = 0
down_payment = total_cost * portion_down_payment
annual_salary_int = int(annual_salary)
#print(annual_salary_int)


while down_payment >  current_savings:
    if months_to_save != 0 and months_to_save %6 == 0:
        annual_salary_int = annual_salary_int + (annual_salary_int * float(raise_pct))
        monthly_salary = annual_salary_int / 12
        monthly_savings = monthly_salary * float(portion_saved)
        #print("Your monthly salary is now", monthly_salary)
    else:
        monthly_salary = annual_salary_int / 12
        monthly_savings = monthly_salary * float(portion_saved)
        #print("Your monthly salary is still", monthly_salary)
    current_savings = current_savings + monthly_savings + ((current_savings*r)/12)
    print(current_savings)
    months_to_save += 1
    #print(months_to_save)


print("That house will take ",months_to_save, "months to save for the down payment")





