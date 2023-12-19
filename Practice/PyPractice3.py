#Practice 3
import datetime
print("************************************")
print("Welcome to my practice condition program")
print("************************************")

name = input("Your Name: ")
yearBirth = int(input("Year Birth: "))
gender = int(input("Your Gender [0=Male/1=Female]: "))
job = int(input("Have a Job [0=Yes/1=No]: "))
salary = 0.00

if job == 0:
    salary = int(input("Your Salary: "))

currentYear= datetime.datetime.today().year
age = (currentYear + 543) - yearBirth

if gender == 0:
    strGender = "Male"
else:
    strGender = "Female"

if job == 0:
    strJob = "Yes"
else:
    strJob = "No"

livingAllowance=0.00

if age >= 60:
    livingAllowance = 600 + ((age - 60) * 100)

tax=0.00

if job == 0:
    incomes = salary * 12
    net = incomes - 30000
    if net <= 300000:
        tax = 0.00
    elif net <= 500000:
        tax = (net - 300000) * 0.03
    else:
        tax = 60000 + ((net - 500000) * 0.05)

print("***************** Result ****************")
print("Name: ", name)
print("Year Birth: ", yearBirth)
print("Age: ", age)
print("Gender: ", strGender)
print("Job: ", strJob)

if age >= 60:
    print("{0:<50s}{1:>1,.2f} THB".format(("Living Allowance: ", livingAllowance)))

if job == 0:
    print("{0:<50s}{1:>10,.2f} บาท".format("Salary: ", salary))
    print("{0:<50s}{1:>10,.2f} บาท".format("Incomes: ", incomes))
    print("{0:<50s}{1:>10,.2f} บาท".format("Net: ", net))
    print("{0:<50s}{1:>10,.2f} บาท".format("Tax: ", tax))
    print("***************** Good bye ****************")