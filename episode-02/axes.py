from mcpq import Minecraft, Vec3

mc = Minecraft()
home = mc.getPlayer().pos.floor() + Vec3(2, 0, 2)

for i in range(1, 9):
    mc.setBlock("red_concrete", home + Vec3(i, 0, 0))
    mc.setBlock("blue_concrete", home + Vec3(0, 0, i))
    mc.setBlock("lime_concrete", home + Vec3(0, i, 0))
