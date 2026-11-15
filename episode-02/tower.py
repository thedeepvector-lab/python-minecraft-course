from mcpq import Minecraft, Vec3

mc = Minecraft()
base = mc.getPlayer().pos.floor() + Vec3(14, 0, 2)

mc.setBlockCube("air", base, base + Vec3(14, 0, 0))

for i in range(15):
    mc.setBlock("quartz_block", base + Vec3(0, i, 0))
