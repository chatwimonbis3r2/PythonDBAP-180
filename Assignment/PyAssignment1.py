#Assignment 1
#2.1
employee = "Chatwimon Wangsabay"
status = "It Support"
department = "IT"

#2.2
strSalary = input("Your Salary: ")
strAllowance = input("Your Allowance: ")
salary = float(strSalary)
allowance = float(strAllowance)

#2.3
bonus = salary * 3

#2.4
incomes = (salary + allowance) * 12 + bonus

#2.5
strRate = input("Your Rate: ")
rate = int(strRate)

#2.6
tax = incomes * rate / 100

#2.7
print("====================")
print("Name: ", employee)
print("Status: ", status)
print("Department: ", department)
print("Salary: ", salary)
print("Allowance: ", allowance)
print("Bonus: ", bonus)
print("Incomes: ", incomes)
print("Rate: ", rate)
print("Tax: ", tax)
print("====================")