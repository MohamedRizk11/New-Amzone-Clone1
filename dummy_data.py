import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
import random
from django.conf import settings
from faker import Faker
from product.models import Brand, Product


def create_Products(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg']
    flags = ['Sale ','New','Feature']
    for _ in range(n):
       
        Product.objects.create(
            name=fake.name(),
            image=f'brand/{images[random.randint(0,8)]}'   ,         
            falg= flags[random.randint(0,2)],
            price= round(random.uniform(1500.99,2599.99),2),
            sku = random.randint(1000,1000000000000),
            subtitels= fake.text(max_nb_chars=300),
            desciptions= fake.text(max_nb_chars=20000),
            quantity=random.randint(1,30),
            brand=Brand.objects.get(id=random.randint(110,190)),
        )
    print(f'Seed {n} Product Successfully')       


def create_Brand(n):
    fake = Faker()
    images=['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg','9.jpg']
    
    for _ in range(n):

        Brand.objects.create(
            name=fake.name(),
            image =f'brand/{images[random.randint(0,8)]}',
    
            
        ) 

    print(f'Seed {n} Brands Successfully')       



#create_Brand(100)
create_Products(500)