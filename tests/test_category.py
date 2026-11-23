"""Тесты класса Category и счётчиков."""

from src.category import Category
from src.product import Product


def test_category_init(category, product):
    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"


def test_products_getter_returns_string(category, product):
    expected = "Смартфон, 50000.0 руб. Остаток: 10 шт.\n"
    assert category.products == expected


def test_category_counters(category, product):
    Category.category_count = 0
    Category.product_count = 0

    another = Product("Ноутбук", "Игровой ноутбук", 90000.0, 5)
    Category("Ноутбуки", "Мобильная техника", [another])

    assert Category.category_count == 1
    assert Category.product_count == 1


def test_add_product_increases_count(category):
    Category.product_count = 0

    new_item = Product("Планшет", "Планшет для чтения", 30000.0, 3)
    category.add_product(new_item)

    assert Category.product_count == 1
    assert "Планшет, 30000.0 руб. Остаток: 3 шт.\n" in category.products
