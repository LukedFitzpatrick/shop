from graphic import *
from constants import *
from actor import *
from object import *
from ai import *
import libtcodpy as libtcod
import random

def generateMerchant():
   merchantGraphic = Graphic('M', "Merchant", getRandomColour())
   merchantActor = Actor()
   merchantAI = AI()
   startX = random.choice([0, SCREEN_WIDTH-1])
   startY = random.randrange(0, GAME_HEIGHT-1)
   merchantObject = Object(startX, startY, True, graphic=merchantGraphic, 
      actor=merchantActor, item=None, ai=merchantAI)
   return merchantObject

