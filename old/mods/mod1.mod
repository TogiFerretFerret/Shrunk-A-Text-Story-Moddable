import forge.mod
class mod1:
    """A hook implementation namespace."""

    @forge.mod.hookimpl
    def myhook(self, arg1, arg2):
        print("inside Plugin_1.myhook()")
        return arg1 + arg2