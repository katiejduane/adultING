# adultING

# pygame imports
import pygame
from pygame.sprite import Group, groupcollide

# imports from my files
from adult import Adult
from life import Life
from buildings import Buildings

# Initialize pygame
pygame.init()

# Make a screen with a size. It must be a TUPLE.   ### my background image doesn't really show until you click the red X, then it flickers!?!?
screen_size = (600, 500) # may need to adjust!
pygame_screen = pygame.display.set_mode(screen_size) 

pygame.display.set_caption('adultING') 

# game variables
background_image = pygame.image.load('map_lg.png')

# object declarations

# main game loop
game_on = True
while game_on == True:
    # ======= Event Checker ======== #
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # draw stuff
    pygame_screen.blit(background_image,[0,-700])

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
