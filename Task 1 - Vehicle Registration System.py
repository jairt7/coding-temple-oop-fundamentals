# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, vehicle_type, owner):
        self.reg_num = reg_num
        self.vehicle_type = vehicle_type
        self.owner = owner
    
    def update_owner(self, new_owner):
        self.owner = new_owner
    
    def display_info(self):
        print(f"Vehicle type: {self.vehicle_type}, vehicle registration number: {self.reg_num}, vehicle owner: {self.owner}")

vehicles = {}

def register_vehicle(reg_num, vehicle_type, owner):
    if reg_num in vehicles:
        print("Registration number already exists. Try again.")
        return
    vehicles[reg_num] = Vehicle(reg_num, vehicle_type, owner)
    print("Vehicle registered.")


my_car = Vehicle(1, "car", "me")
my_car.display_info()
my_car.update_owner("you")
my_car.display_info()
my_new_car = Vehicle(2, "truck", "dealer")
my_new_car.display_info()
my_new_car.update_owner("me")
my_new_car.display_info()