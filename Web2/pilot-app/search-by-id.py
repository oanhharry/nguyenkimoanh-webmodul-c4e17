from models.service import Service
import mlab

mlab.connect()

#search by id with 2 option:

# find_id = Service.objects.get(id='5af5a22646b3a9316bf611a0')

find_id = "5af59b2946b3a9256defdfd8"
hera = Service.objects.with_id(find_id)

#delete the record
# find_id.delete()

# print(find_id["name"])

if hera is not None:
    print(hera.address)
    hera.update(set__address = "Phố Vọng", set__height = 170)
    hera.reload()
    print(hera.address)
else:
    print("Service not found")
