import time
from mcpi.minecraft import minecraft
mc = Minecraft.create()

pos1 = mc.player.getTilepos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

time.sleep(10)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

# Compare the difference between the starting position and ending position
xDistance = x2 - x1
yDistance = 5 
zDistance = 2

# Post the results to that chat
mc.postToChat("") 
