class Vehicle:
    def __init__(self, license_plate, type):
        self.license_plate = license_plate
        self.type = type

class ParkingSpot:
    def __init__(self, spot_id, type):
        self.type = type
        self.spot_id = spot_id
        self.is_empty = True
        self.vehicle = None
    
    def assign_vehicle(self, vehicle):
        if not self.is_empty:
            print("This spot is occupied! Please try another one")
        self.vehicle = vehicle
        self.is_empty = False
    
    def remove_vehicle(self):
        if self.is_empty:
            print("Nothing to vacate, slot is empty")
        self.vehicle = None
        self.is_empty = True

class ParkingLot:
    def __init__(self, name):
        self.name = name
        self.parking_spots = [] # [1,2,4]

    def add_parking_spots(self, spot):
        self.parking_spots.append(spot)
    
    def park_vehicle(self, vehicle):
        for spot in self.parking_spots:
            if spot.is_empty and spot.type == vehicle.type:
                spot.assign_vehicle(spot)
                print("Vehicle %s is parking at %d"%(vehicle.license_plate,spot.spot_id))
                spot.is_empty=False
                return
        return "No spot available, try another one"

    def unpark_vehicle(self, spot_id):
        for spot in self.parking_spots:
            if spot.spot_id==spot_id and spot.is_empty==False:
                spot.is_empty=True
                spot.vehicle = None
                print("Spot vacated")
                return 
        return "Spot already vacant"

    def check_availability(self, spot_id):
        for spot in self.parking_spots:
            if spot.spot_id==spot_id and spot.is_empty:
                print("Spot is available to park")
                return
        print("Spot unavailable :(. Please try another one! ")
            

# Example usage
if __name__ == "__main__":
    parking_lot = ParkingLot("Downtown Parking Lot")
    
    # Add parking spots
    parking_lot.add_parking_spots(ParkingSpot(1, "Small"))
    parking_lot.add_parking_spots(ParkingSpot(2, "Medium"))
    parking_lot.add_parking_spots(ParkingSpot(3, "Large"))


    # Park vehicles
    vehicle1 = Vehicle("ABC123", "Small")
    vehicle2 = Vehicle("XYZ789", "Large")
    
    parking_lot.park_vehicle(vehicle1)
    parking_lot.park_vehicle(vehicle2)
    
    # Check availability
    parking_lot.check_availability(3)
    
    # # Unpark a vehicle
    parking_lot.unpark_vehicle(1)
    parking_lot.check_availability(1)
