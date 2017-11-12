import math
import cmath
import pygame

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

	def getCollision(self, x,y,r):

		def dist(a,b):
			return ((a[0]-b[0])**2+(a[1]-b[1])**2)**.5

		for i in range(len(self.L) - 1 ):
			LAB = dist(self.L[i],self.L[i+1])
			Dx = (self.L[i+1][0]-self.L[i][0])/LAB
			Dy = (self.L[i+1][1]-self.L[i][1])/LAB
			t = Dx*(x-self.L[i][0]) + Dy*(y-self.L[i][1])    
			Ex = t*Dx+self.L[i][0]
			Ey = t*Dy+self.L[i][1]
			LEC = math.sqrt((Ex-x)**2+(Ey-y)**2)
			if ( LEC < r and dist([x,y],self.L[i]) <= r):
				dt = math.sqrt(r**2-LEC**2)
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

				return ang


