class Vehicle:
    def __init__(self, name, number, availability, rate_per_day, fuel, year):
        self.__name = name
        self.__number = number
        self.__availability = availability
        self.__rate_per_day = rate_per_day
        self.__fuel = fuel
        self.__year = year

    # Getters
    def get_name(self):
        return self.__name

    def get_number(self):
        return self.__number

    def is_available(self):
        return self.__availability

    def get_rate(self):
        return self.__rate_per_day

    def get_fuel(self):
        return self.__fuel

    def get_year(self):
        return self.__year

    # Setters
    def set_availability(self, status):
        self.__availability = status

    # Actions
    def rent(self):
        self.__availability = False

    def return_vehicle(self):
        self.__availability = True