from graphic import *
from command import *
from object import *
from actor import *
from input import *
from constants import *
from itemLoader import *
import libtcodpy as libtcod
from inventory import *

def playGame(player, gameObjects, con):
   # main game loop starts here
   objects = gameObjects
   commandStream = []   
   #################################################################
   # need to do an initial render before going into the loop
   renderAll(objects, con)
   libtcod.console_flush()
   # handle commands and update everything
   commandStream = inputToCommands(commandStream, objects, con, player)
   for command in commandStream:
      # carry out the command on the player.
      command.execute(player)
      # once we've executed the command, remove it from the stream.
      commandStream.remove(command)
   #################################################################

   #################################################################
   while not libtcod.console_is_window_closed():
      # draw all the objects first:
      renderAll(objects, con)
      # apply drawing updates
      libtcod.console_flush()

      # clear objects ready for next frame but don't flush them
      clearAll(objects, con)

      # handle commands and update everything
      commandStream = inputToCommands(commandStream, objects, con, player)
      for command in commandStream:
         # carry out the command on the player, or on the objects etc.
         if command.code == COMMAND_CODE_ACTOR:
            command.execute(player)
         if command.code == COMMAND_CODE_OBJECTS:
            objects = command.execute(objects)
         # once we've executed the command, remove it from the stream.
         commandStream.remove(command)
   #################################################################
      

objects = []

# game object initialisation
# make the player
playerActor = Actor()
playerGraphic = Graphic('@', "You", libtcod.Color(255, 255, 255), None)
playerInventory = Inventory()
items = getFullItemList()
for item in items:
   playerInventory.addItem(item)

player = Object(x=5, y=5, blocks=True, graphic=playerGraphic, actor=playerActor, inventory=playerInventory)
objects.append(player)

# make the boundary walls
# make the boundary walls on the far left and right of the screen
for row in range(0, SCREEN_HEIGHT):
   wallGraphic = Graphic('#', "Wall", libtcod.Color(255, 255, 255), libtcod.Color(130, 150, 152))
   newWallLeft = Object(x=0, y=row, blocks=True, graphic=wallGraphic)
   wallGraphic = Graphic('#', "Wall", libtcod.Color(255, 255, 255), libtcod.Color(130, 150, 152))
   newWallRight = Object(x=SCREEN_WIDTH-1, y=row, blocks=True, graphic=wallGraphic)
   objects.append(newWallLeft)
   objects.append(newWallRight)

# make the boundary walls on the top and bottom of the screen
for column in range(0, SCREEN_WIDTH-1):
   wallGraphic = Graphic('#', "Wall", libtcod.Color(255, 255, 255), libtcod.Color(130, 150, 152))
   newWallTop = Object(x=column, y=0, blocks=True, graphic=wallGraphic)
   objects.append(newWallTop)
   # leave room for the door!
   if not column == int(SCREEN_WIDTH/2):
      wallGraphic = Graphic('#', "Wall", libtcod.Color(255, 255, 255), libtcod.Color(130, 150, 152))
      newWallBottom = Object(x=column, y=SCREEN_HEIGHT-1, blocks=True, graphic=wallGraphic)  
      objects.append(newWallBottom)
   
# libtcod initialisation
libtcod.console_set_custom_font('arial12x12.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_TCOD)
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'SWORD SHOP', False)
libtcod.sys_set_fps(LIMIT_FPS)
con = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)


playGame(player, objects, con)