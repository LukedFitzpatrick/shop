from graphic import *
from constants import *
from actor import *
from object import *
from ai import *
import libtcodpy as libtcod
import random

def generateMerchant():
   merchantGraphic = Graphic('m', "Merchant", getRandomColour())
   merchantActor = Actor()
   merchantAI = AI(merchant=True, shopper=False)
   startX = random.choice([0, SCREEN_WIDTH-1])
   startY = random.randrange(0, GAME_HEIGHT-1)
   merchantObject = Object(startX, startY, True, graphic=merchantGraphic, 
      actor=merchantActor, item=None, ai=merchantAI)
   return merchantObject

def generateShopper():
   shopperGraphic = Graphic('s', "Shopper", getRandomColour())
   shopperActor = Actor()
   shopperAI = AI(merchant=False, shopper=True)
   startX = random.choice([0, SCREEN_WIDTH-1])
   startY = random.randrange(0, GAME_HEIGHT-1)
   shopperObject = Object(startX, startY, True, graphic=shopperGraphic, 
      actor=shopperActor, item=None, ai=shopperAI)
   return shopperObject