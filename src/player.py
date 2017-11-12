# this creates the player/cursor class and related functions

import pygame

class Player(object):
	def __init__(self, x=0, y=0):
		self.points = []
		self.x = x
		self.y = y
		self.scale = 1

	def rotate(self):
		pass

	def scale(self, factor):
		pass
