from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

pos = mc.pler.getTilePos()
floorX = pos.x - 2
floorY = pos.y - 1
floorZ = pos.z - 2
width = 5
length = 5
block = 41
mc.setBlocks(floorX, floorY, floorZ,
             floorX + width, floorY, floorZ + length, block)

while floorX <= pos.x <= floorX + width and # check z is within the floor
    if block == 41:
        block = 57
    else:
        block = 41
