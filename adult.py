# Adult Class

import pygame
from pygame.sprite import Sprite

class Adult(object):
    def __init__(self, name, fr_image, bk_image, r_image, l_image): # can pass in additional images here
        self.name = name
        self.x = 300
        self.y = 250
        self.fr_image = fr_image
        self.image = self.fr_image
        self.bk_image = bk_image
        self.r_image = r_image
        self.l_image = l_image
        self.health = 10
        self.career = 10
        self.adventure = 10
        self.love = 10
        self.finance = 10
        self.growth = 10
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth

    def __repr__(self):
        return "Health: %d, Career: %d, Adventure: %d, Love: %s, Finance: %d, Growth: %d " % (self.health, self.career, self.adventure, self.love, self.finance, self.growth)
    
    def print_total(self):
        return "Your Score: %d " % self.total
    
    def image_selector(self, screen, image):
        screen.blit(image, [self.x, self.y])
    
    def health_adjust(self, health_change):
        self.health += health_change
    def career_adjust(self, career_change):
        self.career += career_change
    def adv_adjust(self, adventure_change):
        self.adventure = self.adventure + adventure_change
    def love_adjust(self, love_change):
        self.love += love_change
    def finance_adjust(self, finance_change):
        self.finance += finance_change
    def growth_adjust(self, growth_change):
        self.growth += growth_change


    def update_total(self):
        self.total = self.health + self.career + self.adventure + self.love + self.finance + self.growth


