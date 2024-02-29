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

    def add_goods(self, name, products):
        if name == self.name:
            self.__products.append(products)
        else:
            print(f'Товар {products} должен быть объектом класса {name}')

    @property
    def product_list(self):
        for product in self.__products:
            return f'{product.name}, {product.price} руб. Остаток:{product.quantity} шт.\n'


