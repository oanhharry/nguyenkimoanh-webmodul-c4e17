from models.service import Service
import mlab

mlab.connect()

find_id = Service.objects.get(id='5af5a3bb46b3a9341ce23c72')
find_id.delete()


# test = Service.objects.with_id('5af59cd846b3a92829370fe9')

# test = mlab.Service.find({"_id": ObjectId("5af59cd846b3a92829370fe9")})
print(find_id["name"])
