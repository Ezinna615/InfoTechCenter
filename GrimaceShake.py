print("*************************************************")
print("Gasoline Branch\n\n")

#Import Libraries here
import random

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



print(gasLevelGauge())
print(ListOfGasStations())
