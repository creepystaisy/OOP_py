from Customers import Customers
from Goods import Goods

class Positions:



    def getPositionGood(self):
        return self.__positionGood

    def getPositionAmount(self):
        return self.__positionAmount

    def getPositionPrice(self):
        return self.__positionPrice

    def __init__(self, positionGood, positionAmount):
        self.__positionGood = positionGood
        self.__positionAmount = positionAmount
        self.__positionPrice = self.sPositionPrice(self.getPositionGood().getGoodPrice(), self.getPositionAmount())

    def setPositionGood(self, positionGood):
        self.__positionGood = positionGood

    def setPositionAmount(self, positionAmount):
        self.__positionAmount = goodPrice

    def sPositionPrice(self, positionPrice, positionAmount):
        price = 0;
        price=positionAmount * positionPrice;
        return price;

    def setPositionPrice(self, positionPrice):
        self.__positionPrice = price;



    def __str__(self):
        return " {} * {}  =  {}".format(self.__positionGood, self.__positionAmount, self.__positionPrice)

