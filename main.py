import sqlite3


class Product:

    def __init__(self, name, cat, unit, amount=float):
        self.name = name
        self.cat = cat
        self.unit = unit
        self.amount = amount

    def add_to_db(self):
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()


