import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty


def accountCheck():
    # Check if the user has a Replit account
    global hasAccount
    print("Do you have a Replit account? (y/n)")
    account = fkey.getchars(chars=["y", "n"])
    if account == "y":
        hasAccount = 1
    else:
        hasAccount = 0