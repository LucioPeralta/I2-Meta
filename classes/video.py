from pytube import YouTube
from pytube import exceptions

class Video:
    
    def __init__(self, url: str):
        self.url_video = url
        self.fetch_video()

    def fetch_video(self):
        if self.url_video == "":
            return None
        self.video = YouTube(self.url_video, on_complete_callback=self.complete_download, on_progress_callback=self.progress_download)        
        try:
            self.video.streams
        except exceptions.VideoUnavailable: #url inexistente
            print("Url inexistente")

    
    def download_video(self, quality: str, path: str, filename: str):
        stream = self.video.streams.filter(res=quality).first()
        stream.download(output_path=path, filename=filename)

    def download_audio(self, path, filename):
        stream = self.video.streams.get_audio_only()
        stream.download(output_path=path, filename=filename)

    def complete_download(self, streams, filepath):
        print("Descarga finalizada")

    def progress_download(self, streams, chunks, bytes_remaining):
        print("")
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
    


