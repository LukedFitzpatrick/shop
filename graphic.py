import libtcodpy as libtcod
from constants import *
from message import *

class Graphic:
   def __init__(self, char, name, colour, backgroundColour=None):
      self.char = char
      self.currentChar = char
      self.name = name
      self.colour = colour
      self.currentColour = colour
      if backgroundColour:
         self.backgroundColour = backgroundColour
      else:
         self.backgroundColour = libtcod.BKGND_NONE

   def draw(self, con):
      #set the color and then draw the character that represents this object at its position
      currentChar = self.getChar()
      libtcod.console_set_default_foreground(con, self.currentColour)
      libtcod.console_set_default_background(con, self.backgroundColour)
      libtcod.console_put_char(con, self.parent.x, self.parent.y, currentChar, flag=libtcod.BKGND_DEFAULT)
 
   def clear(self, con):
      #erase the character that represents this object
      libtcod.console_put_char(con, self.parent.x, self.parent.y, ' ', libtcod.BKGND_NONE)

   def getChar(self):
      # if we're holding an object, then blink between the two chars
      if self.parent.actor and self.parent.actor.heldObject:
         if(self.currentChar == self.char):
            self.currentChar = self.parent.actor.heldObject.graphic.char
            self.currentColour = self.parent.actor.heldObject.graphic.colour

         else:
            self.currentChar = self.char
            self.currentColour = self.colour
      else:
         self.currentChar = self.char

      return self.currentChar

def clearAll(objects, con):
   for object in objects:
      if object.graphic:
         object.graphic.clear(con)
   libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, GAME_HEIGHT, 0, 0, GAME_Y)

def renderAll(objects, player, con, panel, infobar):
   # draw objects without actors first
   for object in objects:
      if not object.actor:
         object.graphic.draw(con)
   for object in objects:
      if object.actor:
         object.graphic.draw(con)
   
   libtcod.console_blit(con, 0, 0, SCREEN_WIDTH, GAME_HEIGHT, 0, 0, GAME_Y)

   # do panel stuff
   libtcod.console_set_default_background(panel, PANEL_BACKGROUND_COLOUR)
   libtcod.console_clear(panel)
 
   #print the current game message
   libtcod.console_set_default_foreground(panel, getMessageColour())
   libtcod.console_print_rect(panel, 1, 1, SCREEN_WIDTH-1, PANEL_HEIGHT, getMessage())
   
   # blit the panel to the screen
   libtcod.console_blit(panel, 0, 0, SCREEN_WIDTH, PANEL_HEIGHT, 0, 0, PANEL_Y)

   # do info bar stuff
   libtcod.console_set_default_background(infobar, INFO_BAR_BACKGROUND_COLOUR)
   libtcod.console_clear(infobar)
   
   # print their current money
   libtcod.console_set_default_foreground(infobar, getMoneyColour(player.actor.money))
   libtcod.console_print_rect(infobar, SCREEN_WIDTH/2 - 3, 0, SCREEN_WIDTH, INFO_BAR_HEIGHT, "$"+str(player.actor.money))

   libtcod.console_blit(infobar, 0, 0, SCREEN_WIDTH, INFO_BAR_HEIGHT, 0, 0, INFO_BAR_Y)



   



def getWallGraphic():
   wallGraphic = Graphic('0', "Wall", WALL_COLOUR)
   return wallGraphic