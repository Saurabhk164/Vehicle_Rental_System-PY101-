from .vehicle import Vehicle

class Bike(Vehicle):
    def __init__(self, name, number, availability, rate_per_day, fuel, year):
        super().__init__(name, number, availability, rate_per_day, fuel, year)