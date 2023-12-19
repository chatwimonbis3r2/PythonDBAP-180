import MySQLdb
from dbConf import DBDesc

myDb = DBDesc()
myConn = MySQLdb.connect(host=myDb.getHost(),
                         user=myDb.getUser(),
                         password=myDb.getPassword(),
                         database=myDb.getDatabase())

mySeclect = 1,2,3,4,5
myCursor = myConn.cursor()

while mySeclect != 6:
    print("*" * 100)
    print("1: Product information with selling price")
    print("2: Product information on the production line 'Trains' and 'Motorcycles'")
    print("3: Data on the specific customers who made the most purchases.")
    print("4: Product information that does not appear in the order list at all")
    print("5: Product sales by purchase order")
    print("6: Exit")
    print("-" * 100)
    mySeclect = int(input("Seclet: "))

    if mySeclect == 1:
        selectSql = "SELECT productCode,productName,productLine,productVendor,buyPrice " \
                    "FROM products " \
                    "where buyPrice > 50 and buyPrice < 90"
        print(">>1: Product information with selling price<<")
        print("{:10s} {:40s} {:20s} {:25s} {:10}".format("Code","Name","Line","Vendor","Price"))
        myCursor.execute(selectSql)
        result = myCursor.fetchall()
    elif mySeclect == 2:
        selectSql = "SELECT productCode,productName,productLine,productVendor,buyPrice " \
                    "FROM products " \
                    "where productLine Like '%Trains%' or productLine Like '%Motorcycles%'"
        print(">>2: Product information on the production line 'Trains' and 'Motorcycles'<<")
        print("{:10s} {:40s} {:20s} {:25s} {:10}".format("Code", "Name", "Line", "Vendor", "Price"))
        myCursor.execute(selectSql)
        result = myCursor.fetchall()
    elif mySeclect == 3:
        selectSql = "SELECT customers.customerNumber,customerName,orderdetails.orderNumber,quantityOrdered " \
                    "FROM classicmodels.customers, classicmodels.orders, classicmodels.orderdetails " \
                    "where orders.orderNumber = orderdetails.orderNumber and orders.customerNumber = customers.customerNumber " \
                    "ORDER BY orderdetails.quantityOrdered DESC LIMIT 1"
        print(">>3: Data on the specific customers who made the most purchases<<")
        print("{:10s} {:10s} {:10s} {:10s}".format("Number", "cusNumber", "Quantity", "Price"))
        myCursor.execute(selectSql)
        result = myCursor.fetchall()
    elif mySeclect == 4:
        selectSql = "SELECT products.productCode, productName, productVendor, buyPrice " \
                    "FROM classicmodels.products " \
                    "where NOT products.productCode IN (SELECT orderdetails.productCode FROM classicmodels.orderdetails)"
        print(">>4: Product information that does not appear in the order list at all<<")
        print("{:10s} {:10s} {:50s} {:20s} {:10s}".format("orCode", "proCode", "Name", "Line", "Price"))
        myCursor.execute(selectSql)
        result = myCursor.fetchall()
    elif mySeclect == 5:
        selectSql = "SELECT orders.orderNumber, orderDate, SUM(orderdetails.quantityOrdered), SUM(orderdetails.priceEach) " \
                    "FROM classicmodels.orders, classicmodels.orderdetails " \
                    "WHERE orders.orderNumber = orderdetails.orderNumber " \
                    "group by orders.orderNumber " \
                    "order by orders.orderNumber desc"
        print(">>5: Product sales by purchase order<<")
        print("{:10s} {:10s} {:>22s}".format("orCode", "orDate", "Quantity"))
        myCursor.execute(selectSql)
        result = myCursor.fetchall()
    else:
        print("Exit")
        result = myCursor.fetchall()

    print("*" * 100)
    for row in result:
        if mySeclect == 1:
            #productCode,productName,productLine,productVendor,buyPrice
            print("{:10s} {:40s} {:20s} {:25s} {:<10,.2f}".format(row[0], row[1], row[2], row[3], row[4]))
        elif mySeclect == 2:
            #productCode,productName,productLine,productVendor,buyPrice
            print("{:10s} {:40s} {:20s} {:25s} {:<10,.2f}".format(row[0], row[1], row[2], row[3], row[4]))
        elif mySeclect == 3:
            #orders.orderNumber, customerNumber, orderdetails.quantityOrdered, priceEach
            print("{:<10d} {:<10s} {:<10d} {:<10d}".format(row[0], row[1], row[2], row[3]))
        elif mySeclect == 4:
            #orderdetails.productCode, products.productCode, productName, productLine, buyPrice
            print("{:10s} {:10s} {:20s} {:<10,.2f}".format(row[0], row[1], row[2], row[3]))
        elif mySeclect == 5:
            #orders.orderNumber, orderDate, orderdetails.quantityOrdered
            print("{:<10.0f} {} {:>10,.2f}".format(row[0], row[1], row[2]))
        else:
            break

print("The End")
myCursor.close()