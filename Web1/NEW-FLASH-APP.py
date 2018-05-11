from flask import Flask, render_template, redirect
app = Flask(__name__)

@app.route ('/')
def index():
    return "Hi C4E17"

@app.route ('/about-me')
def hi():
    return "Hello, I'm Oanh, 25 years olds. I'm a marketer. Travelling is my hobby"

@app.route ('/school')
def school():
    return redirect('http://techkids.vn/')


if __name__ == '__main__':
  app.run(debug=True)
