from room import Room
from player import Player
from item import Item
import textwrap

# Declare items in rooms

item = {
    'outside': [Item("spear", "stabbing your foe"), Item("ointment", "mosquito bites")],
    'foyer': [Item("swing", "resting your tired feet"), Item("rug", "wrapping a dead body")],
    "overlook": [Item("rope", "climbing up the cliff"), Item("flashlight", "lighting your way up the steep climb")],
    "narrow": [Item("wheelbarrow", "carrying you or your new fortune?"), Item("shovel", "digging yourself into boundless treasures")],
    "treasure": [Item("compass", "finding your way home"), Item("map", "continuing in the treasure hunt")],
}

# Declare Items to be picked
pickeditem = {
    "default": Item("coins", "buying something important"),
    'spear': Item("spear", "stabbing your foe"),
    'ointment': Item("ointment", "mosquito bites"),
    'swing': Item("swing", "resting your tired feet"),
    "rug": Item("rug", "wrapping a dead body"),
    "rope": Item("rope", "climbing up the cliff"),
    "flashlight": Item("flashlight", "lighting your way up the steep climb"),
    "wheelbarrow": Item("wheelbarrow", "carrying you or your new fortune?"),
    "shovel": Item("shovel", "digging yourself into boundless treasures"),
    "compass": Item("compass", "finding your way home"),
    "map": Item("map", "continuing in the treasure hunt"),
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", item["outside"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", item["foyer"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", item["overlook"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", item["narrow"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", item["treasure"]),
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


# initialize Player
player_outside = Player("Mildred", room["outside"], pickeditem["default"])
current_room = player_outside.room
current_player = player_outside.name
current_items = player_outside.item
print(
    f" \033[1;35;40m {player_outside.__str__()} \n")

# REPL
user_input = ""
pick_items = "default"
playeritems = []
roomname = "outside"
takeordrop = ""


def displayusercommand(user_input, roomname):
    print("You can pick the available items in this room")
    user_input = input(
        "  \033[1;32;40m \n Enter your command ")
    itemslist = user_input.split(" ")
    takeordrop = itemslist[0]
    def userpicksitems(itemslist):
        if(len(itemslist) == 1):
            print(f" \033[1;31;40m Wrong command, use [verb] [object] format")
            user_input = "q"
        else:
            playeritems.append(itemslist[1])
            pick_items = itemslist[1]
            print(
                f" \033[1;33;40m {itemslist[1]} has been added to your arsenal. You have {len(playeritems)} items in your arsenal\n")
            return pick_items
    def removeitem(pick_items, roomname):
        pick_items = itemslist[1]
        takeordrop = itemslist[0]
        print(f"take {takeordrop}")
        if roomname == "outside" or "foyer" or "overlook" or "narrow" or "treasure" and pick_items == "spear" or "swing" or "rope" or "wheelbarrow" or "compass" and len(item[roomname]) == 2 and takeordrop == "get" or "take":
            item[roomname].remove(item[roomname][0])
        elif roomname == "outside" or "foyer" or "overlook" or "narrow" or "treasure" and pick_items == "spear" or "swing" or "rope" or "wheelbarrow" or "compass" or "ointment" or "rug" or "flashlight" or "shovel" or "map" and len(item[roomname]) == 1 and takeordrop == "get" or "take":
            item[roomname].remove(item[roomname][0])
        elif roomname == "outside" or "foyer" or "overlook" or "narrow" or "treasure" and pick_items == "ointment" or "rug" or "flashlight" or "shovel" or "map" or "spear" or "swing" or "rope" or "wheelbarrow" or "compass" and len(item[roomname]) == 2  and takeordrop == "get" or "take":
            item[roomname].remove(item[roomname][1])
        # elif roomname == "outside" or "foyer" or "overlook" or "narrow" or "treasure" and pick_items == "spear" or "swing" or "rope" or "wheelbarrow" or "compass" or "ointment" or "rug" or "flashlight" or "shovel" or "map" and takeordrop == "drop":
        #     item[roomname].append(pickeditem[pick_items])
        #     print(f" dropped item {item[roomname]}")
        #     playeritems.remove(pick_items)
        else:
            print("Please provide the correct item name to take from the room")
    #     print(f" dropped {takeordrop}")
    # elif  takeordrop == "drop":
    #     print(f" dropped is working {takeordrop}")
    def additem(pick_items, roomname):
        pick_items = itemslist[1]
        takeordrop = itemslist[0]
        print(f"dropped {takeordrop}")
        if roomname == "outside" or "foyer" or "overlook" or "narrow" or "treasure" and pick_items == "spear" or "swing" or "rope" or "wheelbarrow" or "compass" or "ointment" or "rug" or "flashlight" or "shovel" or "map" and takeordrop == "drop":
            item[roomname].append(pickeditem[pick_items])
            print(f" dropped item {item[roomname]}")
            playeritems.remove(pick_items)
        else:
            print("Please provide the correct item name to drop")
    if takeordrop == "drop":
        print("drop is working")
        additem(pick_items,roomname)
    else:
        print("take is working")
        removeitem(pick_items, roomname)
    userpicksitems(itemslist)


while user_input == "":
    user_input = input("  \033[1;32;40m \n Enter your command ")
    try:
        if len(user_input.split(" ")) == 1 and user_input == "n" and current_room == Player("Mildred", room["outside"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["outside"].n_to, pickeditem[f"{pick_items}"])
            roomname = "outside"
            displayusercommand(user_input, roomname)
            print(f" \033[1;33;40m {player_outside.__str__()}\n")
            current_room = player_outside.room
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "n" and current_room == Player("Mildred", room["foyer"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["foyer"].n_to, pickeditem[f"{pick_items}"])
            roomname = "foyer"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "n" and current_room == Player("Mildred", room["narrow"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["narrow"].n_to, pickeditem[f"{pick_items}"])
            roomname = "narrow"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "s" and current_room == Player("Mildred", room["foyer"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["foyer"].s_to, pickeditem[f"{pick_items}"])
            roomname = "foyer"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "s" and current_room == Player("Mildred", room["overlook"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["overlook"].s_to, pickeditem[f"{pick_items}"])
            roomname = "overlook"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "s" and current_room == Player("Mildred", room["treasure"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["treasure"].s_to, pickeditem[f"{pick_items}"])
            roomname = "treasure"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "e" and current_room == Player("Mildred", room["foyer"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["foyer"].e_to, pickeditem[f"{pick_items}"])
            roomname = "foyer"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "w" and current_room == Player("Mildred", room["narrow"], pickeditem[f"{pick_items}"]).room:
            player_outside = Player(
                "Mildred", room["narrow"].w_to, pickeditem[f"{pick_items}"])
            roomname = "narrow"
            displayusercommand(user_input, roomname)
            current_room = player_outside.room
            print(
                f" \033[1;33;40m {player_outside.__str__()} \n")
            user_input = ""
        elif len(user_input.split(" ")) == 1 and user_input == "q":
            print("\033[1;34;40m --Game Over---Thankyou for playing--  \n")
        else:
            print(
                " \033[1;31;40m You have hit a wall, there is no room in this direction! Please enter you choice as either n,w,e or s  \n")
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
