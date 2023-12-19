def fCalTax(memberStatus, total):
    discount = 0.00
    if memberStatus == 1:
        if total <= 1000:
            discount = 0.00
        elif total <= 5000:
            discount = total * 0.05
        elif total <= 10000:
            discount = total * 0.10
        else:
            discount = total * 0.10
    return discount

def fCalScore(memberStatus, total):
    score=0
    if memberStatus != 0:
        if total <= 500:
            score = 0
        elif total <= 1000:
            score = 5
        elif total <= 5000:
            score = 10
        else:
            score = 15
    return score

print("*** Welcome To User-Define Function Program ** ")
memberType = int(input("Enter Member Status[0=None/1=Member]: "))
price = float(input("Enter Product Price: "))
amount = int(input("Enter Product Amount: "))
myScore = int(input("Enter Your Score: "))
total = price * amount
myDiscount = fCalTax(memberType, total)
myScore = myScore + fCalScore(memberType, total)

if memberType==0:
    strMemberType="None Member"
else:
    strMemberType="Member"

print("*************** Result **************** ")
print("Member type: "+strMemberType)
print("{0:20s} {1:15,.2f} ".format("Product Price: ",price))
print("{0:20s} {1:15,.2f} ".format("Product Amount: ",amount))
print("{0:20s} {1:15,.2f} ".format("Total: ", total))
print("{0:20s} {1:15,.2f} ".format("Discount: ",myDiscount))
print("{0:20s} {1:15,.2f} ".format("Your Score Point: ",myScore))
print("*************** Good bye **************** ")