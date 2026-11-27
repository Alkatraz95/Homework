"""Тесты классов-наследников Product и новой функциональности."""

import pytest

from src.category import Category
from src.product import LawnGrass, Product, Smartphone


def test_smartphone_attributes(smartphone):
    assert smartphone.name == "Samsung"
    assert smartphone.efficiency == 95.5
    assert smartphone.model == "S23 Ultra"
    assert smartphone.memory == 256
    assert smartphone.color == "Серый"
    assert smartphone.price == 180000.0
    assert smartphone.quantity == 5


def test_lawngrass_attributes(lawngrass):
    assert lawngrass.country == "Россия"
    assert lawngrass.germination_period == "7 дней"
    assert lawngrass.color == "Зелёный"
    assert lawngrass.price == 500.0


def test_smartphone_is_product(smartphone):
    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, Smartphone)


def test_lawngrass_is_product(lawngrass):
    assert isinstance(lawngrass, Product)
    assert not isinstance(lawngrass, Smartphone)


def test_issubclass_checks():
    assert issubclass(Smartphone, Product)
    assert issubclass(LawnGrass, Product)
    assert not issubclass(Product, Smartphone)


def test_inherited_str(smartphone, lawngrass):
    assert str(smartphone) == "Samsung, 180000.0 руб. Остаток: 5 шт."
    assert str(lawngrass) == "Газонная трава, 500.0 руб. Остаток: 20 шт."


def test_add_same_class_products():
    a = Smartphone("A", "desc", 100, 2, 90, "m1", 64, "чёрный")
    b = Smartphone("B", "desc", 200, 3, 95, "m2", 128, "белый")
    assert a + b == 100 * 2 + 200 * 3


def test_add_different_product_classes(smartphone, lawngrass):
    with pytest.raises(TypeError):
        smartphone + lawngrass
    with pytest.raises(TypeError):
        lawngrass + smartphone


def test_add_subclass_with_base_class(smartphone, product):
    with pytest.raises(TypeError):
        smartphone + product
    with pytest.raises(TypeError):
        product + smartphone


def test_add_product_accepts_inherited(category, smartphone):
    Category.product_count = 0
    category.add_product(smartphone)
    assert Category.product_count == 1
    assert "Samsung, 180000.0 руб. Остаток: 5 шт.\n" in category.products


def test_add_product_rejects_non_product(category):
    with pytest.raises(TypeError):
        category.add_product("Просто строка")
