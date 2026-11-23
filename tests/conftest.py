"""Фикстуры для тестов классов Product и Category."""

import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product():
    return Product("Смартфон", "Современный смартфон", 50000.0, 10)


@pytest.fixture
def category(product):
    return Category("Электроника", "Техника и гаджеты", [product])
