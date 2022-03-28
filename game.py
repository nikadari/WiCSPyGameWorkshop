# To run game, type command in terminal: python3 game.py

import pygame
from sys import exit

# PART ONE: Create Pygame Window
# initiates pygame window frame
pygame.init()
# create display screen (visible output w/ width & height parameters)
screen = pygame.display.set_mode((800, 400))
# Sets name at top menu bar
pygame.display.set_caption('RUHacks PyGame Demo')
# Using Clock object to control time and frame rate (speed)
clock = pygame.time.Clock()
# Initialize font
test_font = pygame.font.Font('./font/Pixeltype.ttf', 50)
test2_font = pygame.font.Font('./font/Pixeltype.ttf', 100)


# Background
sky_surface = pygame.image.load('./graphics/sky.png').convert_alpha()
ground_surface = pygame.image.load('./graphics/ground.png').convert_alpha()

# Game Over Screen Text
gameover_surface = test2_font.render('GAME OVER', False, 'Black')
gameover2_surface = test_font.render('Press SPACE button', False, 'Black')

# Snail + Rectangle
snail_surface = pygame.image.load('./graphics/snail.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

# Player Surface + Rectangle
player_surf = pygame.image.load('./graphics/player_walk.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))

# Boolean to check game state
game_active = True
# Variable that represents gravitational pull
player_gravity = 0

# PART TWO: While True Loop will keep the window continously running
# Inside the while loop, we will draw all our elements and update everything (rendering)
while True:
    # section 1: check for triggered action
    for event in pygame.event.get():
        # Close window (if quit is selected) - add sys import statement at top
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # when game is being played (game_active = True), check if space button is hit
        if game_active:
            if event.type == pygame.KEYDOWN:
                # if up in the air, bring player back down after jump
                if event.key == pygame.K_SPACE and player_rect.bottom >= 300:
                    player_gravity = -20
        else:
            # if game over screen and space bar is hit, restart game (turn game_active from False to True)
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                snail_rect.left = 800

    # section 2: Draws Background and Scenes
    if game_active == True:
        # Background - blit = block image transfer (stack surfaces on each other)
        screen.blit(sky_surface, (0, 0))  # origin is top left
        screen.blit(ground_surface, (0, 300))

        # Snail
        snail_rect.x -= 5  # move 5 pixels to the left per frame refresh
        # once snail reaches left end, move it back to starting position (right end)
        if snail_rect.right <= 0:
            snail_rect.left = 800
        screen.blit(snail_surface, snail_rect)  # draw snail

        # Player
        # creates illusion of falling in natural speed (increasing speed as falling)
        player_gravity += 1
        player_rect.y += player_gravity
        if player_rect.bottom >= 300:
            player_rect.bottom = 300
        screen.blit(player_surf, player_rect)

        # Rectangle/Object Collision
        # methods returns 0 (no collision) or 1 (collision)
        # note: can replace with pygame.quit() if short on time
        if player_rect.colliderect(snail_rect) == 1:
            game_active = False

    else:
        # GAME OVER SCREEN
        screen.fill('Grey')
        screen.blit(gameover_surface, (250, 150))
        screen.blit(gameover2_surface, (255, 250))
        player_rect.midbottom = (80, 300)
        player_gravity = 0

    pygame.display.update()  # displays everything we have drawn in loop
    clock.tick(60)
