import pytest
import pytest_html
from pyth import *

def getAllBowlOrange():
    #Arrange
    bowlList=['Apple','Orange','Mango']
    apple = fruitBowl(bowlList)

    fruitList=apple.addFruits("Apple")


    fruitRemove = apple.removeFruits("Mango")

    #Act

    orange = fruitBowl(bowlList)
    orangeBowl=orange.allOrangeFruits()
    print("Orange Bowl having" + " " + str(orangeBowl) + " " + "Orange")

    orangebyTaste = Orange('sore','orange')
    segmentByTasteColor = orangebyTaste.orangeQuantity('Kg', bowlList)
    print("Orange Bowl having" + " " + str(segmentByTasteColor) + " " + "Orange")

    #Assert

    #Assert
    assert orangeBowl == 1   #should have same len of ORange given in list
    assert segmentByTasteColor ==1  #should have same length of ORange given by taste and colour


