from flask import Flask,render_template
app = Flask(__name__)

@app.route('/bmi2/<weight>/<height>')
def bmi(weight,height):
    w = int(weight)
    h = int(height)/100
    bmi = w/(h*h)
    x = 0
    if bmi < 16:
        x = "Severely underweight"
    elif bmi < 18.5:
        x = "SUnderweight"
    elif bmi < 25:
        x = "Normal"
    elif bmi < 30:
        x ="Overweight"
    else:
        x = "Obese"
    return render_template('bmi.html',bmi = bmi, x = x)

if __name__ == '__main__':
  app.run(debug=True)
