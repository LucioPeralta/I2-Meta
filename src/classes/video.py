from pytube import YouTube
from pytube import exceptions
from src.classes.error_descarga import ErrorVideo

class Video:
    
    def __init__(self, url: str):
        self.url_video = url
        self.fetch_video()

    def fetch_video(self):
        try:
            self.video = YouTube(self.url_video)
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
        stream.download(output_path=path, filename=filename)

    
    def get_qualities_video(self):
        qualities = []
        streams = self.video.streams.filter(type="video")

        for stream in streams:
            res = stream.resolution
            if res not in qualities and res is not None:
                qualities.append(res)

        qualities.sort()  # Ordenar la lista en orden ascendente

        return qualities

    def get_qualities_audio(self):
        audio_streams = []
        for stream in self.video.streams.all():
            if stream.type == "audio":
                audio_streams.append(stream)

        qualities = []

        for stream in audio_streams:
            res = stream.abr
            if res not in qualities and res is not None:
                qualities.append(res)

        qualities.sort(key=lambda x: int(x[:-4]))  # Ordenar la lista en orden ascendente
        return qualities

    def get_title(self):
        return self.video.title
    
    def get_url_miniature(self):
        return self.video.thumbnail_url
    
    def get_author(self):
        return self.video.author
    
    def get_duration(self):
        return self.video.length
    
    def get_publish_date(self):
        return self.video.publish_date
