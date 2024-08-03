from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def get_type(self) -> str:
        pass


class Car(Vehicle):
    def get_type(self) -> str:
        res = 'Car'
        print(f'get_type(): {res}')
        return res


class Bike(Vehicle):
    def get_type(self) -> str:
        res = 'Bike'
        print(f'get_type(): {res}')
        return res


class Truck(Vehicle):
    def get_type(self) -> str:
        res = 'Truck'
        print(f'get_type(): {res}')
        return res


class VehicleFactory(ABC):
    @abstractmethod
    def create_vehicle(self) -> Vehicle:
        pass


class CarFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Car()


class BikeFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Bike()


class TruckFactory(VehicleFactory):
    def create_vehicle(self) -> Vehicle:
        return Truck()


if __name__ == '__main__':
    car_factory = CarFactory()
    truck_factory = TruckFactory()
    bike_factory = BikeFactory()

    my_car = car_factory.create_vehicle()
    my_truck = truck_factory.create_vehicle()
    my_bike = bike_factory.create_vehicle()

    my_car.get_type()  # 'Car'
    my_truck.get_type()  # 'Truck'
    my_bike.get_type()  # 'Bike'
