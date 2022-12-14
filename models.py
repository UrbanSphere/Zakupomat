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
            return None


    def add_to_db(self):
        if self.find_by_name(self.name):
            self.del_from_db()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'INSERT INTO products VALUES (?, ?, ?, 0.0)'
        cursor.execute(query, (self.name, self.cat, self.unit))

        connection.commit()
        connection.close()


    def del_from_db(self):
        if self.find_by_name(self.name) is None:
            raise NameError(f'No such product called \'{self.name}\' to be deleted')
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


class Recipe:
    def __init__(self, name, category, description, ingredients: list):
        self.name = name
        self.cat = category
        self.des = description
        self.ingr = ingredients


    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM recipes WHERE name=?'
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        if row:
            return cls(row[0], row[1], row[2], row[3])
        else:
            return None


    def add_to_db(self):
        if self.find_by_name(self.name):
            self.del_from_db()

        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'INSERT INTO recipes VALUES (?, ?, ?, ?)'
        cursor.execute(query, (self.name, self.cat, self.des, self.ingr))

        connection.commit()
        connection.close()


    def del_from_db(self):
        if self.find_by_name(self.name) is None:
            raise NameError(f'No such product called \'{self.name}\' to be deleted')
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'DELETE FROM recipes WHERE name=?'
        cursor.execute(query, (self.name,))

        connection.commit()
        connection.close()


    def to_dict(self):
        return {'name': self.name, 'category': self.cat, 'description': self.des, 'ingredients': self.ingr}


    @staticmethod
    def show_all_products():
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()

        query = 'SELECT * FROM recipes'
        result = cursor.execute(query)
        row = result.fetchall()

        connection.commit()
        connection.close()
        return row