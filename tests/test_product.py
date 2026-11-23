"""Тесты класса Product."""

from src.product import Product


def test_product_init(product):
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_new_product_creates_instance():
    data = {
        "name": "Ноутбук",
        "description": "Игровой ноутбук",
        "price": 90000.0,
        "quantity": 5,
    }
    new_item = Product.new_product(data)

    assert new_item.name == "Ноутбук"
    assert new_item.description == "Игровой ноутбук"
    assert new_item.price == 90000.0
    assert new_item.quantity == 5


def test_price_setter_updates_value(product):
    product.price = 55000.0
    assert product.price == 55000.0


def test_price_setter_rejects_zero_and_negative(product, capsys):
    product.price = 0
    assert product.price == 50000.0
    product.price = -100
    assert product.price == 50000.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
