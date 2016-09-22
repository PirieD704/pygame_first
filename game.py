import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory
from settings import Settings
import game_functions as gf # added psuedonym gf so we don't have to write out game_functions every time


# Set up the main core function
def run_game():
	pygame.init() # intitialize all the pygame modules
	game_settings = Settings()
	screen = pygame.display.set_mode(game_settings.screen_size) # Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") # set teh message on the status bar
	


	hero = Hero(screen) # set a variable equal to the class and pass it the screen

	while 1: # run this loop forever...
		gf.check_events(hero) # call gf (aliased for game_functions module) and get the check_events method
		hero.update() #update the hero location
		gf.update_screen(game_settings, screen, hero)


run_game() #Start the game!