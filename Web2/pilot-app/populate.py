from models.service import Service
from faker import Faker
import mlab
from random import randint, choice
mlab.connect()


fake = Faker()
# print(fake.address())
for i in range(50):
    print("Saving serive", i +1, "...")

    service = Service(name = fake.name(),
                        yob = randint(1990,2001),
                        gender = randint(0,1),
                        height = randint(150,170),
                        phone = fake.phone_number(),
                        address = fake.address(),
                        status = choice([True, False]))
    service.save()
