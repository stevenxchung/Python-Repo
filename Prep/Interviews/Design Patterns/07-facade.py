class Order:
    def __init__(self, contents: str, take_out: bool):
        self.contents = contents
        self.take_out = take_out

    def get_order(self) -> str:
        return self.contents

    def is_take_out(self) -> bool:
        return self.take_out


class Cashier:
    def take_order(self, contents: str, take_out: bool) -> Order:
        return Order(contents, take_out)


class Food:
    def __init__(self, order: str):
        self.contents = order

    def get_food(self) -> str:
        return self.contents


class Chef:
    def prepare_food(self, order: Order) -> Food:
        return Food(order.get_order())


class PackagedFood(Food):
    def __init__(self, food: Food):
        super().__init__(food.get_food() + ' in a bag')


class KitchenStaff:
    def package_order(self, food: Food) -> PackagedFood:
        return PackagedFood(food)


class DriveThruFacade:
    def __init__(self):
        self.cashier = Cashier()
        self.chef = Chef()
        self.kitchen_staff = KitchenStaff()

    def take_order(self, order_contents: str, take_out: bool) -> Food:
        order = self.cashier.take_order(order_contents, take_out)
        food = self.chef.prepare_food(order)
        if take_out:
            food = self.kitchen_staff.package_order(food)

        print(f'take_order(): {food.contents}')
        return food


if __name__ == '__main__':
    drive_thru = DriveThruFacade()

    dine_in_food = drive_thru.take_order('Burger and Fries', take_out=False)
    dine_in_food.get_food()  # 'Burger and Fries'

    take_out_food = drive_thru.take_order('Pizza', take_out=True)
    take_out_food.get_food()  # 'Pizza in a bag'
