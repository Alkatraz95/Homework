from main import Category, Product


def test_product_init(product):
    assert product.name == "Смартфон"
    assert product.description == "Современный смартфон"
    assert product.price == 50000.0
    assert product.quantity == 10


def test_category_init(category, product):
    assert category.name == "Электроника"
    assert category.description == "Техника и гаджеты"
    assert category.products == [product]


def test_category_counters(category, product):
    another = Product("Ноутбук", "Игровой ноутбук", 90000.0, 5)
    Category("Ноутбуки", "Мобильная техника", [another])

    assert Category.category_count == 2
    assert Category.product_count == 2
