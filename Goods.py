class Goods:



    def getGoodName(self):
        return self.__goodName

    def getGoodPrice(self):
        return self.__goodPrice

    def getGoodDelivery(self):
        return self.__goodDelivery

    def getGoodDescription(self):
        return self.__goodDescription

    def __init__(self, goodName, goodPrice, goodDelivery, goodDescription):
        self.__goodName = goodName
        self.__goodPrice = goodPrice
        self.__goodDelivery = goodDelivery
        self.__goodDescription = goodDescription

    def setGoodName(self, goodName):
        self.__goodName = goodName

    def setGoodPrice(self, goodPrice):
        self.__goodPrice = goodPrice

    def setGoodDelivery(self, goodDelivery):
        self.__goodDelivery = goodDelivery

    def setGoodDescription(self, goodDescription):
        self.__goodDescription = goodDescription


    def __str__(self):
        return "name: {}  price: {}  delivery: {}  Description: {}".format(self.__goodName, self.__goodPrice, self.__goodDelivery, self.__goodDescription)

