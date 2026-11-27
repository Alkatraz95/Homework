"""Фикстуры для тестов классов Product и Category."""

import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


@pytest.fixture
def product():
    return Product("Смартфон", "Современный смартфон", 50000.0, 10)


@pytest.fixture
def category(product):
    return Category("Электроника", "Техника и гаджеты", [product])


@pytest.fixture
def smartphone():
    return Smartphone(
        "Samsung", "Флагман", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


@pytest.fixture
def lawngrass():
    return LawnGrass(
        "Газонная трава", "Трава для газона", 500.0, 20, "Россия", "7 дней", "Зелёный"
    )
