
class Room:
    def __init__(self, color):
        self.color = color
        self.doors = []

    def add_door(self, room, direction):
        self.doors.append(Door(room, direction))


class Door:
    def __init__(self, room, direction):
        self.destination = room
        self.direction = direction


class Zork:
    def __init__(self):
        self.rooms = {}
        self.create_rooms()
        self.create_doors()

    def create_rooms(self):
        colors = ['while', 'blue', 'red', 'yellow', 'green']
        for color in colors:
            self.rooms[color] = Room(color)    

    def create_doors(self):
        self.rooms['white'].add_door(self.rooms['blue'], 'east')
        self.rooms['blue'].add_door(self.rooms['white'], 'west')
        self.rooms['blue'].add_door(self.rooms['yellow'], 'south')
        self.rooms['yellow'].add_door(self.rooms['blue'], 'north')
        self.rooms['yellow'].add_door(self.rooms['red'], 'south')
        self.rooms['red'].add_door(self.rooms['yellow'], 'north')
        self.rooms['red'].add_door(self.rooms['green'], 'west')
        self.rooms['green'].add_door(self.rooms['red'], 'east')