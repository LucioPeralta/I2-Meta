<<<<<<< HEAD
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
=======
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from main import Descarga_general, buscar_video
from classes.video import Video

calidades = [""]

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", color='#DBEDFA', *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.placeholder = placeholder
        self.placeholder_color = color
        self.default_fg_color = self['fg']
        self.bind("<FocusIn>", self._clear_placeholder)
        self.bind("<FocusOut>", self._add_placeholder)
        self._add_placeholder()

    def _clear_placeholder(self, event):
        if self['fg'] == self.placeholder_color:
            self.delete(0, tk.END)
            self.config(fg=self.default_fg_color)

    def _add_placeholder(self, event=None):
        if not self.get():
            self.insert(0, self.placeholder)
            self.config(fg=self.placeholder_color)

def explorar_directorio():
    directorio = filedialog.askdirectory()
    label_directorio["text"] = directorio
    if directorio == "":
        label_directorio["text"] = "Seleccione el directorio"


# Interfaz
root = tk.Tk()
root.geometry("400x300")
root.title("I2meta")
root.resizable(True, True)
root.configure(bg="#35355A")

# Widgets
url_update = tk.StringVar()
entry_url = EntryWithPlaceholder(root, textvariable=lambda: print("saad"), placeholder="Ingrese la URL", width=25, bg='#444474', highlightthickness=0, foreground='#DBEDFA')


button_buscar = tk.Button(root, command=lambda: buscar_video(entry_url.get(), agregarCualidadesOptionMenu),text="Buscar", width=6, bg='#444474', fg='#DBEDFA', highlightthickness=0)
button_buscar.config(activebackground='#DBEDFA', activeforeground='#471F6F')

entry_nombre = EntryWithPlaceholder(root, placeholder="Ingrese el nombre del archivo", width=35, bg='#444474', highlightthickness=0, foreground='#DBEDFA')

label_directorio = ttk.Label(root, text="Seleccione el directorio", width=25, background='#35355A', foreground="#DBEDFA")
directorio_button = tk.Button(root, text="Explorar", command=explorar_directorio, width=6, bg='#444474', fg='#DBEDFA', highlightthickness=0)
directorio_button.config(activebackground='#DBEDFA', activeforeground='#471F6F')

label_calidad = ttk.Label(root, text="Calidad:",background='#35355A', foreground="#DBEDFA")
calidades = calidades
var_calidad = tk.StringVar(root)
var_calidad.set(calidades[0])
option_calidad = tk.OptionMenu(root, var_calidad, *calidades)
option_calidad.config(width=6, background='#DBEDFA', foreground='#444474',activebackground='#444474', activeforeground='#DBEDFA')
option_calidad["menu"].config(bg='#DBEDFA', fg="#444474", activebackground='#444474', activeforeground='#DBEDFA')

label_formato = ttk.Label(root, text="Formato:", background='#35355A', foreground="#F7F3E3")
var_tipo = tk.StringVar()
var_tipo.set("video")
radio_video = ttk.Radiobutton(root, text="Video", variable=var_tipo, value="video", style='RB.TRadiobutton' )
radio_audio = ttk.Radiobutton(root, text="Audio", variable=var_tipo, value="audio", style='RB.TRadiobutton')

##Cambiar los fondos de los radiobutton.
button_descargar = tk.Button(root, command=lambda: Descarga_general(entry_url.get(), entry_nombre.get(), var_tipo.get(), var_calidad.get(), label_directorio['text']),text="Descargar")
button_descargar.config(width=10, background='#DBEDFA', foreground='#444474',activebackground='#444474', activeforeground='#DBEDFA')
# Estilos
style_rb = ttk.Style()
style_rb.configure('RB.TRadiobutton', foreground='#444474', background='#DBEDFA')
# Posiciones
entry_url.place(x=15, y=13)
entry_nombre.place(x=15, y=50)
label_directorio.place(x=15, y=90)
directorio_button.place(x=282, y=87)
label_calidad.place(x=20, y=140)
option_calidad.place(x=110, y=133)
label_formato.place(x=20, y=180)
radio_video.place(x=110, y=180)
radio_audio.place(x=200, y=180)
button_descargar.place(x=150, y=220)
button_buscar.place(x=282, y=10)

def agregarCualidadesOptionMenu(calidades: list):
    option_calidad["menu"].delete(0, "end")
    for calidad in calidades:
        option_calidad["menu"].add_command(label=calidad, command=lambda value=calidad: var_calidad.set(value))
"""
def update(*args):
    video = Video(url_update.get())
    calidades = video.get_qualities_video()
    # calidades = Video(url_update.get()).get_qualities_video()
    # calidades.remove("")
    var_calidad.set(calidades[0])
    option_calidad.option_clear()
    menu = option_calidad["menu"]
    for i in range(menu.index("end")):
        menu.delete(i)
    for string in calidades:
        menu.add_command(label=string, command=lambda value=string: var_calidad.set(value))
        
url_update.trace_add("write", update)"""

root.mainloop()
>>>>>>> develop
