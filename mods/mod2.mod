import forge.mod
class mod2:
    """A 2nd hook implementation namespace."""

    @forge.mod.hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_2.myhook()")
        return arg1 - arg2