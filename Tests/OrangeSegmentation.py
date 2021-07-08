import pytest
import pytest_html
from pyth import *

def getAllBowlOrange():
    #Arrange
    bowlList=['Apple','Orange','Mango']
    apple = fruitBowl(bowlList)

    fruitList=apple.addFruits("Apple")
    print(fruitList)

    fruitRemove = apple.removeFruits("Mango")
    print(fruitRemove)

    #Act

    orange = fruitBowl(bowlList)
    orangeBowl=orange.allOrangeFruits()
    print(orangeBowl)

    apple1 = Apple("sweet", 'red')
    segmentByTasteColor = apple1.appleType('Kashmiri', bowlList)
    print("Banana Bowl having" + " " + str(segmentByTasteColor) + " " + "Apple")

    #Assert

    #Assert
    assert orangeBowl == 1   #should have same len of apple given in list
    assert segmentByTasteColor ==1  #should have same length of apple given by taste and colour


getAllBowlOrange()