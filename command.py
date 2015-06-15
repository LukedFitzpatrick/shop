class Command:
   def __init__(self, code, executeFunction, firstInput=None, secondInput=None):
      self.executeFunction = executeFunction
      self.firstInput = firstInput
      self.secondInput = secondInput
      self.code = code
   
   def execute(self, target):
      
      if self.firstInput and not self.secondInput:
         returnValue = self.executeFunction(target, self.firstInput)
      elif self.firstInput and self.secondInput:
         returnValue = self.executeFunction(target, self.firstInput, self.secondInput)
      else:
         returnValue = self.executeFunction(target)

      return returnValue

def move(object, dx, dy, objects):
   # check for collisions ASSUMES ONLY MOVING 1 SQUARE AT A TIME
   legalMove = True
   
   for item in objects:
      # if there's something in the way which blocks, can't move there
      if item.x == (object.x + dx) and item.y == (object.y + dy) and item.blocks:
         legalMove = False
   
   if legalMove:
      object.actor.move(dx, dy)

def moveLeft(object, objects):
   move(object, -1, 0, objects)

def moveRight(object, objects):
   move(object, 1, 0, objects)

def moveUp(object, objects):
   move(object, 0, -1, objects)

def moveDown(object, objects):
   move(object, 0, 1, objects)

def openInventoryMenu(object, con):
   if(object.inventory):
      object.inventory.displayInventoryMenu(con)

def placeObject(objects, object):
   if(object):
      objects.append(object)
   return objects

def dropObject(object):
   print "in drop object"
   if object.actor:
      object.actor.dropObject()