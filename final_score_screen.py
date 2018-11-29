# Score Screen (Button)

import pygame.font

class Final_Score_Screen(object):
    def __init__(self, screen):
        # Print the start button
        self.screen = screen
        # How big is the screen? We need a rect
        self.screen_rect = screen.get_rect()
        # Set screen width
        self.width = 500
        # Set height
        self.height = 400
        # Set color
        self.button_color = 100, 198, 207  
        self.text_color = 255, 255, 255
        # get font from pygame!
        self.font = pygame.font.Font(None, 24)
        # Set rect of button
        self.rect = pygame.Rect(0,0,self.width, self.height)
        # Set location of rect
        self.rect.center = self.screen_rect.center

    def score_message(self, Adult, Life):
        # Set up the message!
        if Adult.total > Life.levels:
            self.image_message = self.font.render("You win! " + Adult.print_total() + Life.__repr__(), True, self.text_color)
            self.image_message_rect = self.image_message.get_rect()
            self.image_message_rect.center = self.rect.center
        elif Adult.total < Life.levels:
            self.image_message = self.font.render("Life wins! " + Adult.print_total() +  Life.__repr__(), True, self.text_color)
            self.image_message_rect = self.image_message.get_rect()
            self.image_message_rect.center = self.rect.center


    def draw_button(self):
        # fill in the button
        self.screen.fill(self.button_color, self.rect)
        # actually DRAW the button
        self.screen.blit(self.image_message, self.image_message_rect)