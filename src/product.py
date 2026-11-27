"""Модуль с классом Product и его наследниками."""


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

    def __str__(self):
        """Строковое представление товара для пользователя."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """Возвращает полную стоимость товаров на складе двух объектов."""
        if type(self) is not type(other):
            raise TypeError(
                "Складывать можно только товары из одинаковых классов продуктов"
            )
        return self.__price * self.quantity + other.__price * other.quantity

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


class Smartphone(Product):
    """Класс смартфона: товар с производительностью, моделью, памятью и цветом."""

    def __init__(self, name, description, price, quantity,
                 efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Класс газонной травы: товар со страной-производителем и сроком прорастания."""

    def __init__(self, name, description, price, quantity,
                 country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
