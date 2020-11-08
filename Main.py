from Customers import Customers
from Goods import Goods
from Positions import Positions
from Orders import Orders


nornickel = Customers("OOO Nornickel", "Moskow, Pushkina street, Kolotushkina buildings", "+70000000000", "Ivan Ivanovich")

boots = Goods("boots", 12, "true", "very good boots")
t_shirt = Goods("tshirt", 30, "true", "ordinary tshirt")

pos1 = Positions(boots, 2)
pos2 = Positions(t_shirt, 10)

print(nornickel)

print(boots)

arr = [pos1, pos2]

or1 = Orders (nornickel, arr, "25/10/2020")
print(or1)
