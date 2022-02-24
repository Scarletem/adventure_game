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
	start_room = Room("room_start", "A Lab Room")

	# Set Starting Room
	CURRENT_ROOM = start_room

	# TODO: Create Additional Rooms

	# Add Initial Room to Map
	GAME_MAP[start_room.get_name()] = {
		"object": start_room,
		"north": None,
		"south": None, 
		"east": None,
		"west": None
	}

	# TODO: Add Rooms to the Game Map

	while(not GAMEOVER):
		# Get Command from the player
		command_list = input(">>> ").rstrip().split(" ")
		command = command_list[0]

		if command == 'look':
			look_command(CURRENT_ROOM)
		elif command == 'go':
			direction = command_list[1]
			go_command(GAME_MAP, direction)
		else:
			print(f"{command} is not a valid command. Please try a valid command.\n")
			continue

