from menu import *
from graphic import *
from object import *
class Inventory:
   def __init__(self):
      self.items = []
      self.itemCount = 0

   def addItem(self, item):
      # can't put something in the inventory if it's full
      if(self.itemCount >= 26):
         return False
      else:
         self.items.append(item)
         self.itemCount += 1
         return True


   def displayInventoryMenu(self, con):
       #show a menu with each item of the inventory as an option
       if self.itemCount == 0:
           options = ['Inventory is empty.']
       else:
           options = [item.name for item in self.items]
           colours = [item.colour for item in self.items]
    
       index = menu("Sword inventory:", options, colours, INVENTORY_WIDTH, con)
    
       #if an item was chosen, make the player hold it and remove it from the inventory
       if index is None or self.itemCount == 0: 
         return None
       else:
         # create an object from the item
         itemItem = self.items[index]
         itemGraphic = Graphic(itemItem.char, itemItem.name, itemItem.colour)
         itemObject = Object(x=-1, y=-1, blocks=False, graphic=itemGraphic, actor=None, item=itemItem, inventory=None)
         self.parent.actor.pickupObject(itemObject)

         self.items.remove(self.items[index])
         self.itemCount -= 1

