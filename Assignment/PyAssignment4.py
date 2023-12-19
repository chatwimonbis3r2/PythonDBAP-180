#Assignment 4
#3
studyList = []
gradeDic = {}
#4
stdID = input("Student Id: ")
stdName = input("Student Name: ")
#4.1
cont = "Y"
while cont == "Y" or cont == "y":
    #4.1.1
    sbjID = input("Subject ID: ")
    sbjName = input("Subject Name: ")
    credit = int(input("Credit: "))
    strGrade = input("Grade: ")
    #4.1.2
    studyData = [sbjID,sbjName,credit,strGrade]
    studyList.append(studyData)
    #4.1.3
    cont = input("Add More?[Y/N]: ")
#4.2
print("studyList: ",studyList)
#4.3
i = 0
numGrade = 0.0
#4.3.1
for data in studyList:
    if data[3] == "A":
        numGrade = 4
    elif data[3] == "B+":
        numGrade = 3.5
    elif data[3] == "B":
        numGrade = 3
    elif data[3] == "C+":
        numGrade = 2.5
    elif data[3] == "C":
        numGrade = 2
    elif data[3] == "D+":
        numGrade = 1.5
    elif data[3] == "D":
        numGrade = 1
    else:
        numGrade = 0
    #4.3.2
    GP = data[2] * numGrade
    # 4.3.3
    studyList[i] = [data[0],data[1],data[2],data[3],numGrade,GP]
    #4.3.4
    gradeKey = data[0]
    gradeVal = data[3]
    gradeDic[gradeKey] = gradeVal
    i = i + 1
#4.4
CGX = 0.0
CCX = 0.0
for data in studyList:
    CGX += data[5]
    CCX += data[2]
#4.5
GPA = CGX/CCX
#4.6
print("studyList: ",studyList)
#4.7
print("gradeDic: ",gradeDic)
#4.8
print(CGX)
print(CCX)
print(GPA)