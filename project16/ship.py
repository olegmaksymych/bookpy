import pygame

class Ship:
	"""Class for ship management"""

	def __init__(self, ai_game):
		"""Initialize ship and set the starting point"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()

		"""Download the image of the ship and get his RECT"""
		self.image = pygame.image.load('image/ship1.bmp')
		self.rect = self.image.get_rect()

		"""Create each new ship at the bottom of the screen (in the center)"""
		self.rect.midbottom = self.screen_rect.midbottom

		# Save a decimal value for the horizontal position of the ship
		# Зберегти десяткове значення для позиції корабля по горизонталі
		self.x = float(self.rect.x)

		# Moving indicator = індикатор руху
		self.moving_right = False
		self.moving_left = False

	def update(self):
		"""Update the current position of the ship based on the moving indicator"""
		if self.moving_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.moving_left and self.rect.left > 0:
			self.x -= self.settings.ship_speed
		# Update the object RECT with SELF.X
		self.rect.x = self.x


	def blitme(self):
		"""Draw the ship in his current location"""
		self.screen.blit(self.image, self.rect)

