from pytube import YouTube
from pytube import exceptions

class Video:
    
    def __init__(self, url: str):
        self.url_video = url
        self.fetch_video()

    def fetch_video(self):
        self.video = YouTube(self.url_video, 
                             on_complete_callback=self.complete_download, 
                             on_progress_callback=self.progress_download
                             )        
        try:
            self.video.streams
        except exceptions.VideoUnavailable: #url inexistente
            print("Url inexistente")

    
    def download_video(self, 
                       higher_quality: bool, 
                       download_path=None):
        # Este condicional es provisional, porque mejor seria tener una lista de resoluciones
        # y seleccionar el que deseemos
        if higher_quality:
            stream = self.video.streams.get_highest_resolution()
        else:
            stream = self.video.streams.get_lowest_resolution()
        
        if download_path:
            stream.download(output_path=download_path)
            return
        stream.download()


    def download_audio(self):
        stream = self.video.streams.get_audio_only()
        stream.download()

    def complete_download(self, streams, filepath):
        print("Descarga finalizada")

    def progress_download(self, streams, chunks, bytes_remaining):
        print("a")
        #no anda xd 
    
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
    


