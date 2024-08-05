class Meal:
    def __init__(self):
        self.cost = 0.0
        self.takeOut = False
        self.main = ''
        self.drink = ''

    def get_cost(self) -> float:
        return self.cost

    def set_cost(self, cost: float) -> None:
        self.cost = cost

    def get_takeout(self) -> bool:
        return self.takeOut

    def set_takeout(self, takeOut: bool) -> None:
        self.takeOut = takeOut

    def get_main(self) -> str:
        return self.main

    def set_main(self, main: str) -> None:
        self.main = main

    def get_drink(self) -> str:
        return self.drink

    def set_drink(self, drink: str) -> None:
        self.drink = drink


class MealBuilder:

    def __init__(self):
        self.meal = Meal()

    def add_cost(self, cost: float) -> 'MealBuilder':
        self.meal.set_cost(cost)
        res = self.meal.get_cost()
        print(f'add_cost(): {res}')
        return self

    def add_takeout(self, takeOut: bool) -> 'MealBuilder':
        self.meal.set_takeout(takeOut)
        res = self.meal.get_takeout()
        print(f'add_takeout(): {res}')
        return self

    def add_main_course(self, main: str) -> 'MealBuilder':
        self.meal.set_main(main)
        res = self.meal.get_main()
        print(f'add_main_course(): {res}')
        return self

    def add_drink(self, drink: str) -> 'MealBuilder':
        self.meal.set_drink(drink)
        res = self.meal.get_drink()
        print(f'add_drink(): {res}')
        return self

    def build(self) -> Meal:
        return self.meal


if __name__ == '__main__':
    builder = MealBuilder()
    my_meal = (
        builder.add_cost(15.99)
        .add_takeout(True)
        .add_main_course('Burger')
        .add_drink('Coke')
        .build()
    )

    my_meal.get_cost()  # Cost: 15.99
    my_meal.get_takeout()  # TakeOut: true
    my_meal.get_main()  # Main: 'Burger'
    my_meal.get_drink()  # Drink: 'Coke'
