from board import Board
from scene import Scene
import numpy as np
import os

class Main_person:
	def __init__(self,ycoo,xcoo,life):
		self.xcoo = xcoo
		self.ycoo = ycoo
		self.life=life

class Character(Main_person):

	def __init__(self,ycoo,xcoo,life):
		Main_person.__init__(self,ycoo,xcoo,life)
		self.__shape= [ ['I','O'],['J','^']]
		self.allowed_collision=[" ","$","U","B",">"]
		self.coins=0
		self.die=0
		self.protection=False
		self.magnet=False
		self.boost=False
		self.available_shield=True
		self.time_shield_use=0
		self.bullets=[]
		self.score=0
		self.time_magnet_use=0
		self.down_speed=0
		self.attractive_magnet=0

	def create_initial_character(self,grid):
		for i in range(26,28):
			for j in range(1,3):
				grid[i][j] = self.__shape[i-26][j-1]

	def create_character(self,grid):
		grid[self.ycoo][self.xcoo]='I'
		grid[self.ycoo+1][self.xcoo]='J'
		grid[self.ycoo][self.xcoo+1]='O'
		grid[self.ycoo+1][self.xcoo+1]='^'

	def move_forward(self,grid):
		grid[self.ycoo][self.xcoo+2]=grid[self.ycoo][self.xcoo+1]
		grid[self.ycoo][self.xcoo+1]=grid[self.ycoo][self.xcoo]
		grid[self.ycoo+1][self.xcoo+2]=grid[self.ycoo+1][self.xcoo+1]
		grid[self.ycoo+1][self.xcoo+1]=grid[self.ycoo+1][self.xcoo]
		grid[self.ycoo][self.xcoo]=" "
		grid[self.ycoo+1][self.xcoo]=" "

	def move_backward(self,grid):
		grid[self.ycoo][self.xcoo-1]=grid[self.ycoo][self.xcoo]
		grid[self.ycoo][self.xcoo]=grid[self.ycoo][self.xcoo+1]
		grid[self.ycoo+1][self.xcoo-1]=grid[self.ycoo+1][self.xcoo]
		grid[self.ycoo+1][self.xcoo]=grid[self.ycoo+1][self.xcoo+1]
		grid[self.ycoo][self.xcoo+1]=" "
		grid[self.ycoo+1][self.xcoo+1]=" "

	def move_upward(self,grid):
		if(self.ycoo==26):
			grid[self.ycoo-5][self.xcoo]=grid[self.ycoo][self.xcoo]
			grid[self.ycoo-5][self.xcoo+1]=grid[self.ycoo][self.xcoo+1]
			grid[self.ycoo-4][self.xcoo]=grid[self.ycoo+1][self.xcoo]
			grid[self.ycoo-4][self.xcoo+1]=grid[self.ycoo+1][self.xcoo+1]
			grid[self.ycoo+1][self.xcoo+1]=" "
			grid[self.ycoo+1][self.xcoo]=" "
			grid[self.ycoo][self.xcoo+1]=" "
			grid[self.ycoo][self.xcoo]=" "
		else:
			grid[self.ycoo-1][self.xcoo]=grid[self.ycoo][self.xcoo]
			grid[self.ycoo-1][self.xcoo+1]=grid[self.ycoo][self.xcoo+1]
			grid[self.ycoo][self.xcoo]=grid[self.ycoo+1][self.xcoo]
			grid[self.ycoo][self.xcoo+1]=grid[self.ycoo+1][self.xcoo+1]
			grid[self.ycoo+1][self.xcoo+1]=" "
			grid[self.ycoo+1][self.xcoo]=" "

	def move_downward(self,grid):
		if(self.ycoo+2+self.down_speed>27):
			grid[27][self.xcoo]=grid[self.ycoo+1][self.xcoo]
			grid[27][self.xcoo+1]=grid[self.ycoo+1][self.xcoo+1]
			grid[26][self.xcoo]=grid[self.ycoo][self.xcoo]
			grid[26][self.xcoo+1]=grid[self.ycoo][self.xcoo+1]
			grid[self.ycoo][self.xcoo+1]=" "
			grid[self.ycoo][self.xcoo]=" "
			if(self.down_speed>=1):
				grid[self.ycoo+1][self.xcoo+1]=" "
				grid[self.ycoo+1][self.xcoo]=" "
			self.ycoo=26
		else:
			grid[self.ycoo+2+self.down_speed][self.xcoo]=grid[self.ycoo+1][self.xcoo]
			grid[self.ycoo+2+self.down_speed][self.xcoo+1]=grid[self.ycoo+1][self.xcoo+1]
			grid[self.ycoo+1+self.down_speed][self.xcoo]=grid[self.ycoo][self.xcoo]
			grid[self.ycoo+1+self.down_speed][self.xcoo+1]=grid[self.ycoo][self.xcoo+1]
			grid[self.ycoo][self.xcoo+1]=" "
			grid[self.ycoo][self.xcoo]=" "
			if(self.down_speed>=1):
				grid[self.ycoo+1][self.xcoo+1]=" "
				grid[self.ycoo+1][self.xcoo]=" "
			self.ycoo=self.ycoo+1+self.down_speed
			self.down_speed=self.down_speed+1
			print("Lets go down")

	def check_forward(self,grid):
		if (grid[self.ycoo][self.xcoo+2] in self.allowed_collision and grid[self.ycoo+1][self.xcoo+2] in self.allowed_collision):
			# if (grid[self.ycoo][self.xcoo+5] == "$" or grid[self.ycoo+1][self.xcoo+5] == "$" and self.magnet == True):
			# 	self.coins=self.coins+1
			# 	grid[self.ycoo][self.xcoo+5] = " "
			# 	grid[self.ycoo+1][self.xcoo+5] = " "

			if(grid[self.ycoo][self.xcoo+3]==")" and grid[self.ycoo+1][self.xcoo+3]==")"):
				grid[self.ycoo][self.xcoo+3]=" "
				grid[self.ycoo+1][self.xcoo+3]=" "


			if (grid[self.ycoo][self.xcoo+2] == "$" and self.magnet == False):
				self.coins=self.coins+1
				if(grid[self.ycoo+1][self.xcoo+2] == "$" and self.magnet == False):
					self.coins=self.coins+1
			elif(grid[self.ycoo+1][self.xcoo+2] == "$" and self.magnet == False):
					self.coins=self.coins+1
			elif (grid[self.ycoo][self.xcoo+2] == "U" or grid[self.ycoo+1][self.xcoo+2] == "U"):
				self.magnet=True
			elif (grid[self.ycoo][self.xcoo+2] == "B" or grid[self.ycoo+1][self.xcoo+2] == "B"):
				self.boost=True
			return 1
		else:
			if(self.protection==False):
				self.life=self.life-1
			return 2
		# elif(grid[self.ycoo])
		# elif ()

	def check_backward(self,grid):
		if (grid[self.ycoo][self.xcoo-1] in self.allowed_collision and grid[self.ycoo+1][self.xcoo-1] in self.allowed_collision):
			# if (grid[self.ycoo][self.xcoo-4] == "$" or grid[self.ycoo+1][self.xcoo-4] == "$" and self.magnet == True):
			# 	self.coins=self.coins+1
			# 	grid[self.ycoo][self.xcoo-4] = " "
			# 	grid[self.ycoo+1][self.xcoo-4] = " "

			if(grid[self.ycoo][self.xcoo+3]==")" and grid[self.ycoo+1][self.xcoo+3]==")"):
				grid[self.ycoo][self.xcoo+3]=" "
				grid[self.ycoo+1][self.xcoo+3]=" "

			if (grid[self.ycoo][self.xcoo-1] == "$" and self.magnet == False):
				self.coins=self.coins+1
				if(grid[self.ycoo+1][self.xcoo-1] == "$" and self.magnet == False):
					self.coins=self.coins+1
			elif(grid[self.ycoo+1][self.xcoo-1] == "$" and self.magnet == False):
					self.coins=self.coins+1
			elif (grid[self.ycoo][self.xcoo-1] == "U" or grid[self.ycoo+1][self.xcoo-1] == "U"):
				self.magnet=True
			elif (grid[self.ycoo][self.xcoo-1] == "B" or grid[self.ycoo+1][self.xcoo-1] == "B"):
				self.boost=True
			return 1
		else:
			if(self.protection==False):
				self.life=self.life-1
			return 2

	def check_upward(self,grid):
		if (grid[self.ycoo-1][self.xcoo] in self.allowed_collision and grid[self.ycoo-1][self.xcoo+1] in self.allowed_collision):
			# if (grid[self.ycoo - 4 ][self.xcoo] == "$" and self.magnet == True):
			# 	self.coins=self.coins+1
			# 	grid[self.ycoo - 4][self.xcoo] = " "
			# 	if(grid[self.ycoo-4][self.xcoo+1] == "$"):
			# 		self.coins=self.coins+1
			# 		grid[self.ycoo - 4][self.xcoo+1] = " "

			# if (grid[self.ycoo+1][self.xcoo+3]==")" and grid[self.ycoo][self.xcoo+3]==")"):
			# 	grid[self.ycoo+1][self.xcoo+3]=" "
			# 	grid[self.ycoo][self.xcoo+3]=" "

			if (grid[self.ycoo-1][self.xcoo] == "$" and self.magnet == False):
				self.coins=self.coins+1
				if(grid[self.ycoo-1][self.xcoo+1] == "$"):
					self.coins=self.coins+1
			elif (grid[self.ycoo-1][self.xcoo+1] == "$" and self.magnet == False):
					self.coins=self.coins+1			
			elif (grid[self.ycoo-1][self.xcoo] == "U" or grid[self.ycoo-1][self.xcoo+1] == "U"):
				self.magnet=True
			elif (grid[self.ycoo-1][self.xcoo] == "B" or grid[self.ycoo-1][self.xcoo+1] == "B"):
				self.boost=True
			return 1
		else:
			if(self.protection==False):
				self.life=self.life-1
			return 2

	def check_downward(self,grid):
		if(grid[self.ycoo+2][self.xcoo] in self.allowed_collision and grid[self.ycoo+2][self.xcoo+1] in self.allowed_collision):
			# if(self.magnet == True):
			# 	if(self.ycoo+7 < 30):
			# 		for i in range(1,7):#problematic_code
			# 			if (grid[self.ycoo + i ][self.xcoo] == "$"  and self.magnet == True):
			# 				self.coins=self.coins+1
			# 				grid[self.ycoo + i][self.xcoo] = " "
			# 				if(grid[self.ycoo + i][self.xcoo+1] == "$"):
			# 					self.coins=self.coins+1
			# 					grid[self.ycoo + i][self.xcoo+1] = " "
			

			# if (grid[self.ycoo][self.xcoo+3]==")"):
			# 	grid[self.ycoo][self.xcoo+3]=" "



			if (grid[self.ycoo+2][self.xcoo] == "$"  and self.magnet == False):
				self.coins=self.coins+1
				if(grid[self.ycoo+2][self.xcoo+1] == "$"):
					self.coins=self.coins+1
			elif (grid[self.ycoo+2][self.xcoo+1] == "$" and self.magnet == False):
				self.coins=self.coins+1
			elif (grid[self.ycoo+2][self.xcoo] == "U" or grid[self.ycoo+2][self.xcoo+1] == "U"):
				self.magnet=True
			elif (grid[self.ycoo+2][self.xcoo] == "B" or grid[self.ycoo+2][self.xcoo+1] == "B"):
				self.boost=True
			return 1
		else:
			if(self.protection==False):
				self.life=self.life-1
			return 2

	def bullets_fire(self):
		self.bullets.append((self.ycoo,self.xcoo+2))

	def bullets_propagation(self,grid,passtime,boosttime):
		for x,y in self.bullets:
			grid[x][y]=" "
		self.bullets=[(x,y+1) for x,y in self.bullets]
		for x,y in self.bullets:
			if y>298:
				grid[x][y]=" "
				self.bullets.pop(self.bullets.index((x,y)))
			else:
				if y < passtime+100+boosttime:
					if grid[x][y] in self.allowed_collision:
						grid[x][y-1] = grid[x][y]
						grid[x][y]=">"
						# return 1
					else:
						if (grid[x][y]=="|" or grid[x][y]=="\\" or grid[x][y]=="/" or grid[x][y]=="_"):
							# print("COLLIDED!! at ",x,y)
							self.score=self.score+3
							# print(grid[x][y])
							grid[x][y]=" "
							self.bullets.pop(self.bullets.index((x,y)))
							# return 2
						else:
							self.bullets.pop(self.bullets.index((x,y)))
							self.score=self.score+20
							return 3
				else:
					grid[x][y]=" "
					self.bullets.pop(self.bullets.index((x,y)))

	def coin_magnet(self,grid):
		if(self.ycoo-5>0):
			if(self.ycoo+7<30):
				for i in range(self.xcoo-5,self.xcoo+7):
					for j in range(self.ycoo-5,self.ycoo+7):
						if grid[j][i]=="$":
							grid[j][i]=" "
							self.coins=self.coins+1
			else:
				for i in range(self.xcoo-5,self.xcoo+7):
					for j in range(self.ycoo-5,30):
						if grid[j][i]=="$":
							grid[j][i]=" "
							self.coins=self.coins+1
		else:
			for i in range(self.xcoo-5,self.xcoo+7):
				for j in range(4,self.ycoo+7):
					if grid[j][i]=="$":
						grid[j][i]=" "
						self.coins=self.coins+1

	def shield_look(self,grid):
		grid[self.ycoo][self.xcoo+1]=")"
		grid[self.ycoo+1][self.xcoo+1]=")"

	def remove_shield_look(self,grid):
		# if(grid[self.ycoo][self.xcoo+3]==")"):
		# 	grid[self.ycoo][self.xcoo+3]==" "
		# if(grid[self.ycoo+1][self.xcoo+3]==")"):
		# 	grid[self.ycoo+1][self.xcoo+3]=" "
		# if(grid[self.ycoo-1][self.xcoo+3]==")"):
		# 	grid[self.ycoo-1][self.xcoo+3]=" "
		# if(grid[self.ycoo][self.xcoo+4]==")"):
		# 	grid[self.ycoo][self.xcoo+4]=" "
		grid[self.ycoo][self.xcoo+1]="O"
		grid[self.ycoo+1][self.xcoo+1]="^"

	def attractive_mag(self,grid,mag_y,mag_x):
		# for check_x in range(-9,0):
		# 	for check_y in range(-3,4):
		# 		if(grid[self.ycoo+check_y,self.xcoo+check_x]=="M"):
		# 			if(self.xcoo<= 21):
		# 				return 3
		# 			return 1
		# for check_x in range(0,10):
		# 	for check_y in range(-3,4):
		# 		if(grid[self.ycoo,self.xcoo+check_x]=="M" or grid[self.ycoo+1,self.xcoo+check_x]=="M" ):
		# 			if(self.xcoo>= 18):
		# 				return 3
		# 			return 2
		# return 0
		if(self.xcoo>(mag_x-20) and self.xcoo<mag_x and self.attractive_magnet%2==0):
			self.attractive_magnet=self.attractive_magnet+1
			return 2
		elif(self.xcoo<(mag_x+20) and self.xcoo>mag_x and self.attractive_magnet%2==0):
			self.attractive_magnet=self.attractive_magnet+1
			return 1
		else:
			self.attractive_magnet=self.attractive_magnet+1
			return 3

