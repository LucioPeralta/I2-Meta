from classes.video import Video
from tkinter import *
from tkinter import messagebox as MessageBox
from pathlib import Path
from Interfaz import *

import traceback



def descargar_video(url, titulo, calidad):
    video = Video(url)
    filename = titulo+".mp4" if titulo else video.get_title()+".mp4"
    video.download_video(calidad, Path.cwd(), filename)
    print(f"El {filename} de la url {url} se ha descargado correctamente.")
    return filename


def descargar_audio(url , titulo):
    video = Video(url)
    filename = titulo+".mp4" if titulo else video.get_title()+".mp4"
    video.download_audio(Path.cwd(), filename)
    return filename

def buscar_video(url: str, funcion):
    if not "https://www.youtube.com/watch?v=" in url:
        return None
    video = Video(url)
    funcion(video.get_qualities_video())


def Descarga_general(url, titulo, tipo, calidad):
    if tipo == "video":
        try:
            filename = descargar_video(url, titulo, calidad)
            MessageBox.showinfo("Descarga completa", f"El archivo de video {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de video: {str(e)}")
    elif tipo == "audio":
        try:
            filename = descargar_audio(url, titulo)
            MessageBox.showinfo("Descarga completa", f"El archivo de audio {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de audio: {str(e)}")
            traceback.print_exc()
    else:
        MessageBox.showwarning("Seleccion invalida", "Por favor seleccione el tipo de archivo que desea descargar.")
