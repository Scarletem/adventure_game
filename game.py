"""
Adventure Game Base Code
CS102
"""

import sys
from commands import *

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
	print(sys.version)

	# Initialize Game State

	# TODO: Create a Room() instance and assign it to current room

	while(not GAMEOVER):
		# Get Command from the player
		command = input(">>> ").rstrip()

		if command == 'look':
				# TODO: You may need to change the arguments that look_command() takes
				look_command()
		else:
			print(f"{command} is not a valid command. Please try a valid command.\n")
			continue

