import MySQLdb
# import dbConf
#
# myCon = MySQLdb.connect(dbConf.host, dbConf.user,
# dbConf.password, dbConf.dbname)

from dbClass import DbConf
objDb = DbConf()
myCon = MySQLdb.connect(objDb.getHost(), objDb.getUser(),objDb.getPassword(), objDb.getDbName())

# print("Connection opened....")
# ประมวลผลต่างๆ ในฐานข้อมูล
myCursor = myCon.cursor()
strSQL = "select * from division"
myCursor.execute(strSQL)
result = myCursor.fetchall()
print("*" * 100)
print("{:10s} {:30s} {:30s}".format("Division ID", "Division Name", "Desc"))
print("*" * 100)
for row in result:
    print("{:10s} {:30s} {:30s}".format(row[0], row[1], row[2]))

#1
print("*" * 100)
strSQL = "select division.divID, divName, fname, lname from division, employee where division.divID = employee.divID"
myCursor.execute(strSQL)
result = myCursor.fetchall()
for row in result:
    print(row)

#2
print("*" * 100)
strSQL = "select division.divID, divName, fname, lname " \
         "from division, employee " \
         "where division.divID = employee.divID and division.divID = %s "
tpCriteria = ("d01", )

myCursor.execute(strSQL,tpCriteria)
result = myCursor.fetchall()
for row in result:
    print(row)
myCursor.close()
myCon.close()
# print("Connection closed....")