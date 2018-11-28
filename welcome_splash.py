# Splash Screen!
import pygame.font
import pygame


class Splash_Screen(object):
    def __init__(self, screen, image_file):
        # Print the start button
        self.screen = screen
        self.image_file = image_file
        # How big is the screen? We need a rect
        self.screen_rect = screen.get_rect()
        # Set screen width
        self.width = 600
        # Set height
        self.height = 500
        # Set colors
        # self.button_color = 150,50,50
        # self.text_color = 255, 255, 255
        # get font from pygame!
        # self.font = pygame.font.Font(None, 52)
        # Set rect of button
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # Set location of rect
        self.rect.center = self.screen_rect.center

    # def setup_message(self):
    #     # Set up the message!
    #     self.image_message = self.font.render("Play", True, self.text_color)
    #     self.image_message_rect = self.image_message.get_rect()
    #     self.image_message_rect.center = self.rect.center

    def draw_button(self, screen, image_file):
        # fill in the button
        # self.screen.fill(self.button_color, self.rect)
        # actually DRAW the button
        self.screen.blit(screen, image_file, [0,0])
