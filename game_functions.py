# We will put all main game functions here
import sys #we will need sys so the user can quit
import pygame
from bullets import Bullet #we dont care about the update or draw functions. Just the class
from bad_guy import Bad_guy

def check_events(hero, bullets, game_settings, screen):
    for event in pygame.event.get(): #run through all pygame events
        if event.type == pygame.QUIT: #if the event is the quit event...
            sys.exit() #quit
        elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
            if event.key == pygame.K_UP: #the user pressed right
                hero.moving_up = True #set the flag
            elif event.key == pygame.K_DOWN:
                hero.moving_down = True #set the flag
            if event.key == pygame.K_RIGHT: #the user pressed right
                hero.moving_right = True #set the flag
            elif event.key == pygame.K_LEFT:
                hero.moving_left = True #set the flag
            elif event.key == pygame.K_SPACE: #user pushed space bar
                new_bullet = Bullet(screen, hero, game_settings)
                bullets.add(new_bullet)
        elif event.type == pygame.KEYUP: #user let go of a key
            if event.key == pygame.K_UP: #specifically the rigth arrow
                hero.moving_up = False
            elif event.key == pygame.K_DOWN: #specifically the rigth arrow
                hero.moving_down = False
            if event.key == pygame.K_RIGHT: #specifically the rigth arrow
                hero.moving_right = False
            elif event.key == pygame.K_LEFT: #specifically the rigth arrow
                hero.moving_left = False


# Handle all teh screen updates and drawing
def update_screen(settings, screen, hero, bullets, bad_guy):
    screen.fill(settings.bg_color)# Fill teh background with our green
    hero.draw_me() #call the draw method and put the hero on the screen
    # call the draw method and put the hero on the screen
    for bad_guy in bad_guy.sprites():
        bad_guy.draw_me()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    pygame.display.flip()