#Assignment 2
#2.1
cusID = "65342310180-5"
cusName = "Chatwimon Wangsabay"

#2.2
strPrice = input("Your Price: ")
price = float(strPrice)
strQuantity = input("Your Quantity: ")
quantity = int(strQuantity)
amount = price * quantity
discount = amount * 0.10
net = amount - discount

#2.3
myFavoriteSong = ["ลาก่อน - yourmood","you - blackbeans","me - blackbeans","รสหวาน - freehand","คุก - freehand"]

#2.4
menus = {"ข้าวผัด":"35","ผัดไท":"40","ก๋วยเตี๋ยวเนื้อ":"45","ข้าวผัดกุ้ง":"50","ยำแซลมอล":"60"}

#2.5
print("Cus ID: ", cusID)
print("Cus Name: ", cusName)
print("Price: ", price)
print("Quantity: ", quantity)
print("Amount: ", amount)
print("Discount: ", discount)
print("Net: ", net)
print("Favorite Song:", myFavoriteSong)
print("Menus: ", menus)

#2.6
print("Favorite Song List 3:", myFavoriteSong[3])

#2.7
print("Menus 2 - 4: ", menus.get("ผัดไท"),menus.get("ก๋วยเตี๋ยวเนื้อ"),menus.get("ข้าวผัดกุ้ง"))

#2.8
myFavoriteSong.append("orange - treasure")
menus.update({'ตำกุ้งสด':'50'})

#2.9
print(myFavoriteSong)
print(menus)