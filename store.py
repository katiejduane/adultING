# Store Class

import pygame
from pygame.sprite import Sprite

class Store(object):
    def __init__(self, name, item1, item2, item3, item4):
        self.name = name
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.item4 = item4
        # do i need to declare values for my items? if so, would it be better as a dictionary? if so, how would I do that?
    def points_given(self, item, points): # do i need item name here, and how will i know what amount of points to give/take without using a dict?
        pass
