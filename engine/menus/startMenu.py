def subMenu():
  os.system("clear")
  printt("1. New Game", userStrDelay)
  printt("2. Load Game", userStrDelay)
  printt("Select any key to exit", userStrDelay)
  gameLoad = int(fkey.getchars(chars=["1", "2", "3"]))
  if gameLoad == 1:
      os.system("clear")
      accountCheck() # Not passing this line?
      if getHasAccount() == 1:
          registerData()
      else:
          register()
      print()
      loadGame()
  elif gameLoad == 2:
      os.system("clear")
      accountCheck()
      print()
      loadGame()
      os.system("clear")
  else:
      os.system("clear")
      printt("Exiting to the main menu....\n\n", userStrDelay)
      time.sleep(0.5)
      os.system("clear")
      mainMenu()