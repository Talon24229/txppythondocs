#Talon P. Minecraft position test
from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    pos = mc.player.getPos()
#mc.postToChat(pos)
    mc.postToChat('your x position: ' + str(pos.x))
    mc.postToChat('your y position: ' + str(pos.y))
    mc.postToChat('your z position: ' + str(pos.z))
#mc.postToChat(mc.player.getTilePos())
