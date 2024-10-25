class Car:
    def __init__(self, brand, model, price_per_hour):
        self.brand = brand
        self.model = model
        self.price_per_hour = price_per_hour

    def __str__(self):
        return f"{self.brand} {self.model} - ${self.price_per_hour}/hour"


class Showroom:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Added: {car}")

    def display_cars(self):
        if not self.cars:
            print("No cars available in the showroom.")
            return
        print("Available Cars:")
        for idx, car in enumerate(self.cars, start=1):
            print(f"{idx}. {car}")

    def rent_car(self, index, hours):
        if 0 <= index < len(self.cars):
            car = self.cars[index]
            total_cost = car.price_per_hour * hours
            print(f"You have rented {car.brand} {car.model} for {hours} hours.")
            print(f"Total cost: ${total_cost:.2f}")
            return total_cost
        else:
            print("Invalid car selection.")

    def sell_car(self, index):
        if 0 <= index < len(self.cars):
            car = self.cars.pop(index)
            print(f"Sold: {car}")
        else:
            print("Invalid car selection.")


def main():
    showroom = Showroom()

    
    showroom.add_car(Car("Toyota", "Camry", 20))
    showroom.add_car(Car("Honda", "Civic", 15))
    showroom.add_car(Car("Ford", "Mustang", 30))

    while True:
        print("\n--- Car Showroom Menu ---")
        print("1. Display Cars")
        print("2. Rent a Car")
        print("3. Sell a Car")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            showroom.display_cars()
        elif choice == '2':
            showroom.display_cars()
            car_index = int(input("Select the car number to rent: ")) - 1
            hours = int(input("Enter number of hours to rent: "))
            showroom.rent_car(car_index, hours)
        elif choice == '3':
            showroom.display_cars()
            car_index = int(input("Select the car number to sell: ")) - 1
            showroom.sell_car(car_index)
        elif choice == '4':
            print("Exiting the showroom. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()