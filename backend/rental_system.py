import json
from datetime import datetime
from .models.car import Car
from .models.bike import Bike
from .models.customer import Customer

class RentalSystem:
    def __init__(self, vehicles_file, customers_file, log_file):
        self.vehicles_file = vehicles_file
        self.customers_file = customers_file
        self.log_file = log_file
        self.vehicles = []
        self.customers = []
        self.load_vehicles()
        self.load_customers()


    def load_vehicles(self):
        with open(self.vehicles_file, "r") as f:
            data = json.load(f)

        for v in data["vehicles"]:
            if v["type"] == "Car":
                obj = Car(v["name"], v["number"], v["availability"],
                          v["rate_per_day"], v["fuel"], v["year"])
            else:
                obj = Bike(v["name"], v["number"], v["availability"],
                           v["rate_per_day"], v["fuel"], v["year"])

            self.vehicles.append(obj)

    def save_vehicles(self):
        out_list = []
        for v in self.vehicles:
            out_list.append({
                "name": v.get_name(),
                "number": v.get_number(),
                "type": "Car" if isinstance(v, Car) else "Bike",
                "availability": v.is_available(),
                "rate_per_day": v.get_rate(),
                "fuel": v.get_fuel(),
                "year": v.get_year()
            })

        with open(self.vehicles_file, "w") as f:
            json.dump({"vehicles": out_list}, f, indent=4)


    def load_customers(self):
        try:
            with open(self.customers_file, "r") as f:
                data = json.load(f)
                for c in data["customers"]:
                    obj = Customer(c["name"], c["phone"], c["customer_id"])
                    obj.rentals = c["rentals"]
                    self.customers.append(obj)
        except FileNotFoundError:
            self.customers = []

    def save_customers(self):
        out_list = []
        for c in self.customers:
            out_list.append({
                "name": c.name,
                "phone": c.phone,
                "customer_id": c.customer_id,
                "rentals": c.rentals
            })

        with open(self.customers_file, "w") as f:
            json.dump({"customers": out_list}, f, indent=4)


    def find_vehicle(self, number):
        for v in self.vehicles:
            if v.get_number() == number:
                return v
        return None



    def rent_vehicle(self, number, customer_name, customer_phone, days):
        vehicle = self.find_vehicle(number)

        if not vehicle:
            return False, "Vehicle does not exist."

        if not vehicle.is_available():
            return False, "Vehicle is not available."

        # cost calculation
        cost = vehicle.get_rate() * days

        # update vehicle status
        vehicle.rent()
        self.save_vehicles()

        # log action
        self.log_action(f"RENT | {number} | {customer_name} | Days: {days} | Cost: {cost}")

        # add customer
        customer_id = customer_phone
        customer = self.get_or_create_customer(customer_name, customer_phone)
        customer.add_rental(number)
        self.save_customers()

        return True, cost



    def return_vehicle(self, number):
        vehicle = self.find_vehicle(number)

        if not vehicle:
            return False, "Vehicle does not exist."

        if vehicle.is_available():
            return False, "Vehicle is already returned."

        vehicle.return_vehicle()
        self.save_vehicles()

        # log
        self.log_action(f"RETURN | {number}")

        return True, "Vehicle returned successfully."


    def get_or_create_customer(self, name, phone):
        for c in self.customers:
            if c.phone == phone:
                return c
        new_customer = Customer(name, phone, phone)
        self.customers.append(new_customer)
        return new_customer



    def log_action(self, message):
        with open(self.log_file, "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            f.write(f"{timestamp} | {message}\n")