class Actor:
   def __init__(self, money=0):
      self.heldObject = None
      self.money = money

   def move(self, dx, dy):
      if(self.parent):
         self.parent.x += dx
         self.parent.y += dy
         if(self.heldObject):
            self.heldObject.x = self.parent.x
            self.heldObject.y = self.parent.y
      else:
         print "BAD NEWS: An actor that doesn't have a parent tried to move."

   def pickupObject(self, object):
      self.heldObject = object

   def dropObject(self):
      oldObject = self.heldObject
      self.heldObject = None
      self.parent.graphic.currentColour = self.parent.graphic.colour
      self.parent.graphic.currentChar = self.parent.graphic.char
      return oldObject

   def giveMoney(self, amount):
      self.money += amount

   def takeMoney(self, amount):
      if amount > self.money:
         return None
      else:
         self.money -= amount
         return True

