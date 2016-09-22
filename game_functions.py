# We will put all main game functions here
import sys
import pygame
import sys # we will need sys so the user can quit

def check_events(hero):
	for event in pygame.event.get(): # run through all pygame events
		if event.type == pygame.QUIT: # if the event is the quit event...
			sys.exit()
		elif event.type == pygame.KEYDOWN: #the user pushed a key and it's down
			if event.key == pygame.K_RIGHT: #the user pressed right
				hero.moving_right = True 
			elif event.key == pygame.K_LEFT: #the user pressed left
				hero.moving_left = True #Move the hero to the left!
		elif event.type == pygame.KEYUP: #user let go of a key
			if event.key == pygame.K_RIGHT: #specifically the right arrow
				hero.moving_right = False # boolean is changed to false
			elif event.key == pygame.K_LEFT: #specifically the left arrow
				hero.moving_left = False


# Handle all the screen updates and drawings
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color) # Fill the background with our green
	hero.draw_me() # call the draw method and put the hero on the screen
	pygame.display.flip()