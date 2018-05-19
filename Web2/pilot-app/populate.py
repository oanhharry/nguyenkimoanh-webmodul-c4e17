from models.service import Service
from faker import Faker
import mlab
from random import randint, choice
mlab.connect()


fake = Faker()
# print(fake.address())
# for i in range(50):
#     print("Saving serive", i +1, "...")
#
#     service = Service(name = fake.name(),
#                         yob = randint(1990,2001),
#                         gender = randint(0,1),
#                         height = randint(150,170),
#                         phone = fake.phone_number(),
#                         address = fake.address(),
#                         status = choice([True, False]),
#                         image = )
#     service.save()

service1 = Service(
                name = "Oanh",
                yob = 1993,
                gender = 0,
                height = 160,
                phone = '01647899654',
                image = "oanh",
                description = "vui tính",
                measurement = [88,67,90],
                )
service1.save()
service2 = Service(name = "Donkey",
                yob = 1996,
                gender = 1,
                height = 170,
                phone = '01647899874',
                image = "donkey",
                description = "đáng yêu",
                measurement = [90,70,90],

                )
service2.save()
