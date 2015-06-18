from constants import *
from object import *
from graphic import *
from itemLoader import *

class Sale:
   def __init__(self, saleItem):
      self.saleItem = saleItem

   def getSaleCost(self):
      return self.saleItem.cost

   def createSaleObject(self, xa, ya):
      newItem = self.saleItem
      newGraphic = Graphic(self.saleItem.char, self.saleItem.name, 
         self.saleItem.colour, None)
      newObject = Object(x=xa, y=ya, blocks=False, graphic=newGraphic, actor=None, item=newItem)
      return newObject


currentSaleItem = None
currentSaleShopper = None

def offerSale(offeredItem, shopper):
   global currentSaleItem, currentSaleShopper
   currentSaleItem = Sale(offeredItem)
   currentSaleShopper = shopper

def getCurrentSaleCost():
   global currentSaleItem
   if (currentSaleItem):
      return currentSaleItem.getSaleCost()
   else:
      return None

def getCurrentSaleObject(x, y):
   global currentSaleItem
   if(currentSaleItem):
      return currentSaleItem.createSaleObject(x, y)
   else:
      return None

def destroyCurrentSale():
   global currentSaleItem, currentSaleShopper
   currentSaleShopper = None
   currentSaleItem = None

def saleSuccess():
   if currentSaleShopper:
      currentSaleShopper.actor.pickupObject(currentSaleItem.createSaleObject(currentSaleShopper.x, currentSaleShopper.y))

def isActiveSale():
   global currentSaleItem
   if (currentSaleItem):
      return True
   else:
      return False