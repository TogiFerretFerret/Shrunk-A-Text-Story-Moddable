from colored import fore, style
import engine.interactions.directkey as dk  # Better menus 😀
import time
import engine.story.disclaimer
from engine.story.typewriter import printt
import engine.fsys.read
import engine.menus.startMenu
from engine.utils import clear
from main import pm
creader = engine.fsys.read.FileReader()
userStrDelay = float(creader.read("config/userStrDelay.cfgf"))

def mainMenu():
  global userStrDelay, numDeaths, bestFriend, storyLocation
  printt(fore(14) + "TG 101 presents...\n" + style(0), userStrDelay)
  printt(fore(14) + "Modding Framework by RiverdaleSuperCoder...\n\n\n" + style(0), userStrDelay)
  time.sleep(1)
  # Print Title
  reader = engine.fsys.read.FileReader()
  print(reader.read("data/titleText.txt"))
  pm.hook.titleShown()
  time.sleep(0.5)
  printt("\n Welcome to this game...\n\n", userStrDelay)
  time.sleep(0.5)
  printt("1. Start", userStrDelay)
  printt("2. Options", userStrDelay)
  printt("3. Exit", userStrDelay)
  while True:
      try:
          print("Would you like to start your adventure or quit?\n")
          choice = int(dk.dKey(["1", "2", "3"]))
          pm.hook.menuChoice(choice=choice)
          if choice == 1:
              engine.menus.startMenu.subMenu()
              break
          elif choice == 3:
              printt("Goodbye!", userStrDelay)
              quit(0)
          elif choice == 2:
              options()
      except ValueError:
          pm.hook.menuError()
          printt("Invalid input! Try Again!", userStrDelay)
          continue