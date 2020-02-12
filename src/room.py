# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.description = description
        self.name = name

    def __str__(self):
        output = f'room name: {self.name}, room description: {self.description}'
        return output


class Nextroom(Room):
    def __init__(self, name, description, n_to, s_to, e_to, w_to):
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
    def __str__(self):
        output = f'room name: {self.name}, room description: {self.description}'
        return output
