from pytube import YouTube
from tkinter import *
from tkinter import messagebox as MessageBox
from pathlib import Path


def descargar_video(url):
    video = YouTube(url)
    titulo = video.title
    filename = titulo + ".mp4"
    stream = video.streams.get_highest_resolution()
    stream.download(output_path=Path.cwd(), filename=filename)
    return filename


def descargar_audio(url):
    video = YouTube(url)
    stream = video.streams.filter(only_audio=True).first()
    titulo = video.title
    filename = titulo + ".mp3"
    stream.download(output_path=Path.cwd(), filename=filename)
    return filename


def accion():
    enlace = videos.get()
    if var.get() == 1:
        try:
            filename = descargar_video(enlace)
            MessageBox.showinfo("Descarga completa", f"El archivo de video {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de video: {str(e)}")
    elif var.get() == 2:
        try:
            filename = descargar_audio(enlace)
            MessageBox.showinfo("Descarga completa", f"El archivo de audio {filename} se ha descargado correctamente.")
        except Exception as e:
            MessageBox.showerror("Error", f"Se ha producido un error al descargar el archivo de audio: {str(e)}")
    else:
        MessageBox.showwarning("Seleccion invalida", "Por favor seleccione el tipo de archivo que desea descargar.")


def popup():
    MessageBox.showinfo("Sobre mi", "")


root = Tk()
root.config(bd=15)
root.title("Youtube Downloader")


menubar = Menu(root)
root.config(menu=menubar)
helpmenu = Menu(menubar, tearoff=0)

menubar.add_cascade(label="Para mas info", menu=helpmenu)
helpmenu.add_cascade(label="Info", command=popup)
menubar.add_cascade(label="Salir", command=root.destroy)

instrucciones = Label(root, text="Programa para descargar videos o audio ;)")
instrucciones.grid(row=0, column=1)

videos = Entry(root)
videos.grid(row=1, column=1)

var = IntVar()
rb_video = Radiobutton(root, text="Video", variable=var, value=1)
rb_video.grid(row=2, column=1, sticky=W)

rb_audio = Radiobutton(root, text="Audio", variable=var, value=2)
rb_audio.grid(row=3, column=1, sticky=W)

boton = Button(root, text="Descargar", command=accion)
boton.grid(row=4, column=1)

root.mainloop()
