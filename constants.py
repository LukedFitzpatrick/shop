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
K_NOTHING = libtcod.KEY_SPACE

MERCHANT_MOVE_LAG = 5
MERCHANT_LIFE = 500
MERCHANT_TARGET_CHANGE = 50

MERCHANT_SPAWN_CHANCE = 100

SCREEN_WIDTH = 30
GAME_HEIGHT = 20
PANEL_HEIGHT = 6
PANEL_Y = GAME_HEIGHT

WALL_COLOUR = libtcod.Color(83, 119, 122)
GAME_BACKGROUND_COLOUR = libtcod.Color(83,119,122)
PLAYER_COLOUR = libtcod.Color(217,91,67)
PANEL_BACKGROUND_COLOUR = libtcod.Color(84,36,55)

PANEL_TEXT_COLOURS = [libtcod.Color(192,41,66), libtcod.Color(254,67,101), libtcod.Color(252,251,254), 
                     libtcod.Color(249, 205, 173), libtcod.Color(200,200,169), libtcod.Color(131,175,155)]


SEE_MESSAGE_COLOUR_CODE = 5
PICKUP_MESSAGE_COLOUR_CODE = 3
DROP_MESSAGE_COLOUR_CODE = 4



PLAYER_NAME = "You"

# the maximum FPS
LIMIT_FPS = 20

def getRandomColour():
   return libtcod.Color(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))