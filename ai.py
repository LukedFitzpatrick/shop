import libtcodpy as libtcod
import random
from itemLoader import *
from constants import *

class AI:
   def __init__(self, merchant, shopper):
      self.targetX = random.randrange(0, SCREEN_WIDTH)
      self.targetY = random.randrange(GAME_Y, GAME_HEIGHT)
      self.merchant = merchant
      self.shopper = shopper
      self.lifeCounter = MERCHANT_LIFE
      self.readyToDie = False
      self.targetCounter = MERCHANT_TARGET_CHANGE
      if(self.merchant):
         self.sellableObject = random.choice(getQuickItemList())
         self.desiredCategory = None
      if(self.shopper):
         self.desiredCategory = random.choice(getQuickItemList()).category
         self.sellableObject = None

      self.speed = random.randrange(FASTEST_SPEED, SLOWEST_SPEED)
      self.moveCountdown = self.speed

   def getPhrase(self, playerHeldObject=None):
      self.moveCountdown = MERCHANT_CONVERSATION_WAIT_TIME

      if self.merchant:
         if self.sellableObject:
            return (self.parent.graphic.name + " says " + "\"Want to buy " + 
            self.sellableObject.name + " for $" + str(self.sellableObject.cost) + "?\"")
         else:
            return (self.parent.graphic.name + " says " + "\"Sorry, I'm all sold out!\"")
      
      elif self.shopper:
         if self.desiredCategory:
            if self.parent.actor.heldObject:
               return self.parent.graphic.name + " says \"Thanks!\""
            elif playerHeldObject and playerHeldObject.item.category == self.desiredCategory:
               return (self.parent.graphic.name + " says " + "\"That's what I want! You'll take $" + 
               str(playerHeldObject.item.cost) + "?")
            else:
               return (self.parent.graphic.name + " says " + "\"I want a " + 
               self.desiredCategory + "!")



   # behaviour for a merchant
   def generateMerchantKeypress(self):
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
         self.moveCountdown = self.speed
         key = self.keypressForTargetSquare()
      
      return key


   def generateShopperKeypress(self):
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
         self.moveCountdown = self.speed
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
            key.vk = K_RIGHT
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
