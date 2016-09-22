import pygame #DUH
from hero import Hero #bring in the hero class with all it's methods and glory
from bad_guy import Bad_guy #bring in the bad guy class with all it's methods and terror
from settings import Settings
import game_functions as gf # added psuedonym gf so we don't have to write out game_functions every time
from pygame.sprite import Group, groupcollide

# Set up the main core function
def run_game():
	pygame.init() # intitialize all the pygame modules
	game_settings = Settings()
	screen = pygame.display.set_mode(game_settings.screen_size) # Set the screen size with set_mode
	pygame.display.set_caption("Monster Attack") # set teh message on the status bar
	hero = Hero(screen) # set a variable equal to the class and pass it the screen
	bullets = Group() #set the bullets to group
	bad_guy = Group()
	bad_guy.add(Bad_guy(screen))

	tick = 0

	while 1: # run this loop forever...
		gf.check_events(hero, bullets, game_settings, screen) # call gf (aliased for game_functions module) and get the check_events method
		hero.update() #update the hero location
		bad_guy.update(hero, game_settings.enemy_speed)
		groupcollide(bullets, bad_guy, True, True)
		tick += 1
		if tick % 150 == 0:
			bad_guy.add(Bad_guy(screen))
		bullets.update() # call the update method in the while loop
		gf.update_screen(game_settings, screen, hero, bullets, bad_guy) # call the update_screen
		for bullet in bullets: #get rid of bullets that are off the screen
			if bullet.rect.left <= 1000: #bullet bottom is at the top of the screen
				bullets.remove(bullet) #call remove() against the group
		 # print len(bullets) #print the list bullets for fun


run_game() #Start the game!