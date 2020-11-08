from Customers import Customers
from Goods import Goods
from Positions import Positions

class Orders:



   

    def getOrderCustomer(self):
        return self.__orderCustomer

    def getOrderGood(self):
        return self.__orderGood

    def getOrderDate(self):
        return self.__orderDate

    def __init__(self, orderCustomer, orderGood, orderDate):
        self.__orderCustomer = orderCustomer
        self.__orderGood = orderGood
        self.__orderDate = orderDate



    def setOrderCustomer(self, orderCustomer):
        self.__orderCustomer = orderCustomer

    def setOrderGood(self, orderGood):
        self.__orderGood = orderGood

    def setOrderDate(self, orderDate):
        self.__orderDate = orderDate


    def __str__(self):
        return "{} | {} | {} ".format(self.__orderCustomer, self.__orderGood, self.__orderDate)
