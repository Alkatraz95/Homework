import pytest

from main import Category, Product


@pytest.fixture(autouse=True)
def reset_counters():
    """Сбрасывает счётчики классов перед каждым тестом."""
    Category.category_count = 0
    Category.product_count = 0
    yield


@pytest.fixture
def product():
    return Product("Смартфон", "Современный смартфон", 50000.0, 10)


@pytest.fixture
def category(product):
    return Category("Электроника", "Техника и гаджеты", [product])
