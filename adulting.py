# adultING

# pygame imports
import pygame
from pygame.sprite import Group, groupcollide

# imports from my files
from adult import Adult
from life import Life
from buildings import Buildings
from spaces import Spaces
from backgrounds import Background
from welcome_splash import Splash_Screen
from scores import Scores_Button, Life_Scores_Button
from final_score_screen import Final_Score_Screen

# Initialize pygame
pygame.init()
pygame.mixer.init()

# music file
bg_music = pygame.mixer.Sound('brainclaim__saw-cutting-2.wav')

# Make a screen with a size. It must be a TUPLE
screen_size = (600, 500) 
screen = pygame.display.set_mode(screen_size) 

pygame.display.set_caption('adultING') 

# game variables and images
map_image = pygame.image.load('map_lg.png')
welcome_img = pygame.image.load('welcome.png')
char_fr = pygame.image.load('char_fr.png')
char_bk = pygame.image.load('char_bk.png')
char_r = pygame.image.load('char_right.png')
char_l = pygame.image.load('char_left.png')
bank_img = pygame.image.load('bank.png')
travel_img = pygame.image.load('travel_agency.png')
cafe_img = pygame.image.load('cafe_date.png')
forest_img = pygame.image.load('forest.png')
opportunity_img = pygame.image.load('opportunity.png')
adult_img = char_fr

# object declarations
# welcome = Splash_Screen(screen)
player_1 = Adult("Katie", char_fr, char_bk, char_r, char_l)
life_1 = Life()
score_tracker = Scores_Button(screen)
life_tracker = Life_Scores_Button(screen)
background = Background(screen, 'map_lg.png')
cafe = Buildings("Cafe", -644, -1136, -856, -1232)
bank = Buildings("Bank", -164, -464, -380, -638)
travel_agency = Buildings("Travel Agency", -284, -200, -422, -368)
forest = Spaces("Forest", -1010, -32, -1742, -452)
opportunity = Buildings("Opportunities", -194, -1094, -272, -1238)

central_lake = Spaces("Central Lake", -746, -566, -1028, -812)
final_screen = Final_Score_Screen(screen)


# # game_functions
# def change_background(screen, image):
#     screen.blit(image, [0, 0])

# sounds
# bg_music = pygame.mixer.Sound('brainclaim_saw-cutting-2.wav')

# ====================MAIN GAME LOOP===================== #
game_on = True
splash_on = True

#building/space booleans
over_cafe = False
over_bank = False
over_travel = False
over_forest = False
over_dancefloor = False
over_store = False
over_pond = False
over_help = False
over_opportunity = False

cafe_int = False
bank_int = False
travel_int = False
forest_int = False
dancefloor_int = False
store_int = False
pond_int = False
help_int = False
opportunity_int = False

over_central_lake = False
final_score_screen_on = False

while game_on == True:
    # ======= Event Checker ======== #
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            splash_on = False    
        if event.type == pygame.QUIT:
                game_on = False
        if event.type == pygame.KEYDOWN:
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
            if event.key == 13 and over_cafe == True:
                cafe_int = True
            if cafe_int == True:
                print ("cafe int is true")
                if event.key == pygame.K_1:
                    player_1.love_adjust(6), player_1.health_adjust(-3), player_1.adv_adjust(3)
                    life_1.adjust_levels(4)
                elif event.key == pygame.K_2:
                    player_1.love_adjust(8), player_1.health_adjust(2)
                elif event.key == 32:
                    cafe_int = False
                else:
                    pass
                # play error sound?
            if event.key == 13 and over_bank == True:
                bank_int = True
            if bank_int == True:
                if event.key == pygame.K_1:
                    player_1.finance_adjust(9), player_1.adv_adjust(-3)
                    life_1.adjust_levels(4)
                elif event.key == pygame.K_2:
                    player_1.finance_adjust(3), player_1.adv_adjust(6)
                    life_1.adjust_levels(2)
                elif event.key == 32:
                    bank_int = False
                else:
                    pass
                # play error sound?
            if event.key == 13 and over_travel == True:
                travel_int = True
            if travel_int == True:
                if event.key == pygame.K_1:
                    player_1.health_adjust(-3), player_1.adv_adjust(-3)
                    life_1.adjust_levels(2)
                elif event.key == pygame.K_2:
                    player_1.adv_adjust(6), player_1.health_adjust(6)
                elif event.key == pygame.K_3:
                    player_1.adv_adjust(9), player_1.growth_adjust(6)
                elif event.key == pygame.K_4:
                    player_1.adv_adjust(-6)
                    life_1.adjust_levels(2)
                elif event.key == 32:
                    travel_int = False
                elif event.key != pygame.K_1 and event.key != pygame.K_2 and  event.key != pygame.K_3 and event.key != pygame.K_4 and event.key is not None:
                    bg_music.play() # This isn't working!
            if event.key == 13 and over_forest == True:
                forest_int = True
            if forest_int == True:
                if event.key == pygame.K_1:
                    player_1.adv_adjust(-6), player_1.health_adjust(-3)
                    life_1.adjust_levels(4)
                elif event.key == pygame.K_2:
                    player_1.adv_adjust(3), player_1.health_adjust(3), player_1.growth_adjust(3)
                elif event.key == pygame.K_3:
                    player_1.adv_adjust(6), player_1.health_adjust(3), player_1.growth_adjust(3)
                elif event.key == 32:
                    forest_int = False
            if event.key == 13 and over_opportunity == True:
                opportunity_int = True
            if opportunity_int == True:
                if event.key == pygame.K_1:
                    player_1.adv_adjust(3), player_1.career_adjust(-6), player_1.growth_adjust(3), player_1.love_adjust(3), player_1.finance_adjust(-3)
                    life_1.adjust_levels(4)
                elif event.key == pygame.K_2:
                    player_1.adv_adjust(-3), player_1.career_adjust(6), player_1.growth_adjust(3), player_1.finance_adjust(3)
                elif event.key == 32:
                    opportunity_int = False


            if event.key == 13 and over_central_lake == True:
                final_score_screen_on = True
                if final_score_screen_on == True:
                    if event.key == 32:
                        game_on = False
                    else:
                        continue
                    # how to make it play again, starting from beginnging??? There also isn't a message printing to tell the player what to do... how to do that?

        over_cafe = False
        over_bank = False
        over_travel = False
        over_forest = False
        over_dancefloor = False
        over_store = False
        over_pond = False
        over_help = False
        over_opportunity = False
        over_central_lake = False
        
        if background.x <= cafe.x1 and background.x >= cafe.x2 and background.y <= cafe.y1 and background.y >= cafe.y2:
            print ("Cafe")
            over_cafe = True
        elif background.x <= bank.x1 and background.x >= bank.x2 and background.y <= bank.y1 and background.y >= bank.y2:
            print ("Bank")
            over_bank = True
        elif background.x <= travel_agency.x1 and background.x >= travel_agency.x2 and background.y <= travel_agency.y1 and background.y >= travel_agency.y2:
            print ("Travel")
            over_travel = True
        elif background.x <= forest.x1 and background.x >= forest.x2 and background.y <= forest.y1 and background.y >= forest.y2:
            print ("Forest")
            over_forest = True
        elif background.x <= opportunity.x1 and background.x >= opportunity.x2 and background.y <= opportunity.y1 and background.y >= opportunity.y2:
            print ("Opportunity")
            over_opportunity = True
        elif background.x <= central_lake.x1 and background.x >= central_lake.x2 and background.y <= central_lake.y1 and background.y >= central_lake.y2:
            print ("Central Lake")
            over_central_lake = True


    score_tracker.score_message(player_1)
    life_tracker.score_message(life_1)
    final_screen.score_message(player_1, life_1)

    
    # draw background
    background.draw_background() # map
    if splash_on == False:
        screen.blit(player_1.image, [player_1.x, player_1.y])
        player_1.image_selector(screen, adult_img) #character
    # if cafe_int == False
    # draw splash/welcome
    if splash_on == True:
        screen.blit(welcome_img, [0, 0])
    # draw char
    # conditions for drawing buildings
    if cafe_int == True:
        screen.blit(cafe_img, [0, 0])
    if bank_int == True:
        screen.blit(bank_img, [0, 0])
    if travel_int == True:
        screen.blit(travel_img, [0, 0])
    if forest_int == True:
        screen.blit(forest_img, [0, 0])
    if opportunity_int == True:
        screen.blit(opportunity_img, [0, 0])

    if final_score_screen_on == True:
        final_screen.draw_button()
        
    # method for changing the char image based on direction of mvmnt
    
    # draw score button
    score_tracker.draw_button()
    life_tracker.draw_button()
    

    pygame.display.flip()
