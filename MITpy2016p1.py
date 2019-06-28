annual_salary = input("What is your annual salary ?: ")
portion_saved = input("What portion of your salary will you save in decimal pct ?: ")
total_cost = input("What is the cost of your dream home ?: ")

portion_down_payment = 0.25
current_savings = 0
r = .04 #interest rate each month you get current_savings*r/12
monthly_salary = int(annual_salary)/12
print(monthly_salary)
print(type(monthly_salary))
monthly_savings = monthly_salary * float(portion_saved)
months_to_save = 0
down_payment = int(total_cost) * portion_down_payment



while down_payment >  current_savings:
    current_savings = current_savings + monthly_savings + ((current_savings*r)/12)
    #print(current_savings)
    months_to_save += 1
    #print(months_to_save)

print("That house will take ",months_to_save, "months to save for the down payment")





