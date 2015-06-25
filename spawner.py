from graphic import *
from constants import *
from actor import *
from object import *
from ai import *
import libtcodpy as libtcod
import random

global names
names = None

def loadNames():
   global names
   with open('names.txt') as f:
      names = f.read().splitlines()
   return names

def getRandomName():
   global names
   if names:
      return random.choice(names)
   else:
      names = loadNames()
      return random.choice(names)

def getQuickItemList():
   if itemList:
      return itemList
   else:
      return getFullItemList

def generateMerchant():
   merchantGraphic = Graphic('m', getRandomName(), getRandomColour())
   merchantActor = Actor()
   merchantAI = AI(merchant=True, shopper=False)
   startX = random.choice([0, SCREEN_WIDTH-1])
   startY = random.randrange(0, GAME_HEIGHT-1)
   merchantObject = Object(startX, startY, True, graphic=merchantGraphic, 
      actor=merchantActor, item=None, ai=merchantAI)
   return merchantObject

def generateShopper():
   shopperGraphic = Graphic('s', getRandomName(), getRandomColour())
   shopperActor = Actor()
   shopperAI = AI(merchant=False, shopper=True)
   startX = random.choice([0, SCREEN_WIDTH-1])
   startY = random.randrange(0, GAME_HEIGHT-1)
   shopperObject = Object(startX, startY, True, graphic=shopperGraphic, 
      actor=shopperActor, item=None, ai=shopperAI)
   return shopperObject