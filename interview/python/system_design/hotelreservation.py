# Design a hotel reservation (basic hotel reservation)

from enum import Enum

class Guest:
    def __init__(self, name, email=None, phone=None):
        self.name = name
        self.email = email
        self.phone = phone
        self.room = None


class RoomType(Enum):
    single = 1
    double = 2
    suit = 3


class Room:
    def __init__(self, id=0, guest=None):
        self.id = id
        self.guest = guest
        self.is_booked = False


class Hotel:
    def __init__(self, single=0, double=0, suit=0):
        self.single = []
        self.double = []
        self.suit = []
        self.capacity = []
        self.room_info = dict()
        self.hotel_print(single, double, suit)

    def hotel_print(self, single, double, suit):
        pass

    def available_rooms(self, type):
        pass

    def book_room(self, type, guest):
        pass

    def cancel_room(self, room_num):
        pass


class Booking:
    def __init__(self, address, hotels=1):
        self.address = address
        self.floors = [Hotel()]*hotels
        self.reservation_info = dict() # reservation_id: (guest_name, room_info)

    def hotel_set_up(self, hotel, single, double, suit):
        self.floors[floor-1].hotel_print(small, mid, large)
        return

    def show_available_rooms(self, hotel, room_type=0):
        return self.floors[floor-1].available_rooms(room_type)

    def booking(self, hotel, room_type, guest):
        reservation_info = self.floors[floor-1].book_room(room_type, guest)
        # reservation_info has (reservation_id, room_info)

        if reservation_info is None:
            print ("Room type: " + room_type + " is not available on the floor, please try another room or floor")
            return

        self.room_info[reservation_info[0]] = (guest.name, reservation_info[1])
        return reservation_info[0]

    def cancel_booking(self, reservation_id):
        if not self.reservation_info.get(reservation_id]):
            print ("Unknown reservation id, please confirm and enter the proper id!")
            return

        room_num = self.reservation_info[reservation_id][1].id
        self.floors[floor-1].cancel_room(room_num)
        return
