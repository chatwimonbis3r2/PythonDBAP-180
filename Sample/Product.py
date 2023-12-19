class Product:
    def __init__(self,id,name,brand,price,quantity):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.__total = 0.00
        self.__discount = 0.00
        self.__net = 0.00
        self.__setTotal()
        self.__setDiscount()
        self.__setNet()

    def __str__(self):
        return "Product ID: {} Name: {} Brand: {} Price: {}".\
            format(self.id,self.name,self.brand,self.price)

    def __len__(self):
        return self.quantity

    # def __del__(self):
    #     print(">Product Object Deleted.....<")

    def __setTotal(self):
        self.__total = self.price * self.quantity

    def __setDiscount(self):
        if self.__total < 5000.00:
            self.__discount = 0.00
        elif self.__total < 10000.00:
            self.__discount = self.__total * 0.10
        elif self.__total < 30000.00:
            self.__discount = self.__total * 0.15
        else:
            self.__discount = self.__total * 0.20

    def __setNet(self):
        self.__net = self.__total - self.__discount

    def getTotal(self):
        return self.__total

    def getDiscount(self):
        return self.__discount

    def getNet(self):
        return self.__net