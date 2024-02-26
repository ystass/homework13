import pytest
from src.category import Category

@pytest.fixture()
def phones():
    return Category('Телефоны', 'Смартфоны', ['iPhone', 'Samsung',
                                              'Xiaomi', 'HONOR', 'HUAWEI'])

def test_init(phones):
    assert phones.name == 'Телефоны'
    assert phones.description == 'Смартфоны'
    assert phones.products == ['iPhone', 'Samsung', 'Xiaomi', 'HONOR', 'HUAWEI']
    assert phones.number_categories == 1
    assert phones.number_products == 5
