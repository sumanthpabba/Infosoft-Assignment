class FuelStation:

    def __init__(self, diesel: int, petrol: int, electric: int):
        """Initializes the FuelStation object with the specified number of slots for each fuel type."""
        self.fuel_slots: dict = {
            "diesel": diesel, 
            "petrol": petrol,
            "electric": electric
        }
        self.initial_slots = self.fuel_slots.copy()

    def fuel_vehicle(self, fuel_type: str) -> bool:
        """
        Determines whether a fuel slot can be alloted to a vehicle of the specified type

        Args
        ----
        fuel_type: str
            The type of fuel required ("diesel", "petrol", or "electric")

        Returns
        -------
        bool:
            True if a slot is found and the vehicle is fueled, False otherwise
        """
        if fuel_type not in self.fuel_slots or self.fuel_slots[fuel_type] == 0:
            return False

        self.fuel_slots[fuel_type] -= 1

        return True

    def open_fuel_slot(self, fuel_type: str) -> bool:
        """
        Releases a fuel slot of the specified type.

        Args
        ----
        fuel_type: str
            The type of fuel ("diesel", "petrol", or "electric").

        Returns
        -------
        bool:
            True if a slot is released, False if all slots are already empty.
        """
        if fuel_type not in self.fuel_slots or self.fuel_slots[fuel_type] == self.initial_slots[fuel_type]:
            return False
        
        self.fuel_slots[fuel_type] += 1
        return True



fuel_station = FuelStation(diesel=2, petrol=2, electric=1)
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("petrol"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.fuel_vehicle("electric"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("diesel"))
print(fuel_station.fuel_vehicle("diesel"))
print(fuel_station.open_fuel_slot("electric"))
print(fuel_station.open_fuel_slot("electric"))
