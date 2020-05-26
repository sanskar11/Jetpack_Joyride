from character import *

class Boss(Main_person):

	def __init__(self,ycoo,xcoo,life):
		Main_person.__init__(self,ycoo,xcoo,life)
		self.boss=[]
		self.temp=0
		self.balls=[]

	def create_boss(self,grid):
		with open("./dragon") as obj:
			for line in obj:
				self.boss.append(line.strip('\n'))

		for i in range(10):
			for j in range(50):
				grid[self.ycoo+i][self.xcoo+j]=self.boss[i][j]

	def move_boss(self,grid,player_ycoo,player_xcoo):
		for i in range(10):
			for j in range(50):
				grid[self.ycoo+i][self.xcoo+j]=" "
		# if (self.temp%2)==0:
		# 	self.ycoo = self.ycoo+1
		# else:
		# 	self.ycoo = self.ycoo-1

		# if(self.ycoo == 17):
		# 	self.temp=self.temp+1
		# elif(self.ycoo == 2):
		# 	self.temp=self.temp-1

		# for i in range(10):
		# 	for j in range(50):
		# 		grid[self.ycoo+i][self.xcoo+j]=self.boss[i][j]
		if(self.temp%2==0):
			if(self.ycoo == 17):
				self.ycoo=self.ycoo-1
			elif(self.ycoo == 2):
				self.ycoo=self.ycoo+1
			if(player_ycoo<self.ycoo):
				self.ycoo=self.ycoo-1
			else:
				self.ycoo=self.ycoo+1
		self.temp=self.temp+1

		for i in range(10):
			for j in range(50):
				grid[self.ycoo+i][self.xcoo+j]=self.boss[i][j]

	def boss_balls(self,grid):
		grid[self.ycoo+7][self.xcoo-3] = 0
		self.balls.append((self.ycoo+7,self.xcoo-3))

	def balls_propagate(self,grid):
		for x,y in self.balls:
			grid[x][y]=" "
			if(y==0):
				self.balls.pop(self.balls.index((x,y)))
		self.balls=[(x,y-1) for x,y in self.balls]
		for x,y in self.balls:
			if(grid[x][y]==" "):
				grid[x][y]=0
