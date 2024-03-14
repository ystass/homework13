from src.product import Product
from src.MixinOutput import MixinOutput


class Category(MixinOutput):
    """Класс <Категории>"""
    name: str
    description: str
    products: list

    number_categories = 0
    number_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        super().__init__()

        Category.number_categories += 1
        Category.number_products += len(self.__products)

    def __len__(self):
        quantity_products = 0
        for i in self.__products:
            quantity_products += i.quantity
        return quantity_products

    def __str__(self):
        return f'{self.name}, количество продуктов: {len(self)} шт.'

    def add_goods(self, name, products):
        if isinstance(name, Product):
            self.__products.append(products)
        else:
            print(f'Товар {name} должен быть объектом класса {Product} или дочерних классов')

    @property
    def product_list(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n'

    @property
    def products(self):
        return self.__products


