from mcpi.minecraft import Minecraft
mc = Minecraft.create()

count = 0
while count < 100:
    print(count)
    count += 2


pos = mc.player.getPos()
mc.setBlock(pos.x, pos.y, pos.z, 8)
