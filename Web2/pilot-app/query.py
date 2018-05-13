from models.service import Service
from models.customer import Customer
import mlab

mlab.connect()
all_service = Service.objects(gender=1)
all_customer = Customer.objects(gender = 1, contacted = 0)

first_service = all_service[0]

# for index, service in enumerate(all_service):
#     print(service['name'])
#     if index ==9:
#         break
# print(first_service['name'])

# for index, customer in enumerate(all_customer):
#     print(customer['name'])
#     if index == 10:
#         break
print(first_service['name'])
