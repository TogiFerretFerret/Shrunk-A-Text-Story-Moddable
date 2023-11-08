import forge.mod
from engine.story.typewriter import printt
class mod1:
    """A hook implementation namespace."""

    @forge.mod.hookimpl
    def titleShown(self):
      print("A mod1 mod")
      return
    @forge.mod.hookimpl
    def menuChoice(self,choice):
      if choice==3:
        input("Don't Leave! Please! Rerun the game! PLEASE!!!!")
      elif choice==1:
        print('Phew... TYSM')
      elif choice==2:
        print("Phew... I hope")
    @forge.mod.hookimpl
    def menuError(self):
      printt("???? WTF do you think this will do? The instructions are very clear...")
      return