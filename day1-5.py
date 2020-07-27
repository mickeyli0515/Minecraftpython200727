# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 15:30:10 2020

@author: user
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time

a = 0
while True:
    mc.postToChat("不要刷頻 警告" + str(a) + "次")
    
    a = a +1
    time.sleep(1)