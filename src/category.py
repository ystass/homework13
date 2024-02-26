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
        self.products = products

        Category.number_categories += 1
        Category.number_products += len(self.products)
