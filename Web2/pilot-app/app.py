from flask import *
from mongoengine import*
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

mlab.connect()

#design database
#create collection

@app.route('/sign-in')
def signin():
    return render_template('signin.html')


@app.route('/detail/<service_id>')
def detail(service_id):
    service_detail = Service.objects.with_id(service_id)
    return render_template('detail.html', service_detail = service_detail)

@app.route('/search2')
def search2():
    all_service = Service.objects()
    return render_template('search2.html', all_service = all_service)

@app.route('/new-service',methods = ['GET', 'POST'])
def create():
    if request.method == "GET":
        return render_template('new-service.html')
    elif request.method == "POST":
        form = request.form
        name = form['name']
        yob = form['yob']
        phone = form['phone']
        gender = form['gender']
        # save service vào database
    new_service = Service(name = name, yob = yob, phone = phone, gender = gender)
    new_service.save()
    return redirect (url_for('admin'))

@app.route('/delete/<service_id>')
def delete(service_id):
    service_to_delete = Service.objects.with_id(service_id)
    if service_to_delete is not None:
        service_to_delete.delete()
        return redirect(url_for ('admin'))
    else:
        return "Service not found"
    return service_id


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search/<g>')
def search(g):
    all_service = Service.objects(gender = g, yob__lt=2000, address__contains = "Hà Nội" )
    return render_template('search.html',all_service = all_service)

@app.route('/customer')
def customer():
    all_customer = Customer.objects()
    return render_template('customer.html',all_customer = all_customer)

@app.route('/vip')
def vip():
    all_customer = Customer.objects(contacted = 0, gender = 1)
    all_vip = []
    for index, vip in enumerate(all_customer):
        all_vip.append(all_customer[index])
        if index == 9:
            break
    return render_template('vip.html',all_vip = all_vip)

@app.route('/admin')
def admin():
    all_service = Service.objects()
    return render_template('admin.html', all_service = all_service)

if __name__ == '__main__':
  app.run(debug=True)
