import pytest
import pytest_html
from pyth import *

def getAllBowlBanana():
    #Arrange
    bowlList=['Apple','Orange','Mango']
    banana = fruitBowl(bowlList)

    fruitList=banana.addFruits("Apple")
    print(fruitList)

    fruitRemove = banana.removeFruits("Mango")
    print(fruitRemove)
    #Act

    banana = fruitBowl(bowlList)
    bananaBowl=banana.allBananaFruits()
    print(bananaBowl)

    #Assert

getAllBowlBanana()