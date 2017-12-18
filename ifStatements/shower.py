from mcpi.minecraft import Minecraft
mc = Minecraft.create()

shwrX = 7
shwrY = 7
shwrZ = 7

width = 9
height = 9
length = 9

pos = mc.player.getTilesPos()
x = pos.x
y = pos.y
z = pos.z

if shwrX <= x < shwrX + width and 
    mc.setBlocks(shwrX, shwrY + height, shwrZ
                 shwrX + width, shwrY + height, shwrZ + length, 8)
else:
    mc.setBlocks(shwrX, shwrY + height, shwrZ
                 shwrX + width, shwrY + height, shwrZ + length, 0)

if shwrY <= y < shwrY + height and
    mc.setBlock(shwrX, shwrY + height, shwrZ
                 shwrX + width, shwrY + height, shwrZ + length, 8)
else:mc.setBlocks(shwrX, shwrY + height, shwrZ
                 shwrX + width, shwrY + height, shwrZ + length, 0)
    
