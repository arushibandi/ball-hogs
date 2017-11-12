# this creates the player/cursor class and related functions
import math
import cmath
import pygame

class Player(object):
	def __init__(self, x, y):
		self.angle = 0
		self.x = x
		self.y = y
		#print("offset",self.x_offset, self.y_offset)
		self.size = 25
		self.scale = 1
		self.L = [(self.x,self.y), (self.x,self.y+self.size),
			(self.x+self.size//4,self.y+(self.size*3)//4),
			(self.x+(self.size*19)//40, self.y+(self.size*5)//4),
			(self.x+(self.size*32)//50,self.y+(self.size*47)//40),
			(self.x+(self.size*21)//50,self.y+(self.size*27)//40),
			(self.x+(self.size*48)//60,self.y+(self.size*27)//40)]
		#self.update(self.x, self.y)

	def rotateLeft(self):
		self.angle = cmath.exp((math.pi/4)*1j)
		center = complex(self.L[0][0],self.L[0][1])
		for i in range(1,len(self.L)):
			v = self.angle * (complex(self.L[i][0], self.L[i][1]) - center) + center
			self.L[i]= (v.real, v.imag)

	def rotateRight(self):
		self.angle = cmath.exp((math.pi/4)*-1j)
		center = complex(self.L[0][0],self.L[0][1])
		for i in range(1,len(self.L)):
			v = self.angle * (complex(self.L[i][0], self.L[i][1]) - center) + center
			self.L[i]= (v.real, v.imag)

	def scale(self, factor):
		if 0 < self.scale + factor < 4: self.scale += factor

	def update(self, x, y):
		dx = x - self.x
		dy = y - self.y
		self.x = x
		self.y = y
		for i in range(len(self.L)):
			self.L[i] = (self.L[i][0] + dx, self.L[i][1] + dy) 
		#print(self.L)
		#self.x = x
		#self.y = y
		#self.L = [(self.x,self.y), (self.x,self.y+self.size),
		#	(self.x+self.size//4,self.y+(self.size*3)//4),
		#	(self.x+(self.size*19)//40, self.y+(self.size*5)//4),
		#	(self.x+(self.size*32)//50,self.y+(self.size*47)//40),
		#	(self.x+(self.size*21)//50,self.y+(self.size*27)//40),
		#	(self.x+(self.size*48)//60,self.y+(self.size*27)//40)]

	def draw(self, screen):
		pygame.draw.polygon(screen, pygame.Color(0,0,0), self.L)