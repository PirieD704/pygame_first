import pygame#duh

class Hero(object):
	def __init__(self, screen):
		self.screen = screen # give the hero the ability to control the screen

		# Load the hero image, get it's rect
		self.image = pygame.image.load('ball.gif')
		self.rect = self.image.get_rect() #pygame makes give us get_rect on any object so we can get some dimensions and locations
		self.screen_rect = screen.get_rect() # assing a var so the hero class knows how big and where the screen is

		self.rect.centerx = self.screen_rect.centerx #this will put the middle of the hero at the middle of the screen
		self.rect.bottom = self.screen_rect.bottom # this will put our hero "bottom" at the bottom of the screen
		#not self.rect.centery because we want the bottom on the bottom, not the center

	def draw_me(self):
		self.screen.blit(self.image, self.rect) #Draw the Surface... (the image, the where)

