Report

1. First I started by making a grid with a top and a bottom.
	
	The code I used in this is to make a board is contained in the board.py inside the Class Board.

	def empty_board(self): Used to make an empty board by initialising the empty array.
	Now I planned to just display this array in such a manner as to give it a moving feeling.

	def print_board(): Used to print board again and again as our board moves 1 cell each second and when boost is taken it moves by 2 cells per second. Function colorama is used to give the color.

2. In scene.py:
	
	def create_floor is used to create a floor by using character "Z".

	def create_roof is used to create a roof by using character "Z".

	Obstacles are created by the following functions:

	def create_vertical_beam(self,yco,xco,le): For vertical beam

	def create_right_beam(self,yco,xco,le): For right inclined beam

	def create_left_beam(self,yco,xco,le): For left inclined beam

	def create_horizontal_beam(self,yco,xco,le): For horizontal beam

	Coins are created by:

	def create_coins()

	Speed boost is created by:

	def create_speedboost()

	Attractive magnet is created by:

	def create_attractivemag()

3. Movement:

	The movement of the characted is covered in character.py in an inherited class Character inherited from class Main_person().

	def check_upward(),check_downward(),check_left(),check_right() are the functions that wheather movement is possible in upward, downward, left and right direction respectively. It also checks collinsion with firebeams and boss snow balls and decreased the health of the player accordingly.

	Now if movement is possible then move_upward(), move_downward(), move_left(), move_right() is used to move the character in upward, downward, left and right direction. An acceleration effect is created when moving downward.


4. Bullets: 

	def bullets_fire() is used to create a bullets and it pushes the current coordinates of the character in a list bullets.

	def bullets_propagtion() is used to create a make bullets move forward. It also check the collision with fire beams and destroys the fire beams on coming in contact with it. Moreove it also checks collision with the boss.

5. Shield:

	def shield_look() is used to create a shield oh the player.

	def remove_shield_look() is used to remove the shield when the shield time expires.

	def check_shield() in main.py is used to make shield last for 10 sec.

6. Boss: boss in coded in enemy.py in the class Boss with is inherited from class Main_person().

	def create_boss(): Used to create dragon which has an ascii art in file dragon in the folder.

	def move_boss(): Used to give boss the upward and downward movement.

	def boss_balls(): Used to create snow balls of the boss and pusshes the current location of the boss in a list balls.

	def balls_propagate(): Used to make balls move forward.

7. def attractive_mag() checks the precense of the magnet "M" near the player and moves his x coordinates accordingly.

8. def move_player() is used to take user input and act according to the pressed keys.

	def win_message() and def lose_message() is used to print win and lose message respectively. Library colorama is used to give the color.

9. getch.py is used to take asynchronous input.