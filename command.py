from message import *
from constants import *
from transaction import *

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
      if object.graphic.name == PLAYER_NAME:
         pass #updateMoveMessage(object, objects)

def moveLeft(object, objects):
   move(object, -1, 0, objects)

def moveRight(object, objects):
   move(object, 1, 0, objects)

def moveUp(object, objects):
   move(object, 0, -1, objects)

def moveDown(object, objects):
   move(object, 0, 1, objects)

# place and remove objects from the game world.
def placeObject(objects, object):
   if(object):
      objects.append(object)
   return objects

def unplaceObject(objects, object):
   if(object in objects):
      objects.remove(object)
   return objects

# make an actor pick up and drop objects.
def dropObject(actorObject):
   if actorObject.actor.heldObject:
      setMessage(actorObject.graphic.name + " dropped " + actorObject.actor.heldObject.graphic.name
         , DROP_MESSAGE_COLOUR_CODE)
      actorObject.actor.dropObject()

def pickupObject(actorObject, objectToPickup):
   if actorObject.actor and not actorObject.actor.heldObject:
      setMessage(actorObject.graphic.name + " picked up " + objectToPickup.graphic.name
         + "\n(" + str(K_DROP) + " to drop.)", PICKUP_MESSAGE_COLOUR_CODE)
      actorObject.actor.pickupObject(objectToPickup)


# does the updates for standing over objects and speaking to merchants
def updateMoveMessage(object, objects):
   found = False
   # first check for actual people around who might say something
   for person in objects:
      if not found and person.ai and not (person is object) and (person.isCloseTo(object)):
         found = True
         setMessage(person.ai.getPhrase())
         # also offer a transaction here
         if person.ai.sellableObject:
            offerTransaction(person.ai.sellableObject, person)

   # next check for items on the ground
   for item in objects:
      if (item.x == object.x and item.y == object.y and not (item is object)):
         setMessage("You see a " + item.graphic.name + "\n (" + 
            str(K_PICKUP) + " to pickup)", SEE_MESSAGE_COLOUR_CODE)
         found = True
   
   if not found:
      if("You see a" in getMessage() or "says" in getMessage()):
         setMessage("", 5)
      destroyCurrentTransaction()

