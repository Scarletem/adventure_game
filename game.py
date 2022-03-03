"""
Adventure Game Base Code
CS102
"""

import sys
from commands import *
from room import *

# Controls Game Infinite Loop
GAMEOVER = False

# Global State
#
# Structure: Dict: {room_name: {object: Room Object, north: room_name, east: room_name, south:room_name, west: room_name}}
GAME_MAP = {}
CURRENT_ROOM = None

def print_intro():
	print(f"""#########################\n
	Welcome to Adventure Game!\n
	#########################""")

if __name__ == "__main__":

	# Print Game Intro Message
	print_intro()

	# Initialize Game Map
	start_room = Room("room_start", "Your eyes slowly open to find yourself in a strange room. It is in what appears to be an old house. The room has white paint chipping off the walls with blacked out windows and two solitary pieces of furniture, a desk and a bed which you are currently laying on. You stand from the bed and start to walk towards the desk. Once you arrive in front of it, you notice the ratty piece of paper with blotted out ink spelling out six words 'Welcome to The Palace, Good Luck' Good Luck? What's that supposed to mean? You wonder as you make your way to the door, unaware of the multiple pairs of eyes watching you from the walls of The Palace.")

	# Set Starting Room
	CURRENT_ROOM = start_room

	# TODO: Create Additional Rooms
	room_op_1 = Room("The OR", "You turn to open the door to the west and arrive in a room splattered in blood. It appears to have been an old operating room; it had several different sized knives, many lights hanging from the ceiling, and one lone table right in the middle of it. You walk towards the table to find another piece of paper written in blotted ink. On it are, once again, six words, 'Strike One, three strikes, you're out.'")

	room_op_2 = Room("Annabell", "This room contains a terrifying number of hairless dolls.")

	room_op_3 = Room("The Carnival", "This room has an insane number of knives and swords stuck in the walls, like a demented carnival trick.")

	room_op_4 = Room("Surprise", "Looking inside this room, it has a number of cardboard boxes each containing a different object.")

	# Add Initial Room to Map
	GAME_MAP[start_room.get_name()] = {
		"north": room_op_3,
		"south": room_op_2, 
		"east": room_op_4,
		"west": room_op_1
	}

	# TODO: Add Rooms to the Game Map
	GAME_MAP[room_op_1.get_name()] = {
		"north": None,
		"south": None, 
		"east": start_room,
		"west": None
	}

	while(not GAMEOVER):
		# Get Command from the player
		command_list = input(">>> ").rstrip().split(" ")
		command = command_list[0]

		if command == 'look':
			look_command(CURRENT_ROOM)
		elif command == 'go':
			direction = command_list[1]
			CURRENT_ROOM = go_command(GAME_MAP, CURRENT_ROOM, direction)
		else:
			print(f"{command} is not a valid command. Please try a valid command.\n")
			continue

