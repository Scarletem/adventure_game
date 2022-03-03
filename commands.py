"""
This file contains logic for "Commands" that will be used in Adventure Game.
"""

"""
Look Command:

usage: look

Allows the player to 'look' around the room. This function should print a description
of the room to the player's terminal.
"""
from hashlib import new


def look_command(room):
    print(room.get_description())
    return None

"""
Look Command:

usage: go <direction>

Allows the player to go to another room. This function should move the player in the direction
they indicated. If there is no room in that direction, do not move the player and print to 
the user that the player has not moved. If there is a room, move the player to that room and 
print a message indicating the player has moved.

This function should return the ROOM OBJECT of the new room.
"""
def go_command(room_map, current_room, direction):
    # TODO: Implement Go Command
    print(f"I got told to go {direction}.")

    new_room = room_map[current_room.get_name()][direction] 

    if new_room == None:
        print(f"This is a dead end, where are you going?")
        return current_room
    else:
        return new_room 