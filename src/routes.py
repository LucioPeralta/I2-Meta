from flask import Blueprint, render_template, request, send_file, redirect, url_for
from src.classes.video import Video


app_routes = Blueprint('app_routes', __name__)


# Routes

@app_routes.route("/", methods=['GET'])
def Home():
    miniatura = "../static/Miniatura.png"
    return render_template('index.html', miniatura=miniatura)
    

@app_routes.route("/", methods=["POST"])
def search():
    try:
        url = request.form['input_url']
        youtube = Video(url)
        title = youtube.get_title()
        calidades_video = youtube.get_qualities_video()
        calidades_audio = youtube.get_qualities_audio()
        url_img = youtube.get_url_miniature()

        return render_template('index.html', 
                            url_video=url, 
                            titulo=title, 
                            calidades_video=calidades_video,
                            calidades_audio=calidades_audio, 
                            miniatura=url_img,
                            formato="checked")
    except:
        return redirect(url_for("app_routes.Home"))

@app_routes.route("/descargar", methods=["GET"])
def download():
    try:
        url = request.args.get("url")
        print(url)
        video = Video(url)

        name = request.args.get("name")
        formato = request.args.get("format")
        calidad = request.args.get("quality")
        if formato == "video":
            video.download_video(filename=name+".mp4", path="download/", quality=calidad)
            return send_file(path_or_file=f"./download/{name}.mp4" , as_attachment=True)
        elif formato == "audio":
            video.download_audio(filename=name+".mp3", path="download/", quality=calidad)
            return send_file(path_or_file=f"./download/{name}.mp3" , as_attachment=True)
        else:
            return redirect(url_for("app_routes.Home"))
    except:
        return redirect(url_for("app_routes.Home"))