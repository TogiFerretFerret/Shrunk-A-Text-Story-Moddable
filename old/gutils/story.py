import os  # The os module for making a user interface
import time  # Importing the time module... to add suspense!
from replit import db
from pyfiglet import Figlet
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty
import json

class StorySection:
  def __init__(self, title, path):
    self.title = title
    self.path = path
  