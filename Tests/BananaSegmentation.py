import pytest
import pytest_html
from pyth import *

def getAllBowlBanana():
    #Arrange
    bowlList=['Apple','Orange','Mango','Banana']
    bananaobj = fruitBowl(bowlList)

    fruitList=bananaobj.addFruits("Apple")

    fruitRemove = bananaobj.removeFruits("Mango")

    #Act

    bananaObj = fruitBowl(bowlList)
    bananaBowl=bananaObj.allBananaFruits()
    print("banana Bowl having" + " " + str(bananaBowl) + " " + "Banana")

    bananaByTaste = banana('soft','Yellow')
    segmentByTasteColor = bananaByTaste.bnanaQuantity('Kg', bowlList)
    print("banana Bowl having" + " " + str(segmentByTasteColor) + " " + "Banana")


    #Assert

    assert bananaBowl == 1   #should have same len of banana given in list
    assert segmentByTasteColor ==1  #should have same length of banana given by taste and colour


