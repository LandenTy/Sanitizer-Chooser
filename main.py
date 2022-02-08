"""
Main

Description:
"""
from Packet import Sanitizer
from Packet import Choice

productList = []

# Sanitizer Name, Product ID, List it's stored in.
obj1 = Sanitizer("Mahogany", "fb01b14", productList)
obj2 = Sanitizer("Tangerine", "c156f51189ff4579", productList)
obj3 = Sanitizer("Honeycomb", "1396b642c4de72", productList)
obj4 = Sanitizer("Lemon", "e5bd8341a47e", productList)
obj5 = Sanitizer("Ocean", "56d3d9f12", productList)
obj6 = Sanitizer("Vanilla Bean", "0ad53d4cf", productList)

# List to choose from, "isSelected" message, debugTools
Choice(productList, "You shall use the Sanitizer: ", False)
