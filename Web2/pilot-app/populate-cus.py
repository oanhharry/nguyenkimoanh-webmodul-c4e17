from models.customer import Customer
from faker import Faker
import mlab
from random import randint
mlab.connect()

fake = Faker()

for i in range(100):
    customer = Customer(name = fake.name(),
                        gender = randint(0,1),
                        email = fake.email(),
                        phone = fake.phone_number(),
                        job = fake.job(),
                        company = fake.company(),
                        contacted = randint(0,1),
                        )
    customer.save()
