# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 14:33:02 2020

@author: user
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

x,y,z = mc.player.getTilePos()

mc.player.setTilePos(x,y,z)
time.sleep(5)


x = x + 40
mc.player.setTilePos(x,y,z)
time.sleep(5)


x = x + 20
mc.player.setTilePos(x,y,z)












