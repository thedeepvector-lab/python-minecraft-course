from mcpq import Minecraft

mc = Minecraft()
mc.postToChat("Hello Minecraft, this is Python!")

me = mc.getPlayer()
print(me.pos)
