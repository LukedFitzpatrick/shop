import libtcodpy as libtcod
from constants import *
def loadingScreen(console):
   libtcod.console_set_default_background(console, libtcod.Color(0, 0, 0))
   libtcod.console_clear(console)
 
   #print the splash messages
   libtcod.console_set_default_foreground(console, libtcod.Color(200, 200, 200))
   libtcod.console_print_rect(console, 4, 8, SCREEN_WIDTH, SCREEN_HEIGHT, "loading swords...")

   # blit the panel to the screen
   libtcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-(2*4), 0, 0, 4)   
   libtcod.console_flush()


def splashScreen(console):
   libtcod.console_set_default_background(console, SPLASH_BACKGROUND_COLOUR)
   libtcod.console_clear(console)
   
   done = False
   counter = 0
   blinkOn = True
   blinkSpeed = 10

   while not done and not libtcod.console_is_window_closed():
      key = libtcod.console_check_for_keypress(True)
      if not key.vk == libtcod.KEY_NONE:
         done = True

      #print the splash messages
      libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR1)
      libtcod.console_print_rect(console, 4, 5, SCREEN_WIDTH, SCREEN_HEIGHT, "SWORD SHOP")
      libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR2)
      libtcod.console_print_rect(console, 4, 8, SCREEN_WIDTH, SCREEN_HEIGHT, "by luke david\n   fitzpatrick")
      if(blinkOn):
         libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR3)
         libtcod.console_print_rect(console, 16, 13, SCREEN_WIDTH, SCREEN_HEIGHT, "press any key")

      # blit the panel to the screen
      libtcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-(2*6), 0, 0, 6)   
      
      libtcod.console_flush()

      counter += 1
      if counter >= blinkSpeed:
         counter = 0
         blinkOn = not blinkOn
         libtcod.console_clear(console)



def storyScreen(console):
   libtcod.console_set_default_background(console, STORY_BACKGROUND_COLOUR1)
   libtcod.console_clear(console)
   
   done = False
   counter = 0
   blinkOn = True
   blinkSpeed = 10

   while not done and not libtcod.console_is_window_closed():
      key = libtcod.console_check_for_keypress(True)
      if not key.vk == libtcod.KEY_NONE:
         done = True

      #print the story message
      libtcod.console_set_default_foreground(console, STORY_FOREGROUND_COLOUR1)
      libtcod.console_print_rect(console, 1, 3, SCREEN_WIDTH, SCREEN_HEIGHT, STORY_TEXT1)
      if(blinkOn):
         libtcod.console_set_default_foreground(console, SPLASH_FOREGROUND_COLOUR3)
         libtcod.console_print_rect(console, 16, 22, SCREEN_WIDTH, SCREEN_HEIGHT, "press any key")

      # blit the panel to the screen
      libtcod.console_blit(console, 0, 0, SCREEN_WIDTH, SCREEN_HEIGHT-(2*1), 0, 0, 1)   
      
      libtcod.console_flush()

      counter += 1
      if counter >= blinkSpeed:
         counter = 0
         blinkOn = not blinkOn
         libtcod.console_clear(console)

   libtcod.console_clear(console)
