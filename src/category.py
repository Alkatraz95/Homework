"""Модуль с классом Category."""


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

    def add_product(self, product):
        """Добавляет товар в категорию и увеличивает счётчик продуктов."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """Возвращает строку со списком товаров категории."""
        result = ""
        for product in self.__products:
            result += (
                f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n"
            )
        return result
