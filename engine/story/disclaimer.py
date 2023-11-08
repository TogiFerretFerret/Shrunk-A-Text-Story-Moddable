from engine.story.typewriter import printt
from colored import fore, style
import time
import os
import engine.interactions.directkey as dk
def readDisclaim():
  print(
      f"{fore(1)}Do you want to read the disclaimer before proceeding? (y/n)\n >{style(0)}"
  )
  # disclaimerRead = str(dk.dKey(["y", "n"]))
  
  disclaimerRead = "n" # For Testing
  
  if disclaimerRead == "y":
      os.system("clear")
      return True
  else:
      os.system("clear")
      return False
    
def disclaimer(userStrDelay):
  printt(
      f"{fore(1)}{style(5)}⚠️  DISCLAIMER: PLEASE READ THIS CAREFULLY! ⚠️ \n\n{style(0)}",
      userStrDelay,
  )
  time.sleep(0.5)
  printt(
      f"Before playing this game, it's {style(4)}highly{style(0)} recommended to read the 'guide.md' in the 📁Guide, so you won't get confused!\n\n",
      userStrDelay,
  )
  time.sleep(0.5)
  printt(fore(125) + style(1) + style(4) +
         "Understood?!\n\n" + style(0), userStrDelay)
  time.sleep(0.2)
  os.system("clear")