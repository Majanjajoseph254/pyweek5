# Base class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle moves forward.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("Driving on the road 🚗")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("Flying through the sky ✈️")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("Sailing across the water 🚤")

# Function demonstrating polymorphism
def travel(vehicle):
    vehicle.move()

# Example usage
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    travel(v)