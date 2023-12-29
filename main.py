

"""

    Topic: This is a main file that let the user  to intract with the app
    Date: 07 Nov 2023
    Author: Salar

"""

from base.vehicle import Vehicle, Bus, Car, SportCar, RaceCar

if __name__ == "__main__":


    print("++++++++++++++++++++++ Vehicle 1")
    v1 = Vehicle()
    ##v1.display()
    print(v1)

    print("\n++++++++++++++++++++++ Vehicle 2")
    v2 = Vehicle(age=2, yob= 2021, price= 5000, nbDoors = 2 )
    ##v2.display()
    print(v2)
    
    print("\n++++++++++++++++++++++ Vehicle 3")
    v3 = Vehicle(age=2, yob= 2021, nbDoors = 2 )
    ##v3.display()
    print(v3)

    print("\n++++++++++++++++++++++ Vehicle 4")
    v4 = Vehicle.createVehicleByAge(age=5,nbDoors=3)
    ##v4.display()
    print(v4)

    print("\n++++++++++++++++++++++ Vehicle 5")
    v5 = Vehicle.copy(v3)
    ##v5.display()
    print(v5)


    print("\n++++++++++++++++++++++ Bus 1")
    b1 = Bus()
    ##b1.display()
    print(b1)

    print("\n++++++++++++++++++++++ Bus 2")
    b2 = Bus(age=5, yob= 2018, price= 25000, nbDoors = 2, capacity=30 )
    print(b2)

    print("\n++++++++++++++++++++++ Bus 3")
    ##b3 = Bus(age=3, price= 25000, capacity=30 )
    b3 = Bus.createVehicleByAge(age=3, price= 25000, capacity=30)
    print(b3)

    print("\n++++++++++++++++++++++ Bus 4")
    b4 = Bus.copy(b3)
    print(b4)


    print("\n\n")
    Vehicle.getTotalObj()
    Bus.getTotalObj()


    ### =============== delete an obj
    del(v1)
    del(b1)

    print("\n\n")
    Vehicle.getTotalObj()
    Bus.getTotalObj()


    print("\n++++++++++++++++++++++ Car 1")
    c1 = Car()
    print(c1)

    print("\n++++++++++++++++++++++ Car 2")
    c2 = Car(age=5, yob= 2018, price= 15000, nbDoors = 2, nbSeats=5 )
    print(c2)

    print("\n\n")
    Vehicle.getTotalObj()
    Bus.getTotalObj()
    Car.getTotalObj()


    print("\n++++++++++++++++++++++ Sport Car 1")
    sc1 = SportCar()
    print(sc1)

    print("\n++++++++++++++++++++++ Sport Car 2")
    sc2 = SportCar(age=5, yob= 2018, price= 15000, nbDoors = 2, nbSeats=5, mSpeed = 350 )
    print(sc2)

    print("\n++++++++++++++++++++++ Sport Car 3")
    sc3 = SportCar.copy(sc2)
    print(sc3)

    Vehicle.getTotalObj()
    Bus.getTotalObj()
    Car.getTotalObj()
    SportCar.getTotalObj()


    print("\n++++++++++++++++++++++ Race Car 1")
    rc1 = RaceCar()
    print(rc1)

    print("\n++++++++++++++++++++++ Race Car 2")
    rc2 = RaceCar(age=5, yob= 2018, price= 15000, nbDoors = 2, nbSeats=5, mSpeed = 350 )
    print(rc2)

    print("\n++++++++++++++++++++++ Race Car 3")
    rc3 = RaceCar.copy(sc2)
    print(rc3)

    Vehicle.getTotalObj()
    Bus.getTotalObj()
    Car.getTotalObj()
    SportCar.getTotalObj()
    RaceCar.getTotalObj()
    












    




    """
    print(Vehicle.__base__)
    for k, v in object.__dict__.items():
        print(f"{k} +++++++++++++ {v}")
    """

    """
    print("\n++++++++++++++++++++++ Built-in class attr")

    print(Vehicle.__doc__)
    ##print(Vehicle.__dict__)
    for k, v in Vehicle.__dict__.items():
        print(f"{k} --- {v}")

    print(Vehicle.__name__)
    print(v1.__class__.__name__)
    print(Vehicle.__module__)
    print(Vehicle.__base__)

    
    print("\n++++++++++++++++++++++ Built-in attr methods")

    print(hasattr(v1,'getPrice'))
    print(hasattr(v1,'age'))
    print(hasattr(v1,'getAge'))
    print(getattr(v2,'getPrice'))
    setattr(v2,'setPrice', 10000)
    print(getattr(v2,'getPrice'))
    print(getattr(v3,"getNbDoors"))
    setattr(v3,'setNbDoors', 5)
    print(getattr(v3,"getNbDoors"))


    for k, v in int.__dict__.items():
        print(f"{k} ########### {v}")

    
    """
    


    











































