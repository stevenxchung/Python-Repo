from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def notify(self, itemName: str) -> None:
        pass


class Customer(Observer):
    def __init__(self, name: str) -> None:
        self.name = name
        self.notifications = 0

    def notify(self, itemName: str) -> None:
        self.notifications += 1

    def count_notifications(self) -> int:
        print(f'count_notifications({self.name}): {self.notifications}')
        return self.notifications


class OnlineStoreItem:
    def __init__(self, itemName: str, stock: int) -> None:
        self.itemName = itemName
        self.stock = stock
        self.observers = {}

    def subscribe(self, observer: Observer) -> None:
        self.observers[observer.name] = observer

    def unsubscribe(self, observer: Observer) -> None:
        del self.observers[observer.name]

    def update_stock(self, newStock: int) -> None:
        prev, self.stock = self.stock, newStock
        if not (prev == 0 and newStock > 0):
            return

        for observer in self.observers.values():
            observer.notify(self.itemName)


if __name__ == '__main__':
    item1 = OnlineStoreItem('Awesome Gadget', 0)

    customer1 = Customer('John Doe')
    customer2 = Customer('Jane Doe')

    item1.subscribe(customer1)
    item1.subscribe(customer2)
    item1.update_stock(5)  # customer1 and customer2 are notified

    item1.unsubscribe(customer1)

    item1.update_stock(0)  # No one is notified
    item1.update_stock(3)  # Only customer2 is notified this time
    item1.update_stock(2)  # No one is notified

    customer1.count_notifications()  # 1
    customer2.count_notifications()  # 2
