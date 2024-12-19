from typing import Literal


class Tires:
    def __init__(self, size):
        self.size = size
        self.pressure = size

    def get_pressure(self):
        return f"Tire pressure is: {self.pressure}"

    def pump(self):
        return "Tires pumped"


class Engine:
    def __init__(self, fuel_type: Literal["electric", "petrol"]):
        self.fuel_type = fuel_type
        self.state = False

    def start(self):
        if self.state:
            return "Engine already running"

        self.state = True
        return "Engine running"

    def stop(self):
        if not self.state:
            return "Engine stopped"

        self.state = False
        return "Engine stopped"

    def get_state(self):
        if self.state:
            return "Engine is running"

        return "Engine is stopped"


class Vehicle:
    def __init__(self, vin, engine, tires):
        self.vin = vin
        self.engine = engine
        self.tires = tires


city_tires = Tires(15)
electric_engine = Engine("electric")
city_car = Vehicle("ABC123", electric_engine, city_tires)

print(city_car.engine.get_state())
print(city_car.engine.start())
print(city_car.engine.get_state())
print(city_car.engine.stop())
print(city_car.engine.get_state())

print(city_car.tires.get_pressure())
print(city_car.tires.pump())

off_road_tires = Tires(18)
petrol_engine = Engine("petrol")
all_terrain_car = Vehicle("CBA321", petrol_engine, off_road_tires)

print(all_terrain_car.engine.get_state())
print(all_terrain_car.engine.start())
print(all_terrain_car.engine.get_state())
print(all_terrain_car.engine.stop())
print(all_terrain_car.engine.get_state())

print(all_terrain_car.tires.get_pressure())
print(all_terrain_car.tires.pump())
