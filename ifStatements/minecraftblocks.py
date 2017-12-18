from mcpi.minecraft import Minecraft

mc = Minecraft.create()

wool = 35

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, wool, 3)



