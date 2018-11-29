# Life Class

import pygame
from pygame.sprite import Sprite

class Life(object):
    def __init__(self):
        self.levels = 60
    def adjust_levels(self, adjust):
        self.levels += adjust
    def __repr__(self):
        return "Life: %d" % self.levels