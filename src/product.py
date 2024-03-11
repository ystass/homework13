class Product:
    '''Класс <Продукты>'''
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f'{self.name}, {self.price} руб. Остаток: {self.quantity} шт.'

    def __add__(self, other):
        if issubclass(type(other), Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            print('Выбранные товары не одного и того же класса')

    @classmethod
    def new_product(cls, name, description, price, quantity, products):
        for i in products:
            if name == i.name:
                i.quantity += quantity
                if price < i.price:
                    i.price = price
            else:
                return cls(name, description, price, quantity)


    @property
    def price_change(self):
        return self.price


    @price_change.setter
    def price_change(self, new_price):
        if new_price <= 0:
            print('Введенная цена некорректна')
        elif new_price < self.price:
            user_answer = input('Вы хотите ввести цену ниже существующей y / n')
            if user_answer == 'y':
                self.price = new_price


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
