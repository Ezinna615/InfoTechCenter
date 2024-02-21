print("*************************************************")
print("Gasoline Branch\n\n")

#Import Libraries here
import random
from time import sleep

#Function that lsits gas levels, randomly choosing one and returning its value
def gasLevelGauge():
    gasLevelList = ["Empty","Low","Quarter Tank","Half Tank","Three Quarter Tank","Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Function that lists gas stations, m randomly choosing one and returning its value
def ListOfGasStations():
    gasStations = ["Shell","Speedway","Marathon","Circle K","Costco","7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby


#Function will call the gasLevelGauge to determine our gas level and then find a close gas sation
#by calling the ListOFGasStations function if we are on Low or Quarter Tank
def gaslevelAlert():
    milesToGasStationsLow = round(random.uniform(1, 25),1)
    milesToGasStationsQuarterTank = round(random.uniform(25, 50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***\n")
        sleep(2.5)
        print ("     ***Calling Triple AAA***")
    elif gasLevelIndicator == "Low":
        print("Your gas tank is extremely low, checking google mpas for the closest gas station ")
        sleep(2.5)
        print("The closest gas station is",ListOfGasStations(),"which is",milesToGasStationsLow,"miles away.")
    elif gasLevelIndicator == "Quarter Tank":
        print("Your gas tank is on a quarter tank, checking google mpas for the closest gas station... ")
        sleep(2.5)
        print("The closest gas station is",ListOfGasStations(),"which is",milesToGasStationsQuarterTank,"miles away.")
    elif gasLevelIndicator == "Half Tank":
        print("Your gas tank is a half of tank full, which is plenty to get to your destination ")
    elif gasLevelIndicator == "Three Quarter Tank":
        print("Your gas tank is at a three quarter tank ")
    else:
        print("your gas tank is full and you do not need gas")





gaslevelAlert()

