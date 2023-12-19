# sales = [50000,54522,95000,15000,245000,78563,14000,91052]
# saleMax = max(sales)
# saleMin = min(sales)
# print("Sales: ",sales)
# print("Max: ",saleMax)
# print("Min: ",saleMin)
# print("Type List: ",type(sales))
# print("Len Sales: ", len(sales))
#
# strData = "Python"
# lenData = len(strData)
# print("Len Data: ",lenData)

# def sum_sale(allSale):
#     total = 0.00
#     for sale in allSale:
#         total += sale
#     return total
#
# sales = [50000,54522,95000,15000,245000,78563,14000,91052]
# totalSale = sum_sale(sales)
# print("Total Sale: ",totalSale)

# def cal_water_payment(used):
#     payment = 0.00
#     if used <= 100:
#         payment = used * 5
#     elif used <= 200:
#         payment = 500 + ((used - 100) * 7)
#     elif used <= 300:
#         payment = 1200 + ((used - 200) * 10)
#     else:
#         payment = 2200 + ((used - 300) * 13)
#
#     if payment <100 :
#         payment = 0.00
#
#     return payment
#
# before = int(input("Pls enter last month meter: "))
# after = int(input("Pls enter this month meter: "))
# used = after - before
# myPayment = cal_water_payment(used)
# print("Before: {} | Afer: {} | Used: {} | Payment: {}".format(before,after,used,myPayment))

# email = input("enter your email: ")
# cAt = email.count("@")
# cDot = email.count(".")
# if cAt == 1 and (cDot >= 1 and cDot <=3):
#     correct = True
# else:
#     correct = False
#
# if correct == True:
#     print("Good Email")
# else:
#     print("Wrong Email!")

# sales = {"andy":50000,"adam":54522,"marry":95000,"bob":15000,"john":245000,"adda":78563,"lady":14000,"candry":91052}
# print(sales)
# for sale in sales:
#     print("Sale Repersentative: {:<20s} => {:>15,.2f}".format(sale,sales[sale]))

# con = "y"
# while con == "y":
#     print("Hi")
#     con = input("Do You Want To Continue[Y/N]: ").lower()
# #    con = con.lower()

# lastID = "Cus6500005"
# last = lastID[-5:]
# print(last)
# last = str(int(last) + 1)
# print(last)
# last = last.zfill(5)
# print(last)
# newID = "Cus65" + last
# print(newID)

subject65 = ["DBAC","DBMS","MOBILE","SA&D","UX/UI"]
subject66 = subject65.copy()
print(subject65)
print(subject66)
subject66.pop(0)
print(subject66)
subject66.append("IOT")
print(subject66)