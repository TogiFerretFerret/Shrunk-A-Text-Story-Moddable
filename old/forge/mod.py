import pluggy
hookspec = pluggy.HookspecMarker("shrunk")
hookimpl = pluggy.HookimplMarker("shrunk")
class DefaultMod:
    """A hook specification namespace."""

    @hookspec
    def sparrowEncounterT(self, arg1, arg2):
        """My special little hook that you can customize."""