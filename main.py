import os
import forge.mod
import pluggy
from replit import db
from colored import fore, style
import engine.interactions.directkey as dk  # Better menus 😀
import sys
import termios
import tty
from pyfiglet import Figlet
import time
import engine.story.disclaimer
from engine.story.typewriter import printt
import engine.fsys.read
import engine.menus.startMenu
from engine.utils import clear
pm = pluggy.PluginManager("shrunk")
pm.add_hookspecs(forge.mod.DefaultMod)
import engine.menus.mainMenu
#####################
##### Modloader #####
#####################
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
creader = engine.fsys.read.FileReader()
userStrDelay = float(creader.read("config/userStrDelay.cfgf"))
# TODO: Make this save to config file
numDeaths = 0
bestFriend = ""
# DB Stuff
db.db_url = "https://Shrunk-Database.tg101.repl.co"  # type: ignore
os.environ["REPL_DB_URL"] = "https://Shrunk-Database.tg101.repl.co"
# Next line is so one user's data doesn't overwrite everyone else's
username = os.environ["REPL_OWNER"]




# Disclaimer code
if engine.story.disclaimer.readDisclaim():
  engine.story.disclaimer.disclaimer(userStrDelay)
  engine.menus.mainMenu.mainMenu()
else:
  # TODO: Then run main story
  engine.menus.mainMenu.mainMenu()

