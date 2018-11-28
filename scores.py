# Levels/Score 

import pygame.font

class Scores_Button(object):
    def __init__(self, screen): # i passed in Adult because I need to generate the self.total /repr printout as the scores
        # Print the start button
        self.screen = screen
        # How big is the screen? We need a rect
        self.screen_rect = screen.get_rect()
        # Set screen width
        self.width = 600
        # Set height
        self.height = 25
        # Set color
        self.button_color = 191, 146, 177  
        self.text_color = 255, 255, 255
        # get font from pygame!
        self.font = pygame.font.Font(None, 18)
        # Set rect of button
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # Set location of rect
        self.rect.center = (300,10) # this won't work it needs to be 0,0 of screen

    def score_message(self, Adult):
        # Set up the message!
        self.image_message = self.font.render("Your Scores: " + Adult.__repr__(), True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color, self.rect)
        # actually DRAW the button
        self.screen.blit(self.image_message, self.image_message_rect)


class Life_Scores_Button(object):
    def __init__(self, screen): 
        # Print the start button
        self.screen = screen
        # How big is the screen? We need a rect
        self.screen_rect = screen.get_rect()
        # Set screen width
        self.width = 600
        # Set height
        self.height = 25
        # Set color
        self.button_color = 223, 185, 68 
        self.text_color = 255, 255, 255
        # get font from pygame!
        self.font = pygame.font.Font(None, 18)
        # Set rect of button
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # Set location of rect
        self.rect.center = (300,490) 

    def score_message(self, Life):
        # Set up the message!
        self.image_message = self.font.render(Life.__repr__(), True, self.text_color)
        self.image_message_rect = self.image_message.get_rect()
        self.image_message_rect.center = self.rect.center

    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color, self.rect)
        # actually DRAW the button
        self.screen.blit(self.image_message, self.image_message_rect)
