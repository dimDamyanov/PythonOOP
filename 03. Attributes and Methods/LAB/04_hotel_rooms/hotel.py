from .room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for i in range(len(self.rooms)):
            if self.rooms[i].number == room_number:
                if self.rooms[i].take_room(people) != f'Room number {room_number} cannot be taken':
                    self.guests += people

    def free_room(self, room_number):
        for i in range(len(self.rooms)):
            if self.rooms[i].number == room_number:
                self.guests -= self.rooms[i].guests
                self.rooms[i].free_room()

    def print_status(self):
        print(f'Hotel {self.name} has {self.guests} total guests')
        print(f'Free rooms: {", ".join([str(room.number) for room in self.rooms if not room.is_taken])}')
        print(f'Taken rooms: {", ".join([str(room.number) for room in self.rooms if room.is_taken])}')
