# Buildings Classes

import pygame
from pygame.sprite import Sprite

class Buildings(object):
    def __init__(self, name, x1,y1, x2, y2):
        self.name = name
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        # self.rect = pygame.Rect(x1, y1, x2, y2) #will need to add numbers here
        # self.rect.centerx = self.x
        # self.rect.top = self.y
    def welcome(self):
        print ("Welcome to the %s!" % self.name)

        # also have to make a rect


# Travel_Agency = Buildings("Travel Agency")
# Bank = Buildings("Bank")
# Cafe = Buildings("Cafe") # this is also datenight! (cafe is location of date)

# What are the other two buildings? Fortune teller? Old lady to help? And the houses? Say hi gets you social/love/health points??

# ^^ or will i need to create a superclass and subclasses? not sure if each class needs its own specified location
# within the class/this file, or within the object in the game file... same goes for spaces...