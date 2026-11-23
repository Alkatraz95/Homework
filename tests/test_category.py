"""Тесты класса Category и счётчиков."""

from src.category import Category
from src.product import Product


def test_category_init(category, product):
    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"
    assert category.products == [product]


def test_category_counters(category, product):
    Category.category_count = 0
    Category.product_count = 0

    another = Product("Ноутбук", "Игровой ноутбук", 90000.0, 5)
    Category("Ноутбуки", "Мобильная техника", [another])

    assert Category.category_count == 1
    assert Category.product_count == 1
