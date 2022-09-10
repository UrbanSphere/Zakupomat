from models import *


Mleko = Product('mleko', 'nabiał', 'ml')
Mleko.add_to_db()
Chleb = Product('chleb', 'pieczywo', 'szt')
Chleb.add_to_db()
print(Product.show_all_products())

Chleb.del_from_db()
print(Product.show_all_products())


