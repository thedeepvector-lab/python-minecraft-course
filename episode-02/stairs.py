import time
from mcpq import Minecraft, Vec3

mc = Minecraft()
start = mc.getPlayer().pos.floor() + Vec3(2, 0, 12)
colors = ["red", "orange", "yellow", "lime",
          "light_blue", "purple"]

for i in range(30):
    step = start + Vec3(i, i, 0)
    block = colors[i % 6] + "_concrete"
    mc.setBlockCube(block, step, step + Vec3(0, 0, 2))
    time.sleep(0.1)

mc.postToChat("Stairway finished: 30 steps!")
