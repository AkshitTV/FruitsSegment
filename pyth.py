import pytest


class fruitBowl:
    def __init__(self,allFruits):
        self.allfruits = allFruits

    def addFruits(self,fruit):
        self.allfruits.append(fruit)
        return(self.allfruits)

    def removeFruits(self,fruit):
        self.allfruits.remove(fruit)
        return(self.allfruits)

    def bowlSize(self):
        pass

    def bowlMaxLimit(self,size):
        pass

    def allAppleFruits(self):
        for fruitIndex in self.allfruits:
            if fruitIndex == "Apple":
                return(self.allfruits.count("Apple"))

    def allOrangeFruits(self):
        for fruitIndex in self.allfruits:
            if fruitIndex == "Orange":
                return(self.allfruits.count("Orange"))

    def allBananaFruits(self):
        for fruitIndex in self.allfruits:
            if fruitIndex == "Banana":
                return (self.allfruits.count("Banana"))


class fruit:
    def __init__(self,taste,colour):
        self.taste=taste
        self.colour=colour

class Apple(fruit):
    def appleType(self,type,fruits):
        self.type = type

        if self.taste == "sweet" or self.colour == "Red":
            for fruitIndex in fruits:
                if fruitIndex == "Apple":
                    return (fruits.count("Apple"))



    def appleQuantity(self,quantity):
        self.quantity=quantity


class banana(fruit):

    def bnanaQuantity(self,quantity,fruits):
        self.quantity = quantity

        if self.taste=="soft" or self.colour == "Yellow":
            for fruitIndex in fruits:
                if fruitIndex == "Banana":
                    return ("Banana Bowl having" + " " + str(fruits.count("Banana")) + " " + "Banana")


class Orange(fruit):
    def orangeQuantity(self,quantity,fruits):
        self.quantity=quantity


        if self.taste=="sore":
            for fruitIndex in fruits:
                if fruitIndex == "Orange" or self.colour == "Orange":
                    return (fruits.count("Orange"))






