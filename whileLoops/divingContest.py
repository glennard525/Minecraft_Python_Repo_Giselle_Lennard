from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

score = 0
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)

continueAnswer = "Y"
coins = 0
while continueAnswer == "Y":
    coins = coins + 1
    continueAnswer = input("Continue? Y/N")
print("You have " + str(coins) + " coins")

time.sleep(1)
pos = mc.player.getPos()
blockAbove = mc.getBlock(pos.x, pos.y + 2, pos.z)
score = score + 1
mc.postToChat("Current score: " + str(score))

mc.postToChat("Final score: " + str(score))

if score > 6:
    finalPos = mc.player.getTilePos()
    mc.setBlocks(finalPos.x - 5, finalPos.y + 10, finalPos.z - 5,
                 finalPos.x + 5, finalPos.y + 10, finalPos.z + 5, 38)
