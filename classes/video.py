from pytube import YouTube
from pytube import exceptions

class Video:
    
    def __init__(self, url: str):
        self.url_video = url
        self.fetch_video()

    def fetch_video(self):
        self.video = YouTube(self.url_video)
        try:
            self.video.streams
        except exceptions.RegexMatchError:
            raise ErrorVideo("Url no reconocida")
        except exceptions.VideoUnavailable:
            raise ErrorVideo("Video no disponible")
        except exceptions.VideoPrivate:
            raise ErrorVideo("Video privado. No disponible para descargar")
        except exceptions.ExtractError:
            raise ErrorVideo("Error al extraer informacion del video")
        
    
    def download_video(self, quality: str, path: str, filename: str):
        stream = self.video.streams.filter(res=quality).first()
        print(stream)
        stream.download(output_path=path, filename=filename)
    
    def get_qualities_video(self):
        qualities = []

        for stream in self.video.streams.filter(file_extension='mp4'):
            res = stream.resolution
            if res not in qualities and res != None:
                qualities.append(stream.resolution)
        return qualities

    def get_title(self):
        self.video.title
    
    def get_url_miniature(self):
        return self.video.thumbnail_url
    
    def get_author(self):
        return self.video.author
    
    def get_duration(self):
        return self.video.length
    
    def get_publish_date(self):
        return self.video.publish_date
