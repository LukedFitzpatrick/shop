from command import *
from constants import *
from transaction import *
from message import *
from sale import *
from functools import partial


def inputToCommands(key, commands, objects, con, player):
   # looks at what key is pressed and creates commands which control the game 

   # they pressed the left key
   if key.vk == K_LEFT:
      moveCommand = Command(COMMAND_CODE_ACTOR, moveLeft, objects)
      commands.append(moveCommand)
     
   # they pressed the right key
   elif key.vk == K_RIGHT:
      moveCommand = Command(COMMAND_CODE_ACTOR, moveRight, objects)
      commands.append(moveCommand)

   # they pressed the down key
   elif key.vk == K_DOWN:
      moveCommand = Command(COMMAND_CODE_ACTOR, moveDown, objects)
      commands.append(moveCommand)

   # they pressed the up key
   elif key.vk == K_UP:
      moveCommand = Command(COMMAND_CODE_ACTOR, moveUp, objects)
      commands.append(moveCommand)

   # it might be a 'character' key
   else:
      key_char = chr(key.c)

      # they dropped an object onto the ground
      if key_char == K_DROP and player.actor.heldObject:
         placeCommand = Command(COMMAND_CODE_OBJECTS, placeObject, player.actor.heldObject)
         dropCommand = Command(COMMAND_CODE_ACTOR, dropObject)
         commands.append(placeCommand)
         commands.append(dropCommand)

      # they picked up an object off the ground
      elif key_char == K_PICKUP and not player.actor.heldObject:
         foundObject = None
         for object in objects:
            if not foundObject and (object.x == player.x and object.y == player.y and not (object is player)):
               foundObject = object

         if foundObject:
            pickupCommand = Command(COMMAND_CODE_ACTOR, pickupObject, foundObject)
            unplaceCommand = Command(COMMAND_CODE_OBJECTS, unplaceObject, foundObject)
            commands.append(pickupCommand)
            commands.append(unplaceCommand)

      elif key_char == K_ACCEPT_TRANSACTION:
         if isActiveTransaction():
            if(player.actor.takeMoney(getCurrentTransactionCost())):
               placeCommand = Command(COMMAND_CODE_OBJECTS, placeObject, getCurrentTransactionObject(player.x, player.y))
               commands.append(placeCommand)
               transactionSuccess()
               destroyCurrentTransaction()
            else:
               setMessage("Not enough cash!", 1)

         elif isActiveSale():
            player.actor.giveMoney(getCurrentSaleCost())
            dropCommand = Command(COMMAND_CODE_ACTOR, dropObject)
            commands.append(dropCommand)
            saleSuccess()
            destroyCurrentSale()
         
   return commands
