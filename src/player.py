import math
import cmath
import pygame
from sympy import *
#from sympy.geometry import *

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
		self.L = [(self.x,self.y), (self.x,self.y+self.size),
			(self.x+self.size//4,self.y+(self.size*3)//4),
			(self.x+(self.size*19)//40, self.y+(self.size*5)//4),
			(self.x+(self.size*32)//50,self.y+(self.size*47)//40),
			(self.x+(self.size*21)//50,self.y+(self.size*27)//40),
			(self.x+(self.size*48)//60,self.y+(self.size*27)//40)]


	def update(self, x, y):
		dx = x - self.x
		dy = y - self.y
		self.x = x
		self.y = y
		for i in range(len(self.L)):
			self.L[i] = (self.L[i][0] + dx, self.L[i][1] + dy) 

	def draw(self, screen):
		pygame.draw.polygon(screen, pygame.Color(0,0,0), self.L)


	def getCollision(self, screen, x,y,r):

		#c = Circle((x,y), r)
		#for i in range(-1, len(self.L) - 1):
		#	l = Line(Point(L[i]), Point(L[i+1]))
#
		#	print(intersection(c, l))

		def dist(a,b):
			return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

		#def line(p1, p2):
		#	A = (p1[1] - p2[1])
		#	B = (p2[0] - p1[0])
		#	C = (p1[0]*p2[1] - p2[0]*p1[1])
		#	return A, B, -C
#
		#def intersection(L1, L2):
		#	D  = L1[0] * L2[1] - L1[1] * L2[0]
		#	Dx = L1[2] * L2[1] - L1[1] * L2[2]
		#	Dy = L1[0] * L2[2] - L1[2] * L2[0]
		#	if D != 0:
		#		x = Dx / D
		#		y = Dy / D
		#		return x,y
		#	else:
		#		return False
#
		#for i in range(-1, len(self.L) - 1):
		#	d = dist(self.L[i],self.L[i+1])
		#	dx = self.L[i][0] - self.L[i+1][0]
		#	a = math.acos(dx / d)
#
		#	c_dx = r * math.sin(a)
		#	c_dy = r * math.cos(a)
#
		#	cp = [x - c_dx, y - c_dy]
#
		#	m_line = line(self.L[i], self.L[i+1])
		#	c_line = line(cp, [x,y])
#
		#	i_p = intersection(m_line, c_line)
#
		#	if i_p != False and dist(i_p, [x, y]) < r:
		#		pygame.draw.circle(screen, pygame.Color(24,56,200), [int(i_p[0]), int(i_p[1])], 25)
		#		print("intersection")
		#		print(i_p, "(", x, y, ")", r)

		for i in range(-1, len(self.L) - 1 ):
			LAB = dist(self.L[i],self.L[i+1])
			Dx = (self.L[i+1][0]-self.L[i][0])/LAB
			Dy = (self.L[i+1][1]-self.L[i][1])/LAB
			t = (Dx*(x-self.L[i][0]) + Dy*(y-self.L[i][1])) / (LAB**2)  
			Ex = t*Dx+self.L[i][0]
			Ey = t*Dy+self.L[i][1]
			LEC = math.sqrt((Ex-x)**2+(Ey-y)**2)
			if ( LEC < r ):
				#pygame.draw.line(screen, pygame.Color(245,24,55), )
				dt = math.sqrt(r**2-LEC**2) #/ LAB
				#Fx = (t-dt)*Dx + self.L[i][0]
				#Fy = (t-dt)*Dy + self.L[i][1]
				#Gx = (t+dt)*Dx + self.L[i][0]
				#Gy = (t+dt)*Dy + self.L[i][1]
				CEV = [x-Ex,y-Ey]
				PEV = [self.L[i][0]-Ex, self.L[i][1]-Ey]
				#print("c,v", CEV, PEV)
				try:
					ang = math.acos(CEV[0]*PEV[0]+CEV[1]*PEV[1]/dist(CEV,PEV))
				except: return None
#
				return ang

