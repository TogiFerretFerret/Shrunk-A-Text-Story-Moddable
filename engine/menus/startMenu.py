from engine.story.typewriter import printt
from engine.utils import clear
import engine.fsys.read
import engine.interactions.directkey as dk

creader = engine.fsys.read.FileReader()
userStrDelay = float(creader.read("config/userStrDelay.cfgf"))
def subMenu():
  clear()
  printt("1. New Game", userStrDelay)
  printt("2. Load Game", userStrDelay)
  printt("Select any key to exit", userStrDelay)
  gameLoad = int(dk.dKey(dk.numList(1,3)))
  if gameLoad == 1:
      clear()
      accountCheck() # Not passing this line?
      if getHasAccount() == 1:
          registerData()
      else:
          register()
      print()
      loadGame()
  elif gameLoad == 2:
      clear()
      accountCheck()
      print()
      loadGame()
      clear()
  else:
      clear()
      printt("Exiting to the main menu....\n\n", userStrDelay)
      time.sleep(0.5)
      clear()
      mainMenu()