import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds255329.mlab.com:55329/cms-app

host = "ds255329.mlab.com"
port = 55329
db_name = "cms-app"
user_name = "admin"
password = "admin"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
