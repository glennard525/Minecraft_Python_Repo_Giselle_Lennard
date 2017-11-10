from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x = 15
y = 15
z = 15

mc.player.setTilePos (x, y, z)

time.sleep(10)

x = 15
y = 15
z = 15

mc.player.setTilePos (x, y, z)
