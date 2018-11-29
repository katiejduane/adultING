# Backgrounds Classes
import pygame

class Background(object):
    def __init__(self, screen, image):
        self.x = -890
        self.y = -1400
        self.speed = 6
        self.screen = screen
        self.image = pygame.image.load(image)
        self.should_move_down = False
        self.should_move_up = False
        self.should_move_right = False
        self.should_move_left = False

    def draw_background(self):
        if self.should_move_right:
            if self.x >= -1766:
                self.x -= self.speed
        elif self.should_move_left:
            if self.x <= -32:
                self.x += self.speed
        elif self.should_move_up:
            if self.y >= -1424:
                self.y -= self.speed
        elif self.should_move_down:
            if self.y <= -32:
                self.y += self.speed
        self.screen.blit(self.image, [self.x, self.y])

    def should_move(self, direction, true_or_false):
        if direction == "left":
            self.should_move_left = true_or_false
        elif direction == "right":
            self.should_move_right = true_or_false
        elif direction == "up":
            self.should_move_up = true_or_false
        elif direction == "down":
            self.should_move_down = true_or_false
        print (self.x)
        print (self.y)


    def overlay_int(self, screen, image):
        screen.blit(image, [0, 0])





# class Small_Background(object):
#     def __init__(self):
#         pass

