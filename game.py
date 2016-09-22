import sys # we will need sys so the user can quit
import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory


# Set up the main core function
def run_game():
	pygame.init() # intitialize all the pygame modules
	screen = pygame.display.set_mode((1000, 800)) # Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") # set teh message on the status bar
	
	bg_color = (82,111,53) #greeen grass color!

	hero = Hero(screen) # set a variable equal to the class and pass it the screen

	while 1: # run this loop forever...
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()

		# Fill the background with our green
		screen.fill(bg_color)
		hero.draw_me() # call the draw method and put the hero on the screen
		pygame.display.flip()


run_game() #Start the game!