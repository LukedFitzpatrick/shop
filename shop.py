from graphic import *
from command import *
from object import *
from actor import *
from input import *
from constants import *
from itemLoader import *
import libtcodpy as libtcod

def playGame(player, gameObjects, con, panel):
   # main game loop starts here
   objects = gameObjects
   commandStream = []   
   #################################################################
   # need to do an initial render before going into the loop
   renderAll(objects, con, panel)
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
      renderAll(objects, con, panel)
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
playerGraphic = Graphic('@', "You", PLAYER_COLOUR, None)
player = Object(x=5, y=5, blocks=True, graphic=playerGraphic, actor=playerActor)

items = getFullItemList()

heldItem = items[1]
heldGraphic = Graphic(heldItem.char, heldItem.name, heldItem.colour, None)
heldObject = Object(x=5, y=5, blocks=False, graphic=heldGraphic, actor=None, item=heldItem)

player.actor.pickupObject(heldObject)
objects.append(player)

# make the invisible boundary walls
# make the boundary walls on the far left and right of the screen
for row in range(0, GAME_HEIGHT):
   wallGraphic = getWallGraphic()
   newWallLeft = Object(x=-1, y=row, blocks=True, graphic=wallGraphic)
   wallGraphic = getWallGraphic()
   newWallRight = Object(x=SCREEN_WIDTH, y=row, blocks=True, graphic=wallGraphic)
   objects.append(newWallLeft)
   objects.append(newWallRight)

# make the boundary walls on the top and bottom of the screen
for column in range(0, SCREEN_WIDTH):
   wallGraphic = getWallGraphic()
   newWallTop = Object(x=column, y=-1, blocks=True, graphic=wallGraphic)
   objects.append(newWallTop)
   wallGraphic = getWallGraphic()
   newWallBottom = Object(x=column, y=GAME_HEIGHT, blocks=True, graphic=wallGraphic)  
   objects.append(newWallBottom)
   
# libtcod initialisation
libtcod.console_set_custom_font('terminal16x16_gs_ro.png', libtcod.FONT_TYPE_GREYSCALE | libtcod.FONT_LAYOUT_ASCII_INROW)
libtcod.console_init_root(SCREEN_WIDTH, GAME_HEIGHT+PANEL_HEIGHT, 'SWORD SHOP', False)
libtcod.sys_set_fps(LIMIT_FPS)
panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)
con = libtcod.console_new(SCREEN_WIDTH, GAME_HEIGHT)
libtcod.console_set_default_background(con, GAME_BACKGROUND_COLOUR)
libtcod.console_clear(con)


playGame(player, objects, con, panel)