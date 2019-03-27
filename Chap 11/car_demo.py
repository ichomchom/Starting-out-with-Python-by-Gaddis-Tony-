import vehicles

def main():
    #Create object from Car class
    #2007 BMW 12,500 miles, $21,500.00, 4 doors

    car = vehicles.Car('BMW', 2007, 12500, 21500.0, 4)

    #2002 Toyota pickup truck 30,000 miles, $12,000, 4WD
    truck = vehicles.Truck('Toyota', 2002, 30000, 12000, '4WD')

    #SUV 2000 Volvo, 30,000 miles, $18,500, 5 passenger seats
    suv = vehicles.SUV('Volvo', 2000, 30000, 18500, 5)
    
    #Display car's data
    print('The following car is in inventory:')
    print('Make:', car.get_make())
    print('Model:', car.get_model())
    print('Mileage:', car.get_mileage())
    print('Price:', car.get_price())
    print('Number of doors:', car.get_doors())

    #Display truck's data
    print('The following truck is in inventory:')
    print('Make:', truck.get_make())
    print('Model:', truck.get_model())
    print('Mileage:', truck.get_mileage())
    print('Price:', truck.get_price())
    print('Drive type:', truck.get_drive_type())

    #Display suv's data
    print('The following suv is in inventory:')
    print('Make:', suv.get_make())
    print('Model:', suv.get_model())
    print('Mileage:', suv.get_mileage())
    print('Price:', suv.get_price())
    print('Passenger Capacity:', suv.get_pass_cap())
    
main()
