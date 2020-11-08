class Customers:



    def getCustomerName(self):
        return self.__customerName

    def getCustomerAddres(self):
        return self.__customerAddres

    def getCustomerPhone(self):
        return self.__customerPhone

    def getCustomerContactPerson(self):
        return self.__customerContactPerson

    def __init__(self, customerName, customerAddres, customerPhone, customerContactPerson):
        self.__customerName = customerName
        self.__customerAddres = customerAddres
        self.__customerPhone = customerPhone
        self.__customerContactPerson = customerContactPerson

    def setCustomerName(self, customerName):
        self.__customerName = customerName

    def setCustomerAddres(self, customerAddres):
        self.__customerAddres = customerAddres

    def setCustomerPhone(self, customerPhone):
        self.__customerPhone = customerPhone

    def setCustomerContactPerson(self, customerContactPerson):
        self.__customerContactPerson = customerContactPerson


    def __str__(self):
        return "Name: {}  Adress: {}  Phone: {}  ContactPerson: {}".format(self.__customerName, self.__customerAddres, self.__customerPhone, self.__customerContactPerson)
