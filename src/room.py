# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, item):
        self.description = description
        self.name = name
        self.item = item

    def __str__(self):
        output = ''
        output += f'room name: {self.name}, room description: {self.description}. The room has {len(self.item)} items.'
        item_number = 1
        for i in self.item:
            output += f' \n The {self.name} has item name: {i.name}, it can be used for {i.description}\n'
            item_number += 1
        return output


# class Nextroom(Room):
#     def __init__(self, name, description, n_to, s_to, e_to, w_to):
#         self.n_to = n_to
#         self.s_to = s_to
#         self.e_to = e_to
#         self.w_to = w_to
#     def __str__(self):
#         output = f'room name: {self.name}, room description: {self.description}'
#         return output
