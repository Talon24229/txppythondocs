#Talon Pauling
#Minevraft Code example

from mcpi.minecraft import Minecraft

mc = Minecraft.create()

mc.postToChat('Hello')

pos = mc.player.getTilePos()
mc.postToChat(pos)