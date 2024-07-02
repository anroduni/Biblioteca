import tkinter as tk
from tkinter import ttk

# Lista para almacenar las entradas
entries = []

def fomulario(frame_principal):
    global entries  # Accede a la variable global

    for i in range(2):
        frame_principal.grid_columnconfigure(i, weight=1)
    for i in range(10):
        frame_principal.grid_rowconfigure(i, weight=1)

    label_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}
    entry_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}

    campos = [
        ("ID:", 1),
        ("Título:", 2),
        ("Autor:", 3),
        ("Editorial:", 4),
        ("Número de Edición:", 5),
        ("Año de Publicación:", 6),
        ("Páginas:", 7),
        ("Rama:", 8),
        ("ISBN:", 9),
        ("Ubicación:", 10)
    ]

    # Limpiar la lista de entries y destruir widgets existentes
    for entry in entries:
        entry[0].destroy()
    entries.clear()

    # Crear nuevas entradas
    for text, row in campos:
        ttk.Label(frame_principal, text=text, font=("Georgia", 14), background="white").grid(column=0, row=row, **label_options)
        var = tk.StringVar()
        entry = tk.Entry(frame_principal, font=("Georgia", 14), bg="white", textvariable=var)
        entry.grid(column=1, row=row, **entry_options)
        entries.append((entry, row, var))

    return entries



# Lista para almacenar las entradas
entradas = []

def formeliminar(frame_principal):
    global entradas  # Accede a la variable global

    for i in range(2):
        frame_principal.grid_columnconfigure(i, weight=1)
    for i in range(10):
        frame_principal.grid_rowconfigure(i, weight=1)

    label_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}
    entry_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}

    campos = [
        ("ID:", 1),
    ]

    # Limpiar la lista de entradas y destruir widgets existentes
    for entry in entradas:
        entry[0].destroy()
    entradas.clear()

    # Crear nuevas entradas
    for text, row in campos:
        ttk.Label(frame_principal, text=text, font=("Georgia", 14), background="white").grid(column=0, row=row, **label_options)
        var = tk.StringVar()
        entry = tk.Entry(frame_principal, font=("Georgia", 14), bg="white", textvariable=var)
        entry.grid(column=1, row=row, **entry_options)
        entradas.append((entry, row, var))


    return entradas