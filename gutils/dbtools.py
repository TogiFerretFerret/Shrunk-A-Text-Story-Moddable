import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty

# Data register function
def registerData():
    global storyLocation, numDeaths, bestFriend, userStrDelay, username
    # Register new game data to the database
    storyLocation = 1
    numDeaths = 0
    bestFriend = ""
    userStrDelay = 0.04
    username = os.environ["REPL_OWNER"]
    db["storyLocation" + username] = storyLocation  # type: ignore
    db["numDeaths" + username] = numDeaths  # type: ignore
    db["bestFriend" + username] = bestFriend  # type: ignore
    db["userStrDelay" + username] = userStrDelay  # type: ignore
