from flask import Blueprint, render_template, request
from src.classes.video import Video


app_routes = Blueprint('app_routes', __name__)


# Routes

@app_routes.route("/", methods=['GET'])
def Home():
    miniatura = "data:image/jpeg;base64,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"
    return render_template('index.html', miniatura=miniatura)
    

@app_routes.route("/", methods=["POST"])
def Search():
    url = request.form['input_url']
    youtube = Video(url)
    
    title = youtube.get_title()
    calidades = youtube.get_qualities_video()
    url_img = youtube.get_url_miniature()

    return render_template('index.html', video=youtube, titulo=title, calidades=calidades, miniatura=url_img, formato="checked")
    
