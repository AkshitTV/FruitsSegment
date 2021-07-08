import pytest
import pytest_html
from pyth import *

def getAllBowlApples():
    #Arrange
    bowlList=['Apple','Orange','Mango']

    apple = fruitBowl(bowlList)

    fruitList=apple.addFruits("Apple")

    fruitRemove = apple.removeFruits("Apple")

    #Act

    apple = fruitBowl(bowlList)
    appleBowl=apple.allAppleFruits()
    print("Apple Bowl having" + " " + str(appleBowl) + " " + "Apple")


    apple1 = Apple("sweet", 'red')
    segmentByTasteColor = apple1.appleType('Kashmiri', bowlList)
    print("Apple Bowl having" + " " + str(segmentByTasteColor) + " " + "Apple")

    #Assert
    assert appleBowl == 1   #should have same len of apple given in list
    assert segmentByTasteColor ==1  #should have same length of apple given by taste and colour




