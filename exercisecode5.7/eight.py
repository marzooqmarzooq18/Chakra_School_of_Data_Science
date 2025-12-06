# -------------------- Class: Vehicle --------------------
class Vehicle:
    def __init__(self, vehicle_id, driver_name):
        self.vehicle_id = vehicle_id
        self.driver_name = driver_name
        self.distance_covered = 0
        self.fuel_used = 0
        self.__mileage = 0.0   # private attribute

    def add_trip(self, distance, fuel):
        """Record each trip data and update mileage."""
        if distance <= 0 or fuel <= 0:
            print("Invalid trip data. Distance and fuel must be positive.")
            return

        self.distance_covered += distance
        self.fuel_used += fuel
        self.__mileage = self.distance_covered / self.fuel_used

    def get_mileage(self):
        """Return mileage rounded to 2 decimals."""
        return round(self.__mileage, 2)

    def show_summary(self):
        """Display complete vehicle summary."""
        print(f"Vehicle ID: {self.vehicle_id} | Driver: {self.driver_name} | Mileage: {self.get_mileage()} km/l")


# -------------------- Demonstration --------------------
if __name__ == "__main__":
    # Create vehicle objects
    v1 = Vehicle("T001", "Manoj")
    v2 = Vehicle("T002", "Ramesh")

    # Record multiple trips
    v1.add_trip(120, 8)   # Trip 1
    v1.add_trip(150, 10)  # Trip 2

    v2.add_trip(200, 15)  # Trip 1
    v2.add_trip(100, 10)  # Trip 2

    # Show mileage summary
    print("\n--- Final Mileage Report ---")
    v1.show_summary()
    v2.show_summary()