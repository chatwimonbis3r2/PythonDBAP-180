# #Sample 2
# print("--------------------")
# names = ["Apple","Banana","Cherry","Downy","Freshy"]
# myFriend = "Cherry"
# if myFriend in names:
#    print("in name list")
# else:
#    print("not in name list")
#
# print("--------------------")
# sale = float(input("enter your sale: "))
# if sale < 50000:
#    bonus = 100
# elif sale < 100000:
#    bonus = sale * 0.10
# elif sale < 500000:
#    bonus = sale * 0.20
# else:
#    bonus = sale * 0.30
# print("Sale: ",sale," , Bonus: ",bonus)
#
# print("--------------------")
# time = 0
# while time < 10:
#    print("Good morning")
#    print("Welcome to RMUTI. KKC.")
#    time = time + 1
#    print(time)
# year = 2556
# semester = 2
# print("Year: ", year)
# print("Semester: ", semester)

print("--------------------")
cont = "y"
while cont == "y":
    correct = False
    while correct == False:
        saveScore = input("savaScore: ")
        if saveScore.isnumeric():
            saveScore = int(saveScore)
            correct = True
        correct = False
        while correct == False:
            midterScore = input("midterScore: ")
            if midterScore.isnumeric():
                midterScore = int(midterScore)
                correct = True
        correct = False
        while correct == False:
            finalScore = input("finalScore: ")
            if finalScore.isnumeric():
                finalScore = int(finalScore)
                correct = True
        totalScore = saveScore + midterScore + finalScore
        if totalScore < 50:
            grade = "U"
        else:
            grade = "S"
        print("Save: ",saveScore, "Mid: ",midterScore, "Final: ",finalScore)
        print(totalScore, grade)
        cont = input("Add More?[Y/N]")

# print("--------------------")
# num = [5,50,53,45,8,4,95,78,54]
# for i in num:
#     print("Num: ",i)
#
# print("--------------------")
# names = ["Apple","Banana","Cherry","Downy","Freshy"]
# for name in names:
#     print("Name: ",name)
#
# print("--------------------")
# for i in range(10,100,5):
#     print("I is:",i)
#
# print("--------------------")
# menus = {"Mama":10,"Sticky Rice":20,"Fired Rice With Egg":50,"Sushi":80}
# for key in menus.keys():
#     print("Name: {} Is Price: {}".format(key,menus[key]))
#
# print("--------------------")
# for value in menus.values():
#     print("Value: ",value)
#
# print("--------------------")
# for item in menus.items():
#     print("Item: ",item)