import libtcodpy as libtcod
import random
from constants import *

class AI:
   def __init__(self):
      self.targetX = random.randrange(0, SCREEN_WIDTH)
      self.targetY = random.randrange(0, GAME_HEIGHT)
      self.moveCountdown = 10
      self.lifeCounter = MERCHANT_LIFE
      self.readyToDie = False
      self.targetCounter = MERCHANT_TARGET_CHANGE

   # behaviour for a merchant
   def generateKeypress(self):
      self.lifeCounter -= 1
      if self.lifeCounter <= 0:
         self.readyToDie = True

      self.targetCounter -= 1
      if self.targetCounter <= 0:
         self.targetX = random.randrange(0, SCREEN_WIDTH)
         self.targetY = random.randrange(0, GAME_HEIGHT)
         self.targetCounter = MERCHANT_TARGET_CHANGE
      
      key = libtcod.Key()
      if(self.moveCountdown > 0):
         self.moveCountdown -= 1
         key.vk = K_NOTHING
      else:
         self.moveCountdown = MERCHANT_MOVE_LAG
         key = self.keypressForTargetSquare()
      
      return key

   # generic pathfinding
   def keypressForTargetSquare(self):
      key = libtcod.Key()
      # compare distance to our target in x and y directions
      gapX = (self.parent.x - self.targetX) * (self.parent.x - self.targetX)
      gapY = (self.parent.y - self.targetY) * (self.parent.y - self.targetY)
      # further away in the x direction
      if(gapX > gapY):
         if(self.targetX > self.parent.x):
            key.c = K_RIGHT
         elif(self.targetX < self.parent.x):
            key.vk = K_LEFT
         else:
            key.vk = K_NOTHING
      else:
         if(self.targetY > self.parent.y):
            key.vk = K_DOWN
         elif(self.targetY < self.parent.y):
            key.vk = K_UP
         else:
            key.vk = K_NOTHING

      return key
