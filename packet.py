"""
Packet

Description:
"""
import random

class Sanitizer:
    
    def __init__(self, productName, productID, listName):
        
        self.productName = productName
        self.productID = productID
        self.listName = listName.append(productName + "(" + productID + ")")

class Choice:
    
    def __init__(self, Products, message, debugTools):
        
        self.Products = len(Products)
        num = random.randint(0, self.Products)
        
        if debugTools:
            
            print(str(self.Products) + " : Length")
            print(str(num) + " : Guess")
            
            print()
            print(Products)
            print()
        
        if Products > self.Products:
            
            print(message + Products[num - 1])
