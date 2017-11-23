# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 21:13:05 2017

@author: pawel
"""

import pygame, sys,os
from pygame.locals import *
pygame.init()
window = pygame.display.set_mode((640, 800))
pygame.display.set_caption('Mastermind')
def input(events):
   for event in events:
      if event.type == QUIT:
         sys.exit(0)
      else:
         print (event)

# działaj aż do przerwania
while True:
   input(pygame.event.get())