import forge.mod
class mod2:
    """A 2nd hook implementation namespace."""

    @forge.mod.hookimpl
    def titleShown(self):
        print("A mod2 mod")
        return