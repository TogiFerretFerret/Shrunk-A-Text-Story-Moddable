import os
import forge.mod
import pluggy
from replit import db
from colored import fore, style
import fkeycapture as fkey  # Better menus 😀
import sys
import termios
import tty
from pyfiglet import Figlet
import time

pm = pluggy.PluginManager("shrunk")
pm.add_hookspecs(forge.mod.DefaultMod)

###################
##### Modload #####
###################
mods_to_load = [] # List of mods to load
# Get list of mods to load
for i in os.listdir('mods'):
  if i.endswith('.mod'):
    mods_to_load.append(i)
# Load Mods
for mod in mods_to_load:
  with open(f"./mods/{mod}","r") as rv:
    exec(rv.read())
    rv.close()
    pm.register(eval(mod[:-4]+"()"))
##################################################
##### Typing Simulation variables and others #####
##################################################
# TODO: Make this save to config file
userStrDelay = 0.04
numDeaths = 0
bestFriend = ""
# DB Stuff
db.db_url = "https://Shrunk-Database.tg101.repl.co"  # type: ignore
os.environ["REPL_DB_URL"] = "https://Shrunk-Database.tg101.repl.co"
# Next line is so one user's data doesn't overwrite everyone else's
username = os.environ["REPL_OWNER"]
# Disclaimer code
def readDisclaim():
  print(
      f"{fore(1)}Do you want to read the disclaimer before proceeding? (y/n)\n >{style(0)}"
  )
  # disclaimerRead = str(fkey.getchars(chars=["y", "n"]))
  disclaimerRead = "n" # For Testing
  if disclaimerRead == "y":
      os.system("clear")
      disclaimer()
      mainMenu()
  else:
      os.system("clear")
      mainMenu()