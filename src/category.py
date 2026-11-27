"""Модуль с классом Category."""

from src.product import Product


class Category:
    """Класс категории товаров."""

    name: str
    description: str

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Строковое представление категории: имя и общее число товаров на складе."""
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def __iter__(self):
        """Возвращает итератор по товарам категории."""
        return CategoryIterator(self)

    def add_product(self, product):
        """Добавляет товар в категорию, если он является продуктом или его наследником."""
        if not isinstance(product, Product):
            raise TypeError(
                "Добавлять можно только объекты класса Product и его наследников"
            )
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со списком товаров категории."""
        return "".join(f"{product}\n" for product in self.__products)

    @property
    def products_list(self):
        """Возвращает копию списка товаров категории."""
        return self.__products[:]


class CategoryIterator:
    """Итератор, перебирающий товары одной категории."""

    def __init__(self, category):
        """Принимает объект категории и готовится к перебору её товаров."""
        self._products = category.products_list
        self._index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self):
        """Возвращает очередной товар категории."""
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        raise StopIteration
