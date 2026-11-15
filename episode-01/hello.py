from mcpq import Minecraft, Vec3

mc = Minecraft()
me = mc.getPlayer()
spot = me.pos.floor() + Vec3(3, 0, 3)

mc.postToChat("Hello, world. I am Python.")
colors = ["red_concrete", "orange_concrete",
          "yellow_concrete", "lime_concrete",
          "light_blue_concrete", "purple_concrete"]

for y in range(10):
    for x in range(10):
        for z in range(10):
            block = colors[y % len(colors)]
            mc.setBlock(block, spot + Vec3(x, y, z))
