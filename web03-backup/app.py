from flask import *
from mongoengine import *
import mlab
from youtube_dl import YoutubeDL
from model.video import Video


app = Flask(__name__)
#session require a secret key
app.secret_key = "A super secret key"

mlab.connect()

@app.route('/logout')
def logout():
    del session['loggedin']
    return redirect(url_for('index'))

@app.route('/login', methods = ["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template('login.html')
    elif request.method == "POST":
        # return "Hello"
        form = request.form
        username = form['username']
        password = form['password']
        if username == 'admin' and password == 'admin':
            session['loggedin'] = True
            return redirect(url_for('admin'))
            return "Login successfully"
        else:
            return "Permission denied. Go away"

@app.route('/detail/<youtube_id>')
def detail(youtube_id):
    return render_template("detail.html", youtube_id = youtube_id)

@app.route('/admin', methods = ["GET","POST"])
def admin():
    if "loggedin" in session:
        if request.method == "GET":
            videos = Video.objects()
            return render_template('admin.html', videos = videos)

        elif request.method == "POST":
            form = request.form
            link = form['link']
            ydl = YoutubeDL()
            data = ydl.extract_info(link, download = False)
            title = data['title']
            thumbnail = data['thumbnail']
            views = data ['view_count']
            youtube_id = data['id']

            video = Video(title = title,
                        thumbnail = thumbnail,
                        views = views,
                        youtube_id = youtube_id,
                        link = link)
            video.save()
            return redirect(url_for("admin"))
    else:
        return redirect(url_for("login"))

@app.route('/')
def index():
    videos = Video.objects()
    return render_template('index.html', videos = videos)


if __name__ == '__main__':
  app.run(debug=True)
