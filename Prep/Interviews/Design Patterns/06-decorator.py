from abc import ABC, abstractmethod


class Coffee(ABC):
    @abstractmethod
    def get_cost(self):
        pass


class SimpleCoffee(Coffee):
    def get_cost(self):
        return 1.1


class CoffeeDecorator(Coffee):
    def __init__(self, decoratedCoffee):
        self.decoratedCoffee = decoratedCoffee

    def get_cost(self):
        return self.decoratedCoffee.get_cost()


class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self) -> float:
        res = super().get_cost() + 0.5
        print(f'Milk - get_cost(): {res}')
        return res


class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self) -> float:
        res = super().get_cost() + 0.2
        print(f'Sugar - get_cost(): {res}')
        return res


class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    def get_cost(self) -> float:
        res = super().get_cost() + 0.7
        print(f'Cream - get_cost(): {res}')
        return res


if __name__ == '__main__':
    coffee = SimpleCoffee()
    coffee.get_cost()  # 1.1

    coffee = MilkDecorator(coffee)
    coffee.get_cost()  # 1.6

    coffee = SugarDecorator(coffee)
    coffee.get_cost()  # 1.8

    coffee = CreamDecorator(coffee)
    coffee.get_cost()  # 2.5
