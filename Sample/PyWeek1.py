#Sample 1
print("--------------------")
print("Hello!")

print("--------------------")
courseName = "DBAP."
year = 2022
myName = "Chatwimon Wangsabay"
myStatus = '''Student'''
myAge = 20

print("--------------------")
print("Course Name: ", courseName)
print("Course Name: "+ courseName)
print(courseName)
print(courseName, year)
print("Status: ", myStatus, "Age: ",myAge)
print("Name: {0} | Status: {1} | Age: {2}".format(myName,myStatus,myAge))

print("--------------------")
for x in range(0,-10,-1):
    print(x, ~x)

print("--------------------")
temp = 32.50
print(temp)
print(type(temp))
temp = "Hot"
print(temp)
print(type(temp))

print("--------------------")
quantity = input("Enter Number: ")
print(type(quantity))
quantity = int(quantity)
print(type(quantity))
total = quantity * 500
print(total)

sss = range(500)
print(sss)
sale = [1500,2500,600,120,300,900,15000,1200,1450]
print(sale)
sale.append(20000)
sale.append(800)
print(sale)
ttt = sale.pop()
print("ttt: ",ttt, "sale: ",sale)
sale.reverse()
print(sale)
sale.sort()
print(sale)

grade = {"32-406-083-101":"F","32-406-083-103":"D",
         "32-406-086-301":"A","32-406-086-302":"A",
         "32-406-085-202":"C","32-406-087-401":"C+",}
card = {}
menu = {}
salary = {}
