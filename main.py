from backend.rental_system import RentalSystem

def main():
    rental = RentalSystem(
        vehicles_file="data/vehicles_100.json",
        customers_file="data/customers.json",
        log_file="data/logs.txt"
    )

    while True:
        print("\n===== VEHICLE RENTAL SYSTEM =====")
        print("1. View Available Vehicles")
        print("2. Rent a Vehicle")
        print("3. Return a Vehicle")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\nAvailable Vehicles:")
            for v in rental.vehicles:
                if v.is_available():
                    print(f"{v.get_name()} - {v.get_number()} ({v.get_rate()}/day)")

        elif choice == "2":
            number = input("Enter vehicle number: ")
            name = input("Enter customer name: ")
            phone = input("Enter phone: ")
            days = int(input("Enter number of days: "))

            success, msg = rental.rent_vehicle(number, name, phone, days)
            print(msg)

        elif choice == "3":
            number = input("Enter vehicle number to return: ")
            success, msg = rental.return_vehicle(number)
            print(msg)

        elif choice == "4":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()