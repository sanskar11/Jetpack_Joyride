import os
import time
import numpy as np
from colorama import Fore, Back, Style
# for i in range(30):
#     for j in range(100):
#         if i==1 or i==2:
#             print("X",end='')
#         if i==28 or i==29:
#             print("X",end='')
#     print("")


class Board:
	def __init__(self,rows,columns):
		self.rows=rows
		self.columns=columns
		self.grid=np.empty([self.rows,self.columns])
		self.boosttime=0
		# self.boost_time=0
		# self.sttime=time.time()

	def empty_board(self):
		self.grid=np.array([' ' for x in range(self.rows*self.columns)])
		self.grid=self.grid.reshape(self.rows,self.columns)

	def print_board(self,passtime,boost_time):
		# print(self.grid)
		# a=int(time.time()-self.sttime)*2
		# boosttime=0
		if(boost_time != 0):
			self.boosttime=passtime-boost_time
		# print("boosttime",self.boosttime)
		for i in range(self.rows):
			if(self.columns-(passtime+self.boosttime)<100):
				for j in range(self.columns-100,self.columns):
					if(self.grid[i][j]=='Z'):
						print(Fore.LIGHTBLACK_EX + self.grid[i][j],end='')
					elif(self.grid[i][j]=='|' or self.grid[i][j]=='/' or self.grid[i][j]=='\\' or self.grid[i][j]=='_'):
						print(Fore.YELLOW + self.grid[i][j],end='')
					elif(self.grid[i][j]==">"):
						print(Fore.LIGHTRED_EX + self.grid[i][j],end='')
					elif(self.grid[i][j]=="U" or self.grid[i][j]=="J" or self.grid[i][j]=="I"):
						print(Fore.RED + self.grid[i][j],end='')
					elif(self.grid[i][j]=="$"):
						print(Fore.GREEN + self.grid[i][j],end='')
					elif(self.grid[i][j]=="^" or self.grid[i][j]=="O"):
						print(Fore.BLUE + self.grid[i][j],end='')
					else:
						print(Fore.WHITE + self.grid[i][j],end='')
			else:
				for j in range(passtime+self.boosttime,passtime+self.boosttime+100):
					if(self.grid[i][j]=='Z'):
						print(Fore.LIGHTBLACK_EX + self.grid[i][j],end='')
					elif(self.grid[i][j]=='|' or self.grid[i][j]=='/' or self.grid[i][j]=='\\' or self.grid[i][j]=='_'):
						print(Fore.YELLOW + self.grid[i][j],end='')
					elif(self.grid[i][j]==">"):
						print(Fore.LIGHTRED_EX + self.grid[i][j],end='')
					elif(self.grid[i][j]=="U" or self.grid[i][j]=="J" or self.grid[i][j]=="I"):
						print(Fore.RED + self.grid[i][j],end='')
					elif(self.grid[i][j]=="$"):
						print(Fore.GREEN + self.grid[i][j],end='')
					elif(self.grid[i][j]=="^" or self.grid[i][j]=="O"):
						print(Fore.BLUE + self.grid[i][j],end='')
					else:
						print(Fore.WHITE + self.grid[i][j],end='')					
			print("")