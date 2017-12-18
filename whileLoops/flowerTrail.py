from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0.2
while True:
    print(count)
    count += 2


pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 38)
