import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


count = 0
while count < 5:
    x = random.randint(-127, 127)
    y = random.randint(0, 64)
    z = random.randint(-127, 127)
    print(count)
    count += 1
print("Loop finished")



mc.player.setTilePos(x, y, z)
count += 1
