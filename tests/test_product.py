"""Тесты класса Product."""


def test_product_init(product):
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10
