print("\n****************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function randomly chooses the weather from list
def weather():
    weatherForecast = ["Snowing,", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions


print(weather())

