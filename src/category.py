from src.product import Product


class Category:
    '''Класс <Категории>'''
    name: str
    description: str
    products: list

    number_categories = 0
    number_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products

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
        if name == self.name:
            self.__products.append(products)
        else:
            print(f'Товар {products} должен быть объектом класса {name}')

    @property
    def product_list(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n'

    @property
    def products(self):
        return self.__products


class Smartphone(Product):
    def __init__(self, name, description, products, performance, model, memory, color):
        super().__init__(self, name, description, products)
        self.performance = performance
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    def __init__(self, name, description, products, manufacturer, germination_period, color):
        super().__init__(self, name, description, products)
        self.manufacturer = manufacturer
        self.germination_period = germination_period
        self.color = color
