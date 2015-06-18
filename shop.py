from graphic import *
from command import *
from object import *
from actor import *
from input import *
from constants import *
from itemLoader import *
from merchant import *
import libtcodpy as libtcod

def splashScreen(console):
   libtcod.console_set_default_background(console, SPLASH_BACKGROUND_COLOUR)
   libtcod.console_clear(console)
 
   #print the splash messages
   libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR1)
   libtcod.console_print_rect(console, 5, 6, SCREEN_WIDTH, SCREEN_HEIGHT, "SWORD SHOP")
   libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR2)
   libtcod.console_print_rect(console, 5, 10, SCREEN_WIDTH, SCREEN_HEIGHT, "by Luke David\n   Fitzpatrick")
   libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR3)
   libtcod.console_print_rect(console, 16, 17, SCREEN_WIDTH, SCREEN_HEIGHT, "press any key")

   # blit the panel to the screen
   libtcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-(2*4), 0, 0, 4)   
   libtcod.console_flush()
   libtcod.console_wait_for_keypress(False)

   





def playGame(player, gameObjects, con, panel):
   # main game loop starts here
   objects = gameObjects
   commandStream = []   
   #################################################################
   # need to do an initial render before going into the loop
   renderAll(objects, player, con, panel, infobar)
   libtcod.console_flush()
   key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
   # handle commands and update everything
   commandStream = inputToCommands(key, commandStream, objects, con, player)
   for command in commandStream:
      # carry out the command on the player.
      command.execute(player)
      # once we've executed the command, remove it from the stream.
      commandStream.remove(command)
   #################################################################

   #################################################################
   while not libtcod.console_is_window_closed():
      # draw all the objects first:
      renderAll(objects, player, con, panel, infobar)
      # apply drawing updates
      libtcod.console_flush()

      # clear objects ready for next frame but don't flush them
      clearAll(objects, con)

      key = libtcod.console_check_for_keypress(libtcod.KEY_PRESSED)
      # handle player commands and update everything
      commandStream = inputToCommands(key, commandStream, objects, con, player)
      for command in commandStream:
         # carry out the command on the player, or on the objects etc.
         if command.code == COMMAND_CODE_ACTOR:
            command.execute(player)
         if command.code == COMMAND_CODE_OBJECTS:
            objects = command.execute(objects)
         # once we've executed the command, remove it from the stream.
         commandStream.remove(command)

      # handle commands for each object with a brain
      for object in objects:
         if object.ai:
            if object.ai.readyToDie:
               objects.remove(object)               
            else:
               keyPressed = object.ai.generateKeypress()
               objectCommandStream = inputToCommands(keyPressed, [], objects, con, player)
               for command in objectCommandStream:
                  # carry out the command on the objects with AIs.
                  if command.code == COMMAND_CODE_ACTOR:
                     command.execute(object)
                  if command.code == COMMAND_CODE_OBJECTS:
                     objects = command.execute(objects)
                  # once we've executed the command, remove it from the stream.
                  objectCommandStream.remove(command)

      # potentially generate new merchants/shoppers
      if(random.randrange(0, MERCHANT_SPAWN_CHANCE) == 11):
            objects.append(generateMerchant())

      # update the moving messages
      updateMoveMessage(player, objects)
   #################################################################
      

objects = []

# game object initialisation
# make the player
playerActor = Actor(money=90000)
playerGraphic = Graphic('@', PLAYER_NAME, PLAYER_COLOUR, None)
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
libtcod.console_init_root(SCREEN_WIDTH, SCREEN_HEIGHT, 'SWORD SHOP', False)
libtcod.sys_set_fps(LIMIT_FPS)

panel = libtcod.console_new(SCREEN_WIDTH, PANEL_HEIGHT)
con = libtcod.console_new(SCREEN_WIDTH, GAME_HEIGHT)
infobar = libtcod.console_new(SCREEN_WIDTH, INFO_BAR_HEIGHT)
fullscreencon = libtcod.console_new(SCREEN_WIDTH, SCREEN_HEIGHT)
libtcod.console_set_default_background(con, GAME_BACKGROUND_COLOUR)

libtcod.console_clear(con)

splashScreen(fullscreencon)
libtcod.console_clear(con)

playGame(player, objects, con, panel)