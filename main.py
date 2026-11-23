"""Точка входа: демонстрация работы классов Product и Category."""

from src.category import Category
from src.product import Product


if __name__ == "__main__":
    product1 = Product(
        name="Смартфон", description="Современный смартфон",
        price=50000.0, quantity=10,
    )
    product2 = Product(
        name="Ноутбук", description="Игровой ноутбук",
        price=90000.0, quantity=5,
    )

    category = Category(
        name="Электроника", description="Техника и гаджеты",
        products=[product1, product2],
    )

    print(category.name)
    print(category.products[0].name)
    counts = Category.category_count, Category.product_count
    print(f"Категорий: {counts[0]}, товаров: {counts[1]}")
