from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
from pathlib import Path
from Interfaz import *



def descargar_video(url, titulo):
    video = YouTube(url)
    
    filename = titulo + ".mp4"
    stream = video.streams.get_Quality()
    stream.download(output_path=Path.cwd(), filename=filename)
    print(f"EL {filename} de la url {url} se ha descargado correctamente. ")
    return filename


def descargar_audio(url):
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    titulo = video.title
    filename = titulo + ".mp3"
    stream.download(output_path=Path.cwd(), filename=filename)
    return filename


def Descarga_general(url, titulo, tipo):
    if tipo == "video":
        try:
            filename = descargar_video(url, titulo)
            MessageBox.showinfo("Descarga completa", f"El archivo de video {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de video: {str(e)}")
    elif tipo == "audio":
        try:
            filename = descargar_audio(url, titulo)
            MessageBox.showinfo("Descarga completa", f"El archivo de audio {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de audio: {str(e)}")
    else:
        MessageBox.showwarning("Seleccion invalida", "Por favor seleccione el tipo de archivo que desea descargar.")
