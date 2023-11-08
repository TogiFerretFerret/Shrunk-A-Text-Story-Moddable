import pluggy
hookspec = pluggy.HookspecMarker("shrunk")
hookimpl = pluggy.HookimplMarker("shrunk")
class DefaultMod:
  """A hook specification namespace."""
  @hookspec
  def titleShown(self):
    """Title Shown Hook"""
    pass