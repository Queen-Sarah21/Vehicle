Vehicle Management System
Overview
This Python project implements a Vehicle Management System, providing a class hierarchy for different types of vehicles, including base vehicles, buses, cars, sport cars, and race cars.

Project Structure
Base Class: Vehicle

Attributes:
Number of doors
Price
Age
Year of Build (YOB)
Unique identifier (ID)

Methods:
Getters and setters for attributes
Display information about the vehicle
Factory methods for creating vehicles by age and copying vehicles
Class-level method to get the total number of objects

Derived Class: Bus
Inherits from the Vehicle class

Additional attributes:
Passenger capacity
Overrides display method and includes bus-specific information

Derived Class: Car
Inherits from the Vehicle class

Additional attributes:
Number of seats
Overrides display method and includes car-specific information

Derived Class: SportCar
Inherits from the Car class

Additional attributes:
Maximum speed
Overrides display method and includes sport car-specific information

Derived Class: RaceCar
Inherits from the SportCar class

Additional attributes:
Gas consumption
Overrides display method and includes race car-specific information

Usage
Vehicle Class:
Create a base vehicle using the Vehicle class.
Use factory methods to create vehicles by age or copy existing vehicles.

Bus Class:
Create a bus using the Bus class.
Utilize specific attributes and methods for buses.

Car Class:
Create a car using the Car class.
Utilize specific attributes and methods for cars.

SportCar Class:
Create a sport car using the SportCar class.
Utilize specific attributes and methods for sport cars.

RaceCar Class:
Create a race car using the RaceCar class.
Utilize specific attributes and methods for race cars.