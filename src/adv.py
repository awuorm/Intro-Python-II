from room import Room
from player import Player
import textwrap
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
# selection = 0
# REPL
# wrapper = textwrap.TextWrapper(width=50) 
# word_list = wrapper.wrap(text=value) 

player_outside = Player(room["outside"])
current_room = player_outside.room
print(f" \033[1;35;40m player is currently in {current_room} \n")
user_input = ""
while user_input == "":
    user_input = input("  \033[1;32;40m \n Type in your direction ")
    try:
        if user_input == "n" and current_room ==  Player(room["outside"]).room:
            player_outside = Player(room["outside"].n_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "n" and current_room ==  Player(room["foyer"]).room:
            player_outside = Player(room["foyer"].n_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "n" and current_room ==  Player(room["narrow"]).room:
            player_outside = Player(room["narrow"].n_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "s" and current_room ==  Player(room["foyer"]).room:
            player_outside = Player(room["foyer"].s_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "s" and current_room ==  Player(room["overlook"]).room:
            player_outside = Player(room["overlook"].s_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "s" and current_room ==  Player(room["treasure"]).room:
            player_outside = Player(room["treasure"].s_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "e" and current_room ==  Player(room["foyer"]).room:
            player_outside = Player(room["foyer"].e_to)
            current_room = player_outside.room
            print(f" \033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "w" and current_room ==  Player(room["narrow"]).room:
            player_outside = Player(room["narrow"].w_to)
            current_room = player_outside.room
            print(f"\033[1;33;40m player is currently in {current_room}  \n")
            user_input = ""
        elif user_input == "q":
            print("\033[1;34;40m --Game Over---Thankyou for playing--  \n")
        else:
            print(" \033[1;31;40m You have hit a wall, there is no room in this direction! Please enter you choice as either n,w,e or s  \n")
            user_input = ""
    except ValueError:
        print(' \033[1;35;40m You have hit a wall, there is no room in this direction! Please enter you choice as either n,w,e or s')
        user_input = ""
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
