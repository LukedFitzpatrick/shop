from command import *
from constants import *
from functools import partial


def inputToCommands(commands, objects, con, player):
   # looks at what key is pressed and creates commands which control the game 
   key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
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
      # they tried to open the inventory
      if key_char == K_INVENTORY:
         inventoryCommand = Command(COMMAND_CODE_ACTOR, openInventoryMenu, con)
         commands.append(inventoryCommand)

      if key_char == K_DROP:
         placeCommand = Command(COMMAND_CODE_OBJECTS, placeObject, player.actor.heldObject)
         dropCommand = Command(COMMAND_CODE_ACTOR, dropObject)
         commands.append(placeCommand)
         commands.append(dropCommand)
         
   return commands