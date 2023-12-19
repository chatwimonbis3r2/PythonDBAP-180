def fCalAllowance(work):
    if work == "CEO":
        allowance = 20000.00
    elif work == "Manager":
        allowance = 10000.00
    elif work == "Supervisor":
        allowance = 5000.00
    else:
        allowance = 0.00
    return allowance

def fCalBonus(work,salary,year):
    if work == "CEO" or work == "Manager" or work == "Supervisor":
        if year <5:
            bonus = 2 * salary
        elif year >=5 and year <=10:
            bonus = 3 * salary
        else:
            bonus = 5 * salary
    else:
        if year <3 :
            bonus = salary
        elif year >=3 and year <=5:
            bonus = 2 * salary
        elif year >= 6 and year <= 10:
            bonus = 3 * salary
        else:
            bonus = 4 * salary
    return bonus

empID = input("Your ID: ")
empName = input("Your Name: ")
work = input("Your Work: ")
salary = float(input("Your Salary: "))
year = int(input("Your Year: "))
myAllowance = fCalAllowance(work)
myBonus = fCalBonus(work,salary,year)
total = salary + myAllowance + myBonus

print("*************** Result ****************")
print("Employee ID: ",empID)
print("Employee Name: ",empName)
print("---------------------------------------")
print("Work: ",work)
print("Allowance: ",myAllowance)
print("Salary: ",salary)
print("Year: ",year)
print("Bonus: ",myBonus)
print("Total: ",total)