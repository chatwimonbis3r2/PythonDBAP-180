#Challenge 1
print("==========Challenge1==========")
myFriends = ["นัท","ริว","เปรม","อ้อ","อาท","กี้","ภูมิ","แหวน","ตอง","แนน"]
print(myFriends)
print(myFriends[0])
print(myFriends[9])
myFriends.append("จิ๋ว")
myFriends.append("พีช")
print(myFriends)
print(myFriends[6:10])

#Challenge 2
print("==========Challenge2==========")
boyFriends = ("Jin","Zoro","Sanji","Law","Koby")
print(boyFriends)
print(boyFriends[0])
print(boyFriends[4])
print(boyFriends[-1])

#Challenge 3
print("==========Challenge3==========")
salaries = {"Whann":15000,"Koby":13000,"Ace":12000,"JayJay":26000,"Bob":24000}
print(salaries)
print(salaries.get("JayJay"))
print(salaries.get("Bob"))
salaries.update({"Bob":30000})
print(salaries.get("Bob"))
salaries.update({"Bob":salaries["Bob"]+(salaries["Bob"]*0.10)})
print(salaries.get("Bob"))

#Challenge 4
print("==========Challenge4==========")
setLiverpool = {"Jin","Zoro","Sanji","Law","Koby","Caesar","Ace","JayJay","Bob","Kid"}
print(setLiverpool)
setManU = {"Bob","Kid","Prem","Aor","Art","Ky","Poom","Whean","Tong","Nan"}
print(setManU)
setAllFanclub = setLiverpool.union(setManU)
print(setAllFanclub)
setNameLike = setLiverpool.intersection(setManU)
print(setNameLike)
