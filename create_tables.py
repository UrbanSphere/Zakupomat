import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

create_products_table = 'CREATE TABLE IF NOT EXISTS products (name text, category text, unit text, amount real)'
cursor.execute(create_products_table)

create_recipes_table = 'CREATE TABLE IF NOT EXISTS recipes' \
                       ' (name text, category text, description text, ingredients blob)'
cursor.execute(create_recipes_table)

connection.commit()
connection.close()