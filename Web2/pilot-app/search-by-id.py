from models.service import Service
import mlab

mlab.connect()

#search by id with 2 option:

# find_id = Service.objects.get(id='5af5a22646b3a9316bf611a0')

find_id = Service.objects.with_id('5af5a22646b3a9316bf611a0')

#delete the record
# find_id.delete()

print(find_id["name"])
