import pygame
import random
circles = pygame.sprite.Group()
class Circle:
	def __init__(self, radius, LW):
		self.radius = radius
		self.img = pygame.Surface((LW, LW))
		self.rect = self.img.get_rect()
		self.x = random.randint(self.radius, 800-self.radius)
		self.y = random.randint(self.radius, 600-self.radius)
		self.speedx = 0.5*(random.random()+1.0)
		self.speedy = 0.5*(random.random()+1.0)
	def update(self):
		self.y += self.speedy
		self.x += self.speedx
		if self.x + self.radius == 800 or self.x - self.radius == 0:
			self.speedx *= -1
			self.speedy *= -1
		elif self.y + self.radius == 600 or self.y - self.radius == 0:
			self.speedx *= -1
			self.speedy *= -1
	def collide(self, spriteGroup, rect):
		if pygame.sprite.collide_circle(self, spriteGroup):
			self.speedX = -self.speedX
			self.speedY = -self.speedY