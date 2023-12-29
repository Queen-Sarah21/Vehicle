


class Vehicle:

    """
        Topic: This is  base class that contains the vehicle object model
        Date: 07 Nov 2023
        Auothr: Salar
    """

    ### Class Level Attr
    __seq = 100
    __counter = 0

    def __init__(self, nbDoors = 1, price = 200, age = 0, yob = 2023):

        ### Instance Level Attr
        self._numberOfDoors = nbDoors
        self._price =  price
        self._age =  age
        self._yob = yob ### Year Of Build

        self.__id =  Vehicle.__seq
        Vehicle.__seq += 5
        Vehicle.__counter  += 1



    ### Getters and Setters

    ### Number fo doors
    def getID(self):
        return self.__id
        
    ### Number fo doors
    
    def getNbDoors(self):
        return self._numberOfDoors
    """
    def setNbDoors(self, nd):

        if nd == None or nd == '' or nd < 1:
            print(f"Error: The Number of Doors cannot be set as {nd}.")
        else:
            self.__numberOfDoors = nd
    """

    ### Price
    
    def getPrice(self):
        return self._price

    def setPrice(self, pr):

        if pr == None or pr == '' or pr < 200:
            print(f"Error: The Price cannot be set as {pr}.")
        else:
            self._price = pr


    ### Age
    def getAge(self):
        return self._age
    
    def setAge(self, ag):

        if ag == None or ag == '' or ag < 0:
            print(f"Error: The Age cannot be set as {ag}.")
        else:
            self._age = ag

     ### Year of Build
    def getYob(self):
        return self._yob


    ### Instance Level Methods

    def display(self):

        print(f"This Vehicle, {self.__id}- has {self._numberOfDoors} doors, {self._age} years old, built on {self._yob}, and its price is ${self._price}.")
        


    ### Class Level Methods

    ### Factory Method to create a vehicle from age 
    @classmethod
    def createVehicleByAge(cls, nbDoors=1, price=200, age=0):
        yob = 2023 - age
        return cls(nbDoors, price, age, yob)

    ### Factory Method to create a vehicle from another vehicle (copy constructor) 
    @classmethod
    def copy(cls, v):
        return cls(v._numberOfDoors, v._price, v._age, v._yob)

    @classmethod
    def getTotalObj(cls):
        print(f"The total number of vehicles are {cls.__counter}.")

    """
    @classmethod
    def setCounter(cls):
        cls.__counter -= 1
    """

    #### Overriding
    def __str__(self):
        return f"{self.__id}: This Vehicle has {self._numberOfDoors} doors,\t{self._age} years old,\t{self._yob} as year of build,\t${self._price} price."
    
    def __del__(self):
        print(f"{self.__id} removed!")
        Vehicle.__counter -= 1



class Bus(Vehicle):

    __seq =  1000
    __counter = 0

    def __init__(self, nbDoors = 1, price = 200, age = 0, yob = 2023, capacity = 10):

        ##Vehicle.__init__(self, nbDoors, price, age, yob)
        super().__init__(nbDoors, price, age, yob)
        self.__capacity = capacity
        self.__id =  Bus.__seq
        Bus.__seq += 1
        Bus.__counter += 1



    ### Gettres and Setters

    def getID(self):
        return self.__id

    def getCapacity(self):
        return self.__capacity

    def setCapacity(self, pc):

        if pc == None or pc == "" or pc < 10:
            print(f"Error: The Passenger Capacity cannot be set as {pc}")
        else:
            self.__capacity = pc


    
    def display(self):
        print(f"This Bus, {self.__id}- has {self._numberOfDoors} doors, {self._age} years old, built on {self._yob} with {self.__capacity} capacity  and its price is ${self._price}.")


    ### Class Level Methods

    ### Factory Method to create a Bus from age 
    @classmethod
    def createVehicleByAge(cls, nbDoors=1, price=200, age=0, capacity= 10):
        yob = 2023 - age
        return cls(nbDoors, price, age, yob, capacity)

    ### Factory Method to create a Bus from another Bus (copy constructor) 
    @classmethod
    def copy(cls, b):
        return cls(b._numberOfDoors, b._price, b._age, b._yob, b.__capacity)
    
    @classmethod
    def getTotalObj(cls):
        print(f"The total number of buses are {cls.__counter}.")

    #### Overriding
    def __str__(self):
        return f"{self.__id}: This Bus has {self._numberOfDoors} doors,\t{self._age} years old,\t{self._yob} as year of build,\t{self.__capacity} passenger capacity,\t${self._price} price."


    def __del__(self):
        print(f"{self.__id} removed!")
        ### reduce the value of counter from vehicle.
        super().__del__()
        Bus.__counter -= 1


class Car(Vehicle):

    __seq =  2000
    __counter = 0

    def __init__(self, nbDoors = 1, price = 200, age = 0, yob = 2023, nbSeats = 2):

        Vehicle.__init__(self, nbDoors, price, age, yob)
        self._numberOfSeats = nbSeats
        self.__id =  Car.__seq
        Car.__seq += 1
        Car.__counter += 1

    ### Gettres and Setters

    def getID(self):
        return self.__id

    def getNbSeats(self):
        return self._numberOfSeats

    def setNbSeats(self, ns):

        if ns == None or ns == "" or ns < 2:
            print(f"Error: The Number of Seats cannot be set as {ns}")
        else:
            self._numberOfSeats = ns

    ### Class Level Methods
    @classmethod
    def getTotalObj(cls):
        print(f"The total number of cars are {cls.__counter}.")

    #### Overriding
    def __str__(self):
        return f"{self.__id}: This Car has {self._numberOfDoors} doors,\t{self._age} years old,\t{self._yob} as year of build,\t{self._numberOfSeats} seats,\t${self._price} price."


    def __del__(self):
        print(f"{self.__id} removed!")
        super().__del__()
        Car.__counter -= 1




class SportCar(Car):


    __counter = 0
    __seq = 3000

    def __init__(self, nbDoors = 1, price = 200, age = 0, yob = 2023, nbSeats = 2, mSpeed = 250):

        super().__init__(nbDoors, price, age, yob, nbSeats)
        self.__id = SportCar.__seq
        self._maxSpeed = mSpeed
        SportCar.__seq += 1
        SportCar.__counter +=1




    ### Gettres and Setters
    def getID(self):
        return self.__id

    def getMaxSpeed(self):
        return self._maxSpeed

    def setMaxSpeed(self, ms):

        if ms == None or ms == "" or ms < 250:
            print(f"Error: The Max Speed cannot be set as {ms}")
        else:
            self._maxSpeed = ms

    ### Class Level Methods
    @classmethod
    def getTotalObj(cls):
        print(f"The total number of sport cars are {cls.__counter}.")

    #### Overriding
    def __str__(self):
        return f"{self.__id}: This Sport Car has {self._numberOfDoors} doors,\t{self._age} years old,\t{self._yob} as year of build,\t{self._numberOfSeats} seats,\t${self._price} price\t{self._maxSpeed} KM/h."


    def __del__(self):
        print(f"{self.__id} removed!")
        super().__del__()
        SportCar.__counter -= 1
        



class RaceCar(SportCar):


    __counter = 0
    __seq = 4000

    def __init__(self, nbDoors = 1, price = 200, age = 0, yob = 2023, nbSeats = 2, mSpeed = 250, gasCons =  15):

        SportCar.__init__(self, nbDoors, price, age, yob, nbSeats, mSpeed)
        self.__id = RaceCar.__seq
        self.__gasConsumption = gasCons
        RaceCar.__seq += 1
        RaceCar.__counter +=1




    ### Gettres and Setters
    def getID(self):
        return self.__id

    def getGasConsumption(self):
        return self.__gasConsumption

    def setGasConsumption(self, gc):

        if gc == None or gc == "" or gc < 15:
            print(f"Error: The Gas Consumption cannot be set as {gc}")
        else:
            self.__gasConsumption = gc

    ### Class Level Methods
    @classmethod
    def getTotalObj(cls):
        print(f"The total number of race cars are {cls.__counter}.")

    #### Overriding
    def __str__(self):
        return f"{self.__id}: This Sport Car has {self._numberOfDoors} doors,\t{self._age} years old,\t{self._yob} as year of build,\t{self._numberOfSeats} seats,\t${self._price} price\t{self._maxSpeed} KM/h \t{self.__gasConsumption} lit/100KM."


    def __del__(self):
        print(f"{self.__id} removed!")
        super().__del__()
        RaceCar.__counter -= 1
        

"""
    Overriding method:
            1- Method name cannot be chnaged
            2- Arguments cannot be changed
            3- Return type cannot be changed
            4- It is valid between paren and child (Inheritance)

"""




























    
