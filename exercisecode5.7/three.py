# -------------------- Base Class --------------------
class Vehicle:
    total_trips = 0  # Class variable shared by all vehicles

    def __init__(self, vehicle_id, brand, capacity_kg, fuel_type):
        self.vehicle_id = vehicle_id
        self.brand = brand
        self.capacity_kg = capacity_kg
        self.fuel_type = fuel_type

    def calculate_trip_cost(self, distance_km):
        """Base method (to be overridden by subclasses)."""
        return 0

    def display_info(self):
        """Display vehicle basic details."""
        print(f"Vehicle ID: {self.vehicle_id} | Brand: {self.brand} | "
              f"Capacity: {self.capacity_kg}kg | Fuel: {self.fuel_type}")


# -------------------- Subclass 1: Truck --------------------
class Truck(Vehicle):
    def __init__(self, vehicle_id, brand, capacity_kg, fuel_type, cargo_type, cost_per_km):
        super().__init__(vehicle_id, brand, capacity_kg, fuel_type)
        self.cargo_type = cargo_type
        self.cost_per_km = cost_per_km

    def calculate_trip_cost(self, distance_km):
        """Truck trip cost = distance × cost_per_km"""
        cost = distance_km * self.cost_per_km
        Vehicle.total_trips += 1
        print(f"Vehicle: {self.brand} | Truck | Cargo: {self.cargo_type} | "
              f"Trip Cost for {distance_km} km: ₹{int(cost)}")
        return cost


# -------------------- Subclass 2: Van --------------------
class Van(Vehicle):
    def __init__(self, vehicle_id, brand, capacity_kg, fuel_type, temperature_control):
        super().__init__(vehicle_id, brand, capacity_kg, fuel_type)
        self.temperature_control = temperature_control

    def calculate_trip_cost(self, distance_km):
        """Base ₹20/km + ₹5/km if temperature control enabled."""
        cost_per_km = 20
        if self.temperature_control:
            cost_per_km += 5
        cost = distance_km * cost_per_km
        Vehicle.total_trips += 1
        print(f"Vehicle: {self.brand} | Van | Temp Control: {self.temperature_control} | "
              f"Trip Cost: ₹{int(cost)}")
        return cost


# -------------------- Subclass 3: EVTruck --------------------
class EVTruck(Truck):
    def __init__(self, vehicle_id, brand, capacity_kg, battery_charge, cargo_type, cost_per_km):
        super().__init__(vehicle_id, brand, capacity_kg, "Electric", cargo_type, cost_per_km)
        self.battery_charge = battery_charge  # in %

    def calculate_trip_cost(self, distance_km):
        """EV Truck cost = 15% cheaper than normal Truck."""
        base_cost = super().calculate_trip_cost(distance_km)
        discounted_cost = base_cost * 0.85
        Vehicle.total_trips += 0  # already incremented by Truck’s method
        print(f"Vehicle: {self.brand} | EVTruck | Cargo: {self.cargo_type} | "
              f"Trip Cost: ₹{int(discounted_cost)}")
        return discounted_cost

    def refuel(self):
        """Override fuel method for EVs."""
        print("Charging vehicle...done.")


# -------------------- Trip Simulation --------------------
if __name__ == "__main__":
    # Create vehicle objects
    t1 = Truck("T001", "TATA", 15000, "Diesel", "Cement", cost_per_km=50)
    v1 = Van("V001", "Mahindra", 3000, "Petrol", temperature_control=True)
    e1 = EVTruck("E001", "Tesla", 10000, 80, "Electronics", cost_per_km=50)

    # Calculate trip costs for each
    t1.calculate_trip_cost(250)
    v1.calculate_trip_cost(250)
    e1.calculate_trip_cost(250)

    # Show total trips
    print(f"Total Trips Completed: {Vehicle.total_trips}")