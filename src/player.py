# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, item):
        self.name = name
        self.room = room
        self.item = item

    def __str__(self):
        output = ''
        add_items = []
        add_items.append(self.item)
        output += f'Player {self.name}  is in {self.room}.'
        return output
