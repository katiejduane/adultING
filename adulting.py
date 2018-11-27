# adultING

# pygame imports
import pygame
from pygame.sprite import Group, groupcollide

# imports from my files
from adult import Adult
from life import Life
from buildings import Buildings
from backgrounds import Background

# Initialize pygame
pygame.init()

# Make a screen with a size. It must be a TUPLE
screen_size = (600, 500) 
screen = pygame.display.set_mode(screen_size) 

pygame.display.set_caption('adultING') 

# game variables
map_image = pygame.image.load('map_lg.png')
char_fr = pygame.image.load("char_fr.png")
char_bk = pygame.image.load("char_bk.png")
char_r = pygame.image.load("char_right.png")
char_l = pygame.image.load("char_left.png")

# object declarations
player_1 = Adult("Katie", char_fr, char_bk, char_r, char_l)
adult_img = char_fr
background = Background(screen, 'map_lg.png')
store = Buildings("Store", -644, -1136, -856, -1232)

# main game loop
game_on = True
while game_on == True:
    # ======= Event Checker ======== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 274:
                background.should_move('up', True)
                adult_img = char_fr
            elif event.key == 273:
                background.should_move('down', True)
                adult_img = char_bk
            elif event.key == 275:
                background.should_move('right', True)
                adult_img = char_r
            elif event.key == 276:
                background.should_move('left', True)
                adult_img = char_l
        elif event.type == pygame.KEYUP:
            if event.key == 274:
                background.should_move('up', False)
            elif event.key == 273:
                background.should_move('down', False)
            elif event.key == 275:
                background.should_move('right', False)
            elif event.key == 276:
                background.should_move('left', False)
        if background.x <= store.x1 and background.x >= store.x2 and background.y <= store.y1 and background.y >= store.y2:
            print ("Yes")


    
    # draw stuff
    # screen.blit(map_image,[0,-700]) 
    background.draw_background() # map
    screen.blit(player_1.image, [player_1.x, player_1.y]) #character
    player_1.image_selector(screen, adult_img)
    pygame.display.flip()

"""Narrative: This game is derivative of my original text RPG game, where the player is posed a series of questions
that earn or lose points in various levels of life/adulting: health, money, love, career, growth, and adventurism. 
With this interface-based RPG game, the ideology is similar, but more exploratory. The player will start out on the
bottom of the map and the top is the finish. they will be given basic instructions about where the finish is and what
the goal is, buuuuttt: that's it. the rest of the game is sort of up to them--they won't be told that sitting at the 
garden or exploring the forest or strange object/properties could earn them additional points, that is where curiosity
comes in. so it's also a part discovery/curiosity game. what's here, what's there, and what will i do with what i find?
there is also the option of the outdoor dance floor, which will pose a pop up question asking them WHAT THEY WILL DO!? 
dance or run in the other direction (etc). what i'm not sure is how the questions will come up. will the enter another
space or interface or will the question pop up on that screen? programmatically, i don't know what is simpler or what
i'm more capable of, but i also know i can't possibly find the time to design that many different spaces.

questions/scenarios/spaces/interfaces:
-bank
-restaurant/date night (food and person!?)
-store
-travel agency
-out-door-dance-floor
-garden / forest / lake / pond (separate but similar)
- old buildings... haven't quite figured those out tho... wise old person, genie, what?

classes i'll need:
-player/human
-life/adulthood
-store ... algo mas?

=== i'm not really sure about the other items/space. i will have to ask Rob about this; would they be better as classes, 
or as logic? they don't all necessarily need to do anything to themselves or the player or life. Some could though, and would
require I learn how to pass objects to object.

=== i'll also need to learn how to code COLLISIONS. since the game will depend on the player colliding with certain 
spaces/objects in order to interact/answer a question about them. will this be easier if each item (eg the Travel Agnecy) is
also an object? or does it just need to be a zoned area on the map? ask Rob and also look at his RPG game code to see
how he handled collisions.

=== i'll also need to figure out the question interface, since they aren't (probably, looking at the time i'll have)
going to be entering other spaces/rooms/backgrounds. will the game screen darken, or will be there be an overlay? how
will the text appear?

- make a buildings class so i can make them sprites for groupcollide

- make a splash screen same size as the screen, need not be as large as the map image, OR, create a small 

- 512 x 480 ish for screen size, but you'll have to play with it 

"""
