"""Тесты магических методов и итератора категории."""

import pytest

from src.category import Category, CategoryIterator
from src.product import Product


def test_product_str(product):
    assert str(product) == "Смартфон, 50000.0 руб. Остаток: 10 шт."


def test_category_str(category, product):
    assert str(category) == "Электроника, количество продуктов: 10 шт."


def test_category_str_sums_quantity():
    p1 = Product("Товар A", "Описание A", 100, 10)
    p2 = Product("Товар B", "Описание B", 200, 2)
    category = Category("Тест", "Описание", [p1, p2])
    assert str(category) == "Тест, количество продуктов: 12 шт."


def test_add_products(product):
    other = Product("Ноутбук", "Игровой ноутбук", 90000.0, 5)
    assert product + other == 50000.0 * 10 + 90000.0 * 5


def test_add_matches_example():
    a = Product("A", "desc", 100, 10)
    b = Product("B", "desc", 200, 2)
    assert a + b == 1400


def test_add_with_wrong_type(product):
    with pytest.raises(TypeError):
        product + 10


def test_category_iter(category, product):
    items = list(category)
    assert len(items) == 1
    assert items[0] is product


def test_category_iterator_exhaustion(category, product):
    iterator = CategoryIterator(category)
    assert next(iterator) is product
    with pytest.raises(StopIteration):
        next(iterator)


def test_category_iterator_is_iterable(category, product):
    iterator = iter(CategoryIterator(category))
    assert next(iterator) is product
