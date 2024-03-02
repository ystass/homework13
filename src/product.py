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
