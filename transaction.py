from constants import *
from object import *
from graphic import *
from itemLoader import *

class Transaction:
   def __init__(self, transactionItem):
      self.transactionItem = transactionItem

   def getTransactionCost(self):
      return self.transactionItem.cost

   def createTransactionObject(self, xa, ya):
      newItem = self.transactionItem
      newGraphic = Graphic(self.transactionItem.char, self.transactionItem.name, 
         self.transactionItem.colour, None)
      newObject = Object(x=xa, y=ya, blocks=False, graphic=newGraphic, actor=None, item=newItem)
      return newObject     


currentTransactionItem = None
currentOfferingMerchant = None

def offerTransaction(offeredItem, merchant):
   global currentTransactionItem, currentOfferingMerchant
   currentTransactionItem = Transaction(offeredItem)
   currentOfferingMerchant = merchant

def getCurrentTransactionCost():
   global currentTransactionItem
   if (currentTransactionItem):
      return currentTransactionItem.getTransactionCost()
   else:
      return None

def getCurrentTransactionObject(x, y):
   global currentTransactionItem
   if(currentTransactionItem):
      return currentTransactionItem.createTransactionObject(x, y)
   else:
      return None

def destroyCurrentTransaction():
   global currentTransactionItem, currentOfferingMerchant
   currentOfferingMerchant = None
   currentTransactionItem = None

def transactionSuccess():
   if currentOfferingMerchant:
      currentOfferingMerchant.ai.sellableObject = None



def isActiveTransaction():
   global currentTransactionItem
   if (currentTransactionItem):
      return True
   else:
      return False