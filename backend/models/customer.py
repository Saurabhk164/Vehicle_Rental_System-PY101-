class Customer:
    def __init__(self, name, phone, customer_id):
        self.name = name
        self.phone = phone
        self.customer_id = customer_id
        self.rentals = []

    def add_rental(self, vehicle_number):
        self.rentals.append(vehicle_number)