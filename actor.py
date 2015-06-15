class Actor:
   def __init__(self):
      self.heldObject = None

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