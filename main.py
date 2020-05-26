from board import Board
from scene import Scene
from character import Main_person
from character import Character
from alarmexception import AlarmException
from getch import _getChUnix as getChar
from enemy import Boss
from colorama import Fore, Back, Style
import os
import signal
import random
import time
import numpy as np
import sys
obj1=Scene(30,300)
obj1.empty_board()
obj1.create_floor()
obj1.create_roof()
obj2=Character(26,1,5)
obj2.create_initial_character(obj1.grid)
# obj1.create_vertical_beam(19,15,7)
obj1.create_vertical_beam(5,100,7)
# obj1.create_vertical_beam(19,34,3)
obj1.create_right_beam(5,18,7)
obj1.create_right_beam(10,178,10)
obj1.create_right_beam(5,195,7)
obj1.create_left_beam(5,45,20)
obj1.create_horizontal_beam(5,35,25)
obj1.create_horizontal_beam(25,145,25)
obj1.create_coins(15,20,20)
obj1.create_coins(16,75,10)
obj1.create_coins(15,75,10)
obj1.create_coins(14,70,20)
obj1.create_coins(17,70,20)
obj1.create_coins(4,167,25)
obj1.create_coins(5,167,25)
obj1.create_coins(6,167,25)
obj1.create_coins(7,167,25)
# obj1.create_left_beam(7,250,19)
obj1.create_left_beam(7,115,19)
obj1.create_speedboost(12,130)
mag_y=np.random.randint(5,25)
mag_x=np.random.randint(5,150)
obj1.create_attractivemag(mag_y,mag_x)
obj3=Boss(10,250,3)
# obj3=Boss(10,75,3)
obj3.create_boss(obj1.grid)
a=np.random.randint(1,100)
if a<50:
	obj1.create_magnet(5,85)
sttime=time.time()
xcoo=26
ycoo=1
boost=0
down_speed=0
def check_shield(passtime):
	if(obj2.available_shield==False):
		
		if(60-int(passtime-obj2.time_shield_use)>50):
			obj2.shield_look(obj1.grid)
			print(Back.GREEN + "SHIELD ACTIVATED!!" + Style.RESET_ALL)
		else:
			obj2.protection=False
			obj2.remove_shield_look(obj1.grid)
			print("")
		if(passtime-obj2.time_shield_use>=60):
			obj2.available_shield=True
		print("Time left to refill shield", 60-int(passtime-obj2.time_shield_use))
	else:
		print(Back.LIGHTYELLOW_EX + Fore.RED + "SHIELD AVAILABLE...")
		print("Press Space to use the shield..." + Style.RESET_ALL)

def move_player():
	''' moves Mario'''
	def alarmhandler(signum, frame):
		''' input method '''
		raise AlarmException


	def user_input(timeout=0.15):
		''' input method '''
		signal.signal(signal.SIGALRM, alarmhandler)
		signal.setitimer(signal.ITIMER_REAL, timeout)
		
		try:
			text = getChar()()
			signal.alarm(0)
			return text
		except AlarmException:
			pass
		signal.signal(signal.SIGALRM, signal.SIG_IGN)
		return ''

	inp = user_input()
	if(inp == 'd' or inp == 'D'):
		if obj2.xcoo<passtime+obj1.boosttime+98:
			fd=obj2.check_forward(obj1.grid)
			if(fd==1):
				obj2.move_forward(obj1.grid)
				obj2.xcoo=obj2.xcoo+1
				obj2.down_speed=0
				if (obj2.ycoo < 26):
					dn=obj2.check_downward(obj1.grid)
					if(dn==1):
						obj2.move_downward(obj1.grid)

	elif(inp == 'a' or inp == 'A'):
		if obj2.xcoo > passtime-1:
			bk=obj2.check_backward(obj1.grid)
			if(bk==1):
				obj2.move_backward(obj1.grid)
				obj2.xcoo=obj2.xcoo-1
				if (obj2.ycoo < 26):
					dn=obj2.check_downward(obj1.grid)
					obj2.down_speed=0
					if(dn==1):
						obj2.move_downward(obj1.grid)
	
	elif(inp == 'w' or inp == 'W'):
		if obj2.ycoo > 2:
			up=obj2.check_upward(obj1.grid)
			if(up==1):
				obj2.move_upward(obj1.grid)
				if(obj2.ycoo==26):
					obj2.ycoo=obj2.ycoo-5
				else:
					obj2.ycoo=obj2.ycoo-1

	elif(inp == " "):
		if(obj2.available_shield==True):
			obj2.available_shield=False
			obj2.protection=True
			obj2.time_shield_use=passtime

	elif(inp == "f" or inp == "F"):
		obj2.bullets_fire()
		if (obj2.ycoo < 26):
			dn=obj2.check_downward(obj1.grid)
			if(dn==1):
				obj2.move_downward(obj1.grid)
		else:
			obj2.down_speed=0

	else:
		if (obj2.ycoo < 26):
			dn=obj2.check_downward(obj1.grid)
			if(dn==1):
				obj2.move_downward(obj1.grid)
		else:
			obj2.down_speed=0
	# elif(inp == 'b'):
		# return
	# print("Yeah this is being executed")
	# obj2.remove_shield_look(obj1.grid)

def win_message():
	os.system('tput reset')
	print("CONGRATULATIONS YOU WON")
	print("Final Scores")
	print (Back.GREEN + "Score=" + Style.RESET_ALL, obj2.score )
	print(Back.GREEN + "Coins=" + Style.RESET_ALL, obj2.coins)

def lose_message():
	os.system('tput reset')
	print("SORRY BETTER LUCK NEXT TIME!!")
	print("Final Scores")
	print (Back.GREEN + "Score=" + Style.RESET_ALL, obj2.score )
	print(Back.GREEN + "Coins=" + Style.RESET_ALL, obj2.coins)

while (1):
	os.system('tput reset')
	passtime=int(time.time()-sttime)
	remaintime=400-passtime
	print(Back.RED + "Time Remaining=",remaintime)

	if(remaintime==0 or obj2.life==0):
		lose_message()
		break
	
	print (Back.GREEN + "Score=" + Style.RESET_ALL, obj2.score )
	print(Back.GREEN + "Coins=" + Style.RESET_ALL, obj2.coins)
	print(Back.GREEN + "Lives=" + Style.RESET_ALL, obj2.life)

	obj2.create_character(obj1.grid)
	check_shield(passtime)

	# if(obj2.boost==False):
		# obj1.print_board(passtime)
	if(obj2.boost==True and boost == 0):
		boost=passtime
		# obj1.boost_time=passtime
	if(obj2.boost==True):
		print("YOU HAVE TAKEN THE BOOST, SPEED OF THE BOARD INCREASED!!")
	else:
		print("")
		# obj1.boost_time=time.time()
		# obj1.print_board(passtime*2)
	# print(obj1.boost_time)


	hit=obj2.bullets_propagation(obj1.grid,passtime,obj1.boosttime)
	if(hit==3):
		obj3.life=obj3.life-1
	if(obj3.life==0):
		win_message()
		break
	# print(obj2.bullets)

	obj3.move_boss(obj1.grid,obj2.ycoo,obj2.xcoo)
	if(passtime+obj1.boosttime<200):
		if(obj2.xcoo<passtime+obj1.boosttime+1):
			obj2.move_forward(obj1.grid)
			obj2.xcoo=obj2.xcoo+1
	else:
		if(obj2.xcoo<200):
			obj2.move_forward(obj1.grid)
			obj2.xcoo=obj2.xcoo+1

	if(passtime+obj1.boosttime>150):
		if(passtime%5==0):
			obj3.boss_balls(obj1.grid)
		obj3.balls_propagate(obj1.grid)
		print(Back.MAGENTA + "BOSS HEALTH=" + Style.RESET_ALL,obj3.life)
	else:
		print("")
	if(obj2.magnet==True):
		if(obj2.time_magnet_use==0):
			obj2.time_magnet_use=passtime
		if(passtime-obj2.time_magnet_use<10):
			print("YOU HAVE COIN MAGNET available for !!", 10-(passtime-obj2.time_magnet_use))
			obj2.coin_magnet(obj1.grid)
		else:
			obj2.magnet=False
			obj2.time_magnet_use=0
			print("")
	else:
		print("")

	print("")

	obj1.print_board(passtime,boost)
	# print(obj2.xcoo,obj2.ycoo)
	check_mag=obj2.attractive_mag(obj1.grid,mag_y,mag_x)
	if (check_mag>0):
		if(check_mag==2):
			if obj2.xcoo<passtime+obj1.boosttime+98:
				fd=obj2.check_forward(obj1.grid)
				if(fd==1):
					obj2.move_forward(obj1.grid)
					obj2.xcoo=obj2.xcoo+1
					obj2.down_speed=0
		elif(check_mag==1):
			if obj2.xcoo > passtime-1:
				bk=obj2.check_backward(obj1.grid)
				if(bk==1):
					obj2.move_backward(obj1.grid)
					obj2.xcoo=obj2.xcoo-1
	check_mag=0
	move_player()
	print(obj1.boosttime)
	sys.stdout.flush()

