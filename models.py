import sqlite3


class Product:
    def __init__(self, name, cat, unit, amount=float):
        self.name = name
        self.cat = cat
        self.unit = unit
        self.amount = amount


    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM products WHERE name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:
            return cls(row[0], row[1], row[2], row[3])
        else:
            raise NameError(f'No such item called \'{name}\' found')


    def add_to_db(self):
        try:
            self.find_by_name(self.name)
            self.del_from_db()
        except NameError:
            print(f'No such product called \'{self.name}\' found.')

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'INSERT INTO products VALUES (?, ?, ?, 0.0)'
        cursor.execute(query, (self.name, self.cat, self.unit))

        connection.commit()
        connection.close()


    def del_from_db(self):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'DELETE FROM products WHERE name=?'
        cursor.execute(query, (self.name,))

        connection.commit()
        connection.close()


    def to_dict(self):
        return {'name': self.name, 'category': self.cat, 'unit': self.unit, 'amount': self.amount}


    @staticmethod
    def show_all_products():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM products'
        result = cursor.execute(query)
        row = result.fetchall()

        connection.commit()
        connection.close()
        return row

