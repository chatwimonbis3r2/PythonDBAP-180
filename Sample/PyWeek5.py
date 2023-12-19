from Product import Product

prod1 = Product("P001","Computer PC","Acer",35000.00,5) #สร้างออบเจ็กต์
print("ID: ",prod1.id) #การเข้าถึงแอททริบิวท์ของออบเจ็กต์
print("Name: ",prod1.name)
print("Brand: ",prod1.brand)
print("Price: ",prod1.price)
print("Quantity: ",prod1.quantity)

# print("Total: ",prod1.getTotal())
# print("Discount: ",prod1.getDiscount())
# print("Net: ",prod1.getNet())
#
# print(prod1)
# print("Product Quantity: ", len(prod1))
#
# del prod1