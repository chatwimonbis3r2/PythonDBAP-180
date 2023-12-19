import MySQLdb
from dbConf import DBDesc
myDb = DBDesc()
myConn = MySQLdb.connect(host=myDb.getHost(), user=myDb.getUser(),
                         password=myDb.getPassword(), database=myDb.getDatabase())
myCursor = myConn.cursor()

def load():
    import csv
    with open('StationList.csv', 'r') as myFile:
        reader = csv.reader(myFile)
        print("=" * 100)
        print("{:10s} {:20s} {:10s} {:15s} {:30s} {:30s}"
              .format("ID", "LineCode", "Status", "StationCode", "StationNameEN", "StationNameTH"))
        print("-" * 100)
        header = True
        for row in reader:
            if header == True:
                header = False
            else:
                ID = row[0]
                LineCode = row[1]
                Status = row[2]
                StationCode = row[3]
                StationNameEN = row[4]
                print("{:10s} {:20s} {:10s} {:15s} {:30s}"
                      .format(ID, LineCode, Status, StationCode, StationNameEN))
                strsql = "insert into stationList(ID, LineCode, Status, StationCode, StationNameEN) " \
                         "values (%s, %s, %s, %s, %s)"
                value = (ID, LineCode, Status, StationCode, StationNameEN)
                myCursor.execute(strsql, value)
                myConn.commit()
        print("-" * 100)
        print(">>Successfully read data in file and added the data to the table!!")

def display():
    strsql = "SELECT * FROM classicmodels.stationlist"
    myCursor.execute(strsql)
    result = myCursor.fetchall()
    print("=" * 100)
    print("{:10s} {:20s} {:10s} {:15s} {:30s}"
          .format("ID", "LineCode", "Status", "StationCode", "StationNameEN"))
    print("-" * 100)
    for row in result:
        print("{:10s} {:20s} {:10s} {:15s} {:30s}"
              .format(row[0], row[1], row[2], row[3], row[4]))
    print("-" * 100)
    print(">>Successfully read the data in the table!!")

def clear():
    print("-" * 100)
    print(">>Successfully deleted table data!!")
    strsql = "DELETE FROM classicmodels.stationlist"
    myCursor.execute(strsql)
    myConn.commit()

menu = "L","D","C"
while menu != "E":
    print("-" * 100)
    print("L: Load")
    print("D: Display")
    print("C: Clear")
    print("E: Exit")
    menu = input("Your Enter: ")
    menu.upper()

    if menu == "L":
        load()
    elif menu == "D":
        display()
    elif menu == "C":
        clear()
    else:
        print("Exit")