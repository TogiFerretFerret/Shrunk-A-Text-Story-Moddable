import os
import sys
def clear():
  '''
  Clears console. Checks platform and runs appropriate command
  '''
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")