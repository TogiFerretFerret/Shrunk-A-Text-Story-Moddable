import forge.mod
class mod1:
    """A hook implementation namespace."""

    @forge.mod.hookimpl
    def titleShown(self):
      print("A mod1 mod")
      return