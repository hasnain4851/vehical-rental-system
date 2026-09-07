# Vehicle Rental System - Version 1.1
# Features: rent and return vehicles, rental charge calculation

def rent_vehicle(vehicle_id, customer_id):
    print("Vehicle", vehicle_id, "rented to customer", customer_id)

def return_vehicle(vehicle_id):
    print("Vehicle", vehicle_id, "returned")

def calculate_rental_charge(days, rate=500):
    charge = days * rate
    print("Rental Charge = Rs.", charge)
    return charge
