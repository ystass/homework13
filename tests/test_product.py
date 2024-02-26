import pytest
from src.product import Product


@pytest.fixture()
def televisor():
    return Product('Телевизор', 'Диагональ 55',
                   18500.50, 11)


def test_init(televisor):
    assert televisor.name == 'Телевизор'
    assert televisor.description == 'Диагональ 55'
    assert televisor.price == 18500.50
    assert televisor.quantity == 11

