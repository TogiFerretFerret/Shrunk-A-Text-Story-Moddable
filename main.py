import os
import forge.mod
import pluggy

pm = pluggy.PluginManager("shrunk")
pm.add_hookspecs(forge.mod.DefaultMod)

###################
##### Modload #####
###################
mods_to_load = [] # List of mods to load
# Get list of mods to load
for i in os.listdir('mods'):
  if i.endswith('.mod'):
    mods_to_load.append(i)
# Load Mods
for mod in mods_to_load:
  with open(f"./mods/{mod}","r") as rv:
    exec(rv.read())
    rv.close()
    pm.register(eval(mod[:-4]+"()"))
##################################################
##### Typing Simulation variables and others #####
##################################################
# TODO: Make this save to config file
userStrDelay = 0.04
numDeaths = 0
bestFriend = ""