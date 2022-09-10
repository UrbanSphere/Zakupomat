from models import *


Mleko = Product('mleko', 'nabiał', 'ml').add_to_db()
Chleb = Product('chleb', 'pieczywo', 'szt').add_to_db()


print(Product.show_all_products())


