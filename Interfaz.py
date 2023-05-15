import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from idlelib.tooltip import Hovertip

class EntryWithPlaceholder(tk.Entry):
    def __init__(self, master=None, placeholder="", color='#471F6F', *args, **kwargs):
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
    Hovertip(label_directorio, directorio)
    if directorio == "":
        label_directorio["text"] = "Seleccione el directorio"


# Interfaz
root = tk.Tk()
root.geometry("400x300")
root.title("I2meta")
root.resizable(False, False)
root.configure(bg="#F7F3E3")

# Widgets
entry_url = EntryWithPlaceholder(root, placeholder="Ingrese la URL", width=35, bg='#6FB8EC')
entry_nombre = EntryWithPlaceholder(root, placeholder="Ingrese el nombre del archivo", width=35, bg='#6FB8EC')
label_directorio = ttk.Label(root, text="Seleccione el directorio", width=25, background='#6FB8EC')
##Cambiar el color del texto del label.
directorio_button = tk.Button(root, text="Explorar", command=explorar_directorio, width=6, bg='#6FB8EC', fg='#F7F3E3')
label_calidad = ttk.Label(root, text="Calidad:", background='#F7F3E3')
calidades = ["Baja", "Media", "Alta"]
##Cambiar el color del desplegable.
var_calidad = tk.StringVar(root)
var_calidad.set(calidades[0])
option_calidad = tk.OptionMenu(root, var_calidad, *calidades)
option_calidad.config(width=6, background='#6FB8EC', fg="#F7F3E3")
label_formato = ttk.Label(root, text="Formato:", background='#F7F3E3')
var_tipo = tk.StringVar()
var_tipo.set("video")
radio_video = ttk.Radiobutton(root, text="Video", variable=var_tipo, value="video")
radio_audio = ttk.Radiobutton(root, text="Audio", variable=var_tipo, value="audio")
##Cambiar los fondos de los radiobutton.
button_descargar = ttk.Button(root, text="Descargar", style='my.TButton')

# Estilos
style = ttk.Style()
style.configure('my.TButton', font=('Segoe UI', 10), background='#6FB8EC', foreground='#F7F3E3', width=10)

# Posiciones
entry_url.place(x=15, y=10)
entry_nombre.place(x=15, y=50)
label_directorio.place(x=15, y=90)
directorio_button.place(x=282, y=87)
label_calidad.place(x=20, y=140)
option_calidad.place(x=110, y=133)
label_formato.place(x=20, y=180)
radio_video.place(x=110, y=180)
radio_audio.place(x=200, y=180)
button_descargar.place(x=150, y=220)

# Inicio
root.mainloop()
