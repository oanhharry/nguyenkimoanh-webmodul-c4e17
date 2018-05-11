from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
    {
        "title": "Thơ con cóc",
        "content": "Ahihi",
        "author": "Tuấn Anh",
        "gender": 1,
    },
    {
        "title": "Thơ con ếch",
        "content": "Lạy chúa trên cao, turndown 4 what",
        "author": "Nhật Minh",
        "gender": 0,
    },
    {
        "title": "DingTea",
        "content": "Trường DingTea không nghĩ ra gì",
        "author": "Trường Híp",
        "gender": 1
    },
    ]
    return render_template("index.html",posts = posts)

@app.route ('/c4e')
def sayhi():
    return "Hi C4E17"

@app.route ('/hi/<name>/<age>')
def hi(name,age):
    return "Hi {0}, you are {1} years olds".format(name, age)

@app.route('/sum/<int:number1>/<int:number2>')
def sum(number1, number2):
    # number1 = int(number1)
    # number2 = int(number2)
    return str(number1+number2)
    # return "Sum is {0}".format(int(number1)+int(number2))

if __name__ == '__main__':
  app.run(debug=True)
