import pygame
import random
class block(pygame.sprite.Sprite):
	def __init__(self, screen, color, width, height, SX, SY):
		super(block, self).__init__()
		self.height = height
		self.width = width
		self.radius = self.width/2
		self.image = pygame.Surface((width, height), pygame.SRCALPHA, 32)
		self.color = color
		self.image.fill((0,0,0,0))
		self.screen = screen
		self.rect = self.image.get_rect()
		self.speedX = SX
		self.speedY = SY
	def update(self):
		self.rect.left += self.speedX
		self.rect.top += self.speedY
		if self.rect.left < 0 or self.rect.right > self.screen.get_width():
			self.speedX *= -1
		if self.rect.top < 0 or self.rect.bottom > self.screen.get_height():
			self.speedY *= -1
		pygame.draw.circle(self.image, self.color, (self.radius, self.radius), self.radius)
	def collide(self, spriteGroup):
		for i in spriteGroup:
			if pygame.sprite.collide_circle(self, i):
				self.speedX = -self.speedX
				self.speedY = -self.speedY