import libtcodpy as libtcod
from constants import *

currentMinutes = 0
currentHours = 6
currentM = "A.M."

def getTimeString():
   global currentMinutes
   global currentHours
   if(currentMinutes < 10):
      currentMinutesString = "0" + str(int(currentMinutes))
   else:
      currentMinutesString = str(int(currentMinutes))
      
   return str(currentHours) + ":" + str(currentMinutesString) + currentM


def updateTime():
   global currentMinutes
   global currentHours
   global currentM
   currentMinutes += TIME_UPDATE_INCREMENT

   if(currentMinutes >= 60):
      currentHours += 1
      currentMinutes = 0

   if(currentHours >= 12):
      currentHours = 1
      currentM = "P.M"
      

def timeRunOut():
   return(currentHours >= 6 and currentM == "P.M")

def getTimeColour():
   return libtcod.Color(0, 0, 0)
