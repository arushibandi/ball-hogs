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

	def getCollision(x,y,r):
		for i in range(len(self.L)):
			LAB = dist(self.L[i],self.L[i+1])
			Dx = (self.L[i+1][0]-L[i][0])/LAB
			Dy = (L[i+1][1]-L[i][1])/LAB
			t = Dx*(x-L[i][0]) + Dy*(y-L[i][1])    
			Ex = t*Dx+L[i][0]
			Ey = t*Dy+L[i][1]
			LEC = math.sqrt((Ex-x)**2+(Ey-y)**2)
			if ( LEC < r ):
				dt = math.sqrt(r**2-LEC**2)
				Fx = (t-dt)*Dx + L[i][0]
				Fy = (t-dt)*Dy + L[i][1]
				Gx = (t+dt)*Dx + L[i][0]
				Gy = (t+dt)*Dy + L[i][1]
				if dist([Fx,Fy],[L[i][0],L[i][1]]) < dist([Gx,Gy],[L[i][0],L[i][1]]):
					return (Fx,Fy)
				else:
					return (Gx,Gy)

	'''def getCollision(self, x, y, r):
		c = Circle((x, y), r)
		int = None
		for i in range(len(self.L)):
			l = Line(self.L[i-1], self.L[i])
			int = intersection(c, l)
			if int != None:
				return (int, self.L[i-1], self.L[i])'''
