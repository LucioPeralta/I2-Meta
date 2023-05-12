#Interfaz para ver un video von tkinter
from tkinter import *
from tkinter import messagebox as MessageBox  
from tkinter import filedialog
import subprocess

def screen_size():
    size = (None, None)
    args = ["xrandr", "-q", "-d", ":0"]
    proc = subprocess.Popen(args,stdout=subprocess.PIPE)
    for line in proc.stdout:
        if isinstance(line, bytes):
            line = line.decode("utf-8")
            if "Screen" in line:
                withd = int(line.split()[7])
                heigth= int(line.split()[9][:-1])
                size = [round(withd*0.3), round(heigth*0.3)]
                size = str(size[0])+"x"+str(size[1])+ "+100+100"
    return size


base = Tk()
base.title("Prueba")
base.geometry(screen_size())
base.config(background="grey")
base.resizable(width=False, height=True)

Url = Entry(base, width=40, background="grey", fg="black", justify="left")
Url.grid(row=0, column=0, padx=10, pady=15, columnspan=3)

Nombre = Entry(base, width=40, background="grey", fg="black", justify="left")
Nombre.grid(row=1, column=0, padx=10, pady=0, columnspan=3)

Ruta = Entry(base, width=40, background="grey", fg="black", justify="left") 
Ruta.grid(row=2, column=0, padx=10, pady=15, columnspan=3)

Formato = OptionMenu(base, "Formato", "Audio", "Video")
Formato.config(width=8, background="grey", fg="black", justify="center")
Formato["menu"].config(background="grey", fg="black")
Formato.grid(row=1, column=3, padx=10, pady=1, columnspan=3)

Descargar = Button(base, text="Descargar", width=10, height=1, background="black", fg="grey", justify="center")
Descargar.grid(row=0, column=3, padx=10, pady=15)

Calidad = OptionMenu(base, "Calidad", "Alta", "Media", "Baja")
Calidad.grid(row=2, column=3, padx=10, pady=15)
Calidad.config(width=8, background="grey", fg="black", justify="center")

base.mainloop()
