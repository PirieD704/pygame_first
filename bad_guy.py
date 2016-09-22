import pygame #DUH
import math
from pygame.sprite import Sprite 

class Bad_guy(Sprite):
	def __init__(self, screen):
		super(Bad_guy, self).__init__()
		self.screen = screen
		# Load the hero image, get it's rect
		self.image = pygame.image.load('monster.gif')
		self.rect = self.image.get_rect() #pygame makes give us get_rect on any object so we can get some dimensions and locations
		self.screen_rect = screen.get_rect() # assing a var so the hero class knows how big and where the screen is

		self.rect.right = self.screen_rect.right #this will put the middle of the hero at the middle of the screen
		self.rect.centery = self.screen_rect.centery # this will put our hero "top" at the top of the screen
		#not self.rect.centery because we want the top on the top, not the center

	def update(self, hero, speed = 5):
		dx = self.rect.x - hero.rect.x
		dy = self.rect.y - hero.rect.y
		dist = math.hypot(dx, dy)
		dx = dx / dist
		dy = dy / dist

		self.rect.x -= dx * speed
		self.rect.y -= dy * speed

	def draw_me(self):
		self.screen.blit(self.image, self.rect) #Draw the Surface... (the image, the where)

	def __exit__(self, error):
		self.remove(self)