from constants import *

message = ""
messageColour = PANEL_TEXT_COLOURS[0]
def setMessage(newMessage, colourCode = 0):
   global message, messageColour
   messageColour = PANEL_TEXT_COLOURS[colourCode]
   message = newMessage

def getMessage():
   global message
   return message

def getMessageColour():
   global messageColour
   return messageColour

def getMoneyColour(money):
   return INFO_BAR_MONEY_COLOUR