# Design a parking lot

from enum import Enum

class Size(Enum):
    small = 1
    mid = 2
    large = 3


class Vehicle:
    def __init__(self, size=1, license_num=None):
        self.size = Size(size)
        self.license_num = license_num
        self.parking_space = None


class ParkingSpace:
    def __init__(self, id, size=Size(1)):
        self.id = id
        self.size = size
        self.is_occupied = False


class Floor:
    def __init__(self, small=0, mid=0, large=0):
        self.small = []
        self.mid = []
        self.large = []
        self.capacity = 0
        self.spot_info = dict()
        self.floor_print(small, mid, large)

    def floor_print(self, small, mid, large):
        small = small
        mid = small + mid
        large = mid + large
        if small:
            for id in range(small, 0, -1):
                self.small.append(ParkingSpace(id, Size(1)))

        if mid:
            for id in range(mid, small, -1):
                self.mid.append(ParkingSpace(id, Size(2)))

        if large:
            for id in range(large, mid, -1):
                self.large.append(ParkingSpace(id, Size(3)))
        self.capacity = large

    def occupy_parking_spot(self, size):
        if len(self.spot_info) <= self.capacity:
            size = size.value
            if size == 1:
                if len(self.small) != 0:
                    spot = self.small.pop()
                    spot.is_occupied = True
                    spot_num = spot.id
                    self.spot_info[spot_num] = spot
                    return spot_num
                size += 1

            if size == 2:
                if len(self.mid) != 0:
                    spot = self.mid.pop()
                    spot.is_occupied = True
                    spot_num = spot.id
                    self.spot_info[spot_num] = spot
                    return spot_num
                size += 1

            if size == 3 and len(self.large) !=0:
                spot = self.large.pop()
                spot.is_occupied = True
                spot_num = spot.id
                self.spot_info[spot_num] = spot
                return spot_num
        return None

    def empty_parking_spot(self, spot_num):
        spot = self.spot_info.get(spot_num)
        if spot:
            spot.is_occupied = False
            if spot.size == 1:
                self.small.append(spot)
            elif spot.size == 2:
                self.mid.append(spot)
            else:
                self.large.append(spot)

            del self.spot_info[spot_num]
        return


class ParkingLot:
    def __init__(self, address, floors):
        self.address = address
        self.floors = [Floor() for i in range(floors)]
        self.parking_info = dict()

    def floor_set_up(self, floor, small=0, mid=0, large=0):
        self.floors[floor-1].floor_print(small, mid, large)

    def park(self, floor, vehicle):
        if self.parking_info.get(vehicle.license_num):
            print ("Vehicle is already parked!!!")
            return
        spot_size = vehicle.size
        spot_num = self.floors[floor-1].occupy_parking_spot(spot_size)
        print ("Park vehicle(license_num: \""+ vehicle.license_num + "\") at spot: ", spot_num)
        if spot_num:
            self.parking_info[vehicle.license_num] = (floor, spot_num)
            vehicle.parking_space = spot_num
        else:
            print ("Parking is Full!!")
        return spot_num

    def leave(self, vehicle):
        vehicle_location = self.parking_info.get(vehicle.license_num)
        if vehicle_location:
            self.floors[vehicle_location[0]-1].empty_parking_spot(vehicle_location[1])
            vehicle.parking_space = None
            del self.parking_info[vehicle.license_num]
        else:
            print ("Did you park Vehicle(license num:\""+vehicle.license_num+"\") here? Vehicle is unknown!!")
        return

    def know_parking_spot(self, vehicle):
        vehicle_location = self.parking_info.get(vehicle.license_num)
        if vehicle_location:
            print ("Vehicle(license_num: \""+ vehicle.license_num + "\") is parked at parking spot \""+ str(vehicle_location[1]) + "\" on the floor \""+\
                                        str(vehicle_location[0]) + "\".")
        else:
            print ("Did you park vehicle here? Vehicle is unknown!!")
        return



##### Initializing parking lot

# Parking lot at SF with 3 floors
lot1 = ParkingLot("SF", 3)

# 1st floor has 5 small, 5 mid and 5 large parking
lot1.floor_set_up(1, 5, 5, 5)

# 2nd floor has 5 small, 5 mid and 2 large parking
lot1.floor_set_up(2, 5, 5, 2)

# 3rd floor has 2 small, 4 mid and 3 large parking
lot1.floor_set_up(3, 2, 4, 3)



##### Initializing car
car1 = Vehicle(1, "firstCar1")
car2 = Vehicle(2, "firstCar2")

truck1 = Vehicle(3, "123truck")

bike1 = Vehicle(1, "bike1")
bike2 = Vehicle(1, "bike2")
bike3 = Vehicle(1, "bike3")
bike4 = Vehicle(1, "bike4")

####### Parking cars on floor-3
lot1.park(3, car1) # parking at 1 (small size)
lot1.park(3, car2) # parking at 3 (because mid size)
lot1.park(3, truck1) # parking at 7 (because large size)
lot1.park(3, bike1) # parking at 2
lot1.park(3, bike2) # parking at 4
lot1.park(3, bike3) # parking at 5
lot1.park(3, bike4) # parking at 6

# already parked car
lot1.park(3, bike4) # print "car is already parked!!!"

# non-parked car leave
non_parked_car = Vehicle(2, "secondCar")
lot1.leave(non_parked_car) # print "Did you park car(license num:"secondCar") here? Car is unknown!!"


# leaving
lot1.leave(bike1) # empty spot 2 (no print)
lot1.leave(bike2) # empty spot 4 (no print)
lot1.leave(bike3) # empty spot 5 (no print)
lot1.leave(bike4) # empty spot 6 (no print)
print ("___________")
lot1.leave(bike1) # print "Did you park car(license num:"bike1") here? Car is unknown!!"
lot1.leave(bike2) # print "Did you park car(license num:"bike1") here? Car is unknown!!"
lot1.leave(bike3) # print "Did you park car(license num:"bike1") here? Car is unknown!!"
lot1.leave(bike4) # print "Did you park car(license num:"bike1") here? Car is unknown!!"


car11 = Vehicle(1, "11Car")
car12 = Vehicle(1, "12Car")
lot1.park(3, car11) # parking at 6
lot1.park(3, car12) # parking at 5
lot1.park(3, bike3) # parking at 4
lot1.park(3, bike4) # parking at 2
lot1.know_parking_spot(car11)


############## Sample output based on the above setup:
# Park vehicle(license_num: "firstCar1") at spot:  1
# Park vehicle(license_num: "firstCar2") at spot:  3
# Park vehicle(license_num: "123truck") at spot:  7
# Park vehicle(license_num: "bike1") at spot:  2
# Park vehicle(license_num: "bike2") at spot:  4
# Park vehicle(license_num: "bike3") at spot:  5
# Park vehicle(license_num: "bike4") at spot:  6
# Vehicle is already parked!!!
# Did you park Vehicle(license num:"secondCar") here? Vehicle is unknown!!
# ___________
# Did you park Vehicle(license num:"bike1") here? Vehicle is unknown!!
# Did you park Vehicle(license num:"bike2") here? Vehicle is unknown!!
# Did you park Vehicle(license num:"bike3") here? Vehicle is unknown!!
# Did you park Vehicle(license num:"bike4") here? Vehicle is unknown!!
# Park vehicle(license_num: "11Car") at spot:  6
# Park vehicle(license_num: "12Car") at spot:  5
# Park vehicle(license_num: "bike3") at spot:  4
# Park vehicle(license_num: "bike4") at spot:  2
# Vehicle(license_num: "11Car") is parked at parking spot "6" on the floor "3".
