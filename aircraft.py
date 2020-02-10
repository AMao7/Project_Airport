# People (name): Passenger(__passport)

# Aircrafts (capacity): Planes (plane serial and airline)  - As a checking assistant i want to be able to register
#passengers(name and passport)
# list all flights
# add passenger to flight
# list all passengers on the plane

# Flight (Flight n., originn, destination and datetime, list of passengers)

class Aircrafts():
    def __init__(self, capacity):
        self.capacity = capacity


class Plane(Aircrafts):
    def __init__(self, plane_serial, airline):
        self.plane_serial = plane_serial
        self.airline = airline

