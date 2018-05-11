from flask import Flask, render_template
app = Flask(__name__)

@app.route('/user/<username>')
def profile(username):
    users = {
    "van":
        {"name": "Chu Khánh Vân",
        "age": "22",},

    "oanh":
        {"name": "Oanh Harry",
        "age": "25",},
    "thai":
        {"name": "Nguyễn Hồng Thái",
        "age": "27",},
    "huyen":
        {"name": "Hồ Thị Huyền",
        "age": "34",},

    }
    if username in users.keys():
        
        return render_template('profile.html', users = users, username = username)
    else:
        return "User not found"


if __name__ == '__main__':
    app.run(debug = False)
