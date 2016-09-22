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
				hero.rect.centerx += 10#Move the hero to the right!
			elif event.key == pygame.K_LEFT: #the user pressed left
				hero.rect.centerx -= 10 #Move the hero to the left!

# Handle all the screen updates and drawings
def update_screen(settings, screen, hero):
	screen.fill(settings.bg_color) # Fill the background with our green
	hero.draw_me() # call the draw method and put the hero on the screen
	pygame.display.flip()