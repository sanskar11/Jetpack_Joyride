from board import Board
import numpy as np
from colorama import Fore, Back, Style
class Scene(Board):
	def __init__(self,rows,columns):
		Board.__init__(self,rows,columns)

	def create_floor(self):
		self.grid[-1]=np.array(['Z' for x in self.grid[-1]])
		self.grid[-2]=np.array(['Z' for x in self.grid[-1]])

	def create_roof(self):
		self.grid[0]=np.array(['Z' for x in self.grid[0]])
		self.grid[1]=np.array(['Z' for x in self.grid[1]])

	def create_vertical_beam(self,yco,xco,le):
		for i in range(le):
			self.grid[yco+i][xco]='|'

	def create_right_beam(self,yco,xco,le):
		# cons=yco+xco
		for i in range(le):
			self.grid[yco+i][xco-i]="/"

	def create_left_beam(self,yco,xco,le):
		for i in range(le):
			self.grid[yco+i][xco+i]="\\"

	def create_horizontal_beam(self,yco,xco,le):
		for i in range(le):
			self.grid[yco][xco+i]="_"
	
	def create_coins(self,yco,xco,le):
		for i in range(le):
			self.grid[yco][xco+i]="$"

	def create_magnet(self,yco,xco):
		self.grid[yco][xco]="U"

	def create_speedboost(self,yco,xco):
		self.grid[yco][xco]="B"

	def create_attractivemag(self,yco,xco):
		self.grid[yco][xco]="M"
