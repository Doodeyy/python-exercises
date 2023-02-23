class Vehicle:
    maxSpeed = 220
    distance = 100
    def __init__(self, driver, hp, weight, color):
        self.driver = driver
        self.hp = hp
        self.weight = weight
        self.color = color
    
    def kgPerHp(self):
        return self.weight / self.hp
    
    def timeDistance(self):
        return (self.distance / self.maxSpeed) * 60
    
class Bus(Vehicle):
    maxSpeed = 120
    def __init__(self, driver, hp, weight, color, busType):
        super().__init__(driver, hp, weight, color)
        self.busType = busType

class Truck(Vehicle):
    maxSpeed = 90
    def __init__(self, driver, hp, weight, color, truckType):
        super().__init__(driver, hp, weight, color)
        self.truckType = truckType

vehicles = []

vehicles.append(Vehicle("John", 520, 1610, "yellow"))
vehicles.append(Bus("Manos", 450, 7000, "white", "sigle deck bus"))
vehicles.append(Bus("Panos", 220, 2100, "black", "mini bus"))
vehicles.append(Truck("Thanos", 650, 10_000, "blue", "cub over"))
vehicles.append(Truck("Fanhs", 600, 21_000, "red", "fire truck"))

for vehicle in vehicles:
    print(vehicle.driver, vehicle.kgPerHp(), "kg/hp", vehicle.timeDistance(), "min")
