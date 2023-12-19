#Practice 1
university = "Rajamangala University of Technology Isan"
campus = "Khonkean"
major = "Digital Business Technolgy"

print("====================")
print("Good afternoon")
print("====================")
name = input("What your name?: ")
surname = input("What your surname?: ")
age = input("How old are you?: ")
StrQuantity = input("Hom many you buy?: ")
quantity = float(StrQuantity)
fullName = name + " " + surname
total = quantity * 550.00

print("*********************")
print("Hello: ", fullName)
print("Your are: ", age, " Years Old")
print("Welcome to: ", university)
print("Campus: ", campus)
print("This is major: ", major)
print("Your total: ", total)
print("Good Bye.")
print("*********************")