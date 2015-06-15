import ConfigParser
from graphic import *
from object import *
import libtcodpy as libtcod

class Item:
   def __init__(self, char, name, colour, cost):
      self.cost = cost
      self.char = char
      self.name = name
      self.colour = colour

   def getCost(self):
      return self.cost

def ConfigSectionMap(section):
   dict1 = {}
   Config = ConfigParser.RawConfigParser()
   Config.read('items.cfg')
   options = Config.options(section)
   for option in options:
      try:
         dict1[option] = Config.get(section, option)
         if dict1[option] == -1:
            DebugPrint("skip: %s" % option)
      except:
         print("exception on %s!" % option)
         dict1[option] = None
   return dict1


def getFullItemList():
   Config = ConfigParser.RawConfigParser()
   Config.read('items.cfg')
   sections = Config.sections()

   items = []
   for section in sections:
      name = ConfigSectionMap(section)["name"]
      char = ConfigSectionMap(section)["char"]
      red = int(ConfigSectionMap(section)["red"])
      green = int(ConfigSectionMap(section)["green"])
      blue = int(ConfigSectionMap(section)["blue"])
      cost = int(ConfigSectionMap(section)["cost"])

      newItem = Item(char, name, libtcod.Color(red, green, blue), cost)
      items.append(newItem)

   return items

