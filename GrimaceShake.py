print("\n****************************************\n")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

#Create a function randomly chooses the weather from list
def weather():
    weatherForecast = ["Snowy", "Blizzard", "Rainy", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherForecast)
    return weatherConditions

#Variable to call the weather() once VRS(Vehicle Response System) is determined)
weatherAlert = weather()

def vehicleResponseSystem():
    if weatherAlert == "Snowy":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the forecast of",weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS nas been engaged only allowing you to drive 50mph")
    elif weatherAlert == "Blizzard":
         print("\nNational Weather Service has updated our alarm by 45 minutes because of the forecast of",weatherAlert,
               "weather conditions.")
         sleep(1.5)
         print("VRS nas been engaged only allowing you to drive 40mph")
    elif weatherAlert == "Rainy":
         print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of",weatherAlert,
               "weather conditions.")
         sleep(1.5)
         print("VRS nas been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS nas been engaged only allowing you to drive 60mph")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS nas been engaged only allowing you to drive 70mph")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service has updated our alarm by 60 minutes because of the forecast of", weatherAlert,
              "weather conditions.")
        sleep(1.5)
        print("VRS nas been engaged only allowing you to drive 30mph")
    else:
        print("\nNationalWeather Service Forecast", weatherAlert,"weather conditions.")
        sleep(1.5)
        print("VRS has been disengaged! Drive at your own risk.")

        
vehicleResponseSystem()