"""Модуль с классом Product."""


class Product:
    """Класс товара магазина."""

    name: str
    description: str
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_data):
        """Создаёт товар из словаря с параметрами."""
        return cls(
            product_data["name"],
            product_data["description"],
            product_data["price"],
            product_data["quantity"],
        )

    @property
    def price(self):
        """Возвращает цену товара."""
        return self.__price

    @price.setter
    def price(self, new_price):
        """Устанавливает новую цену, если она положительная."""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price
