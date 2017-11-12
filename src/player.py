# this creates the player/cursor class and related functions
import math
import cmath
import pygame
from sympy import *
from sympy.geometry import *

class Player(object):
	def __init__(self, x, y):
		self.angle = 0
		self.x = x
		self.y = y
		self.size = 25
		self.L = [(self.x,self.y), (self.x,self.y+self.size),
			(self.x+self.size//4,self.y+(self.size*3)//4),
			(self.x+(self.size*19)//40, self.y+(self.size*5)//4),
			(self.x+(self.size*32)//50,self.y+(self.size*47)//40),
			(self.x+(self.size*21)//50,self.y+(self.size*27)//40),
			(self.x+(self.size*48)//60,self.y+(self.size*27)//40)]

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
		if 0 < self.size + factor*25 < 150: 
			self.size += factor * 25

	def update(self, x, y):
		dx = x - self.x
		dy = y - self.y
		self.x = x
		self.y = y
		for i in range(len(self.L)):
			self.L[i] = (self.L[i][0] + dx, self.L[i][1] + dy) 

	def draw(self, screen):
		pygame.draw.polygon(screen, pygame.Color(0,0,0), self.L)

	def dist(a,b):
		return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

	def getCollision(self, x, y, r):
		c = Circle((x, y), r)
		int = None
		for i in range(len(self.L)):
			l = Line(L[i-1], L[i])
			int = intersection(c, l)
		return int

