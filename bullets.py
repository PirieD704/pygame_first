import pygame #DUH
from pygame.sprite import Sprite

class Bullet(Sprite):
	def __init__(self, screen, hero, game_settings):
		super(Bullet, self).__init__()
		self.screen = screen
		self.rect = pygame.Rect(0, 0, game_settings.bullet_width, game_settings.bullet_height) #Make a bullet 
		self.rect.centery = hero.rect.centery
		self.rect.right = hero.rect.right
		self.color = game_settings.bullet_color
		self.speed = game_settings.bullet_speed
		self.x = self.rect.x

	def update(self):
		self.x += self.speed #change the y, each time update is run, by bullet speed
		self.rect.x = self.x #update rect position

	def draw_bullet(self):
		pygame.draw.rect(self.screen, self.color, self.rect) #draw the bullet!
