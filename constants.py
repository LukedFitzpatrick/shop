import libtcodpy as libtcod
import random

COMMAND_CODE_ACTOR = 0
COMMAND_CODE_OBJECTS = 1

K_RIGHT = libtcod.KEY_RIGHT
K_LEFT = libtcod.KEY_LEFT
K_DOWN = libtcod.KEY_DOWN
K_UP = libtcod.KEY_UP
K_DROP = 'd'
K_PICKUP = 'g'
K_ACCEPT_TRANSACTION = 'y'
K_NOTHING = libtcod.KEY_SPACE

FASTEST_SPEED = 5
SLOWEST_SPEED = 20

MERCHANT_LIFE = 500
MERCHANT_TARGET_CHANGE = 50
MERCHANT_CONVERSATION_WAIT_TIME = 50
MERCHANT_SPAWN_CHANCE = 100
SHOPPER_SPAWN_CHANCE = 100

SCREEN_WIDTH = 30
INFO_BAR_HEIGHT = 1
INFO_BAR_Y = 0
GAME_HEIGHT = 20
GAME_Y = INFO_BAR_HEIGHT
PANEL_HEIGHT = 6
PANEL_Y = GAME_HEIGHT + INFO_BAR_HEIGHT

SCREEN_HEIGHT = GAME_HEIGHT + PANEL_HEIGHT + INFO_BAR_HEIGHT

WALL_COLOUR = libtcod.Color(83, 119, 122)
GAME_BACKGROUND_COLOUR = libtcod.Color(83,119,122)
PLAYER_COLOUR = libtcod.Color(0, 0, 0)#libtcod.Color(217,91,67)
PANEL_BACKGROUND_COLOUR = libtcod.Color(84,36,55)

PANEL_TEXT_COLOURS = [libtcod.Color(192,41,66), libtcod.Color(254,67,101), libtcod.Color(252,251,254), 
                     libtcod.Color(249, 205, 173), libtcod.Color(200,200,169), libtcod.Color(131,175,155)]

INFO_BAR_BACKGROUND_COLOUR = libtcod.Color(200,200,169)
INFO_BAR_MONEY_COLOUR = libtcod.Color(0,0,0)

SPLASH_BACKGROUND_COLOUR = libtcod.Color(84,36,55)
SPLASH_FOREGROUND_COLOUR1 = libtcod.Color(217,91,67)
SPLASH_FOREGROUND_COLOUR2 = libtcod.Color(249, 205, 173)
SPLASH_FOREGROUND_COLOUR3 = libtcod.Color(104,56,75)

SEE_MESSAGE_COLOUR_CODE = 5
PICKUP_MESSAGE_COLOUR_CODE = 3
DROP_MESSAGE_COLOUR_CODE = 4

PRICE_MARKUP = 1.1


STORY_TEXT1 = ("You are the owner of a boutique sword bazaar. \n\n Traders and customers from all over the world come every day to buy and sell swords.")
STORY_BACKGROUND_COLOUR1 = libtcod.Color(0, 0, 0)
STORY_FOREGROUND_COLOUR1 = libtcod.Color(249, 205, 173)


PLAYER_NAME = "You"

# the maximum FPS
LIMIT_FPS = 30

TIME_UPDATE_INCREMENT = 0.3

def getRandomColour():
   return libtcod.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
