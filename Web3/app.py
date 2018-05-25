from flask import *
from mongoengine import *
import mlab
from youtube_dl import YoutubeDL
from model.video import Video


app = Flask(__name__)

mlab.connect()

@app.route('/admin', methods = ["GET","POST"])
def admin():
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

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True)
