import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty
# SetHasaccount in the name lol
def setHasAccount(val):
  with open("./cfg/ha.txt","wt") as ha:
    ha.write(str(val))
    ha.close()
# getHasAccount
def getHasAccount():
  with open("./cfg/ha.txt","r") as ha:
    return int(ha.read())
# SetUsername
# Replit Auth
# TODO: Make it yknow, actually somewhat not terrible...
def accountCheck():
    # Check if the user has a Replit account
    print("Do you have a Replit account? (y/n)")
    account = fkey.getchars(chars=["y", "n"])
    if account == "y":
        setHasAccount(1)
    else:
        setHasAccount(0)