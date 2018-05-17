from flask import Flask, render_template
from mongoengine import*
import mlab
from models.service import Service
from models.customer import Customer

app = Flask(__name__)

mlab.connect()

#design database
#create collection



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
