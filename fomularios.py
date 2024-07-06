import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
from modelo_biblioteca import versi, verpres, traerpres

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
        ("Nombre:", 1),
    ]

    # Limpiar la lista de entradas y destruir widgets existentes
    for entry in entradas:
        entry[0].destroy()
    entradas.clear()

    # Obtener los nombres de los libros desde versi()
    datos_libros = [("0", "Seleccione")] + versi()  # Agregar una opción de selección inicial

    # Crear nuevas entradas
    for text, row in campos:
        ttk.Label(frame_principal, text=text, font=("Georgia", 14), background="white").grid(column=0, row=row, **label_options)
        var = tk.StringVar()
        
        # Crear el Combobox con los nombres de los libros y configurarlo como solo lectura
        combobox = ttk.Combobox(frame_principal, textvariable=var, values=[nombre for _, nombre in datos_libros], font=("Georgia", 14), state='readonly')
        combobox.grid(column=1, row=row, **entry_options)
        combobox.current(0)  # Establecer "Seleccione" como la opción inicial y no seleccionable
        
        entradas.append((combobox, row, var, datos_libros))  # Guardar también los datos completos del libro

    return entradas


# Lista para almacenar las entradas
entro = []

def form_prestar(frame_principal):
    global entro  # Accede a la variable global

    # Configurar la cuadrícula del frame principal
    for i in range(2):
        frame_principal.grid_columnconfigure(i, weight=1)
    for i in range(10):
        frame_principal.grid_rowconfigure(i, weight=1)

    label_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}
    entry_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}

    campos = [
        ("Solicitante:", 1),
        ("Carrera:", 2),
        ("Fecha inicio:", 3),
        ("Fecha a entregarlo:", 4),
        ("Nombre del libro:", 5),
        ("Estatus:", 6),
    ]

    # Limpiar la lista de entro y destruir widgets existentes
    for entry in entro:
        if isinstance(entry, dict):  # Saltar el diccionario de ids de libros
            continue
        entry[0].destroy()
    entro.clear()

    # Obtener la lista de libros disponibles desde la base de datos
    libros_disponibles = versi()
    nombres_libros = [libro[1] for libro in libros_disponibles]
    id_libros = {libro[1]: libro[0] for libro in libros_disponibles}
    # Crear nuevas entradas
    for text, row in campos:
        ttk.Label(frame_principal, text=text, font=("Georgia", 14), background="white").grid(column=0, row=row, **label_options)
        
        if "Fecha" in text:
            # Usar DateEntry para fechas
            var = tk.StringVar()
            entry = DateEntry(frame_principal, font=("Georgia", 14), bg="white", textvariable=var, date_pattern='yyyy-mm-dd')
        elif text == "Estatus:":
            # Usar Combobox para el estado
            var = tk.StringVar()
            entry = ttk.Combobox(frame_principal, font=("Georgia", 14), textvariable=var, state='readonly')
            entry['values'] = ('Prestado')
           
        elif text == "Nombre del libro:":
            # Usar Combobox para los nombres de libros
            var = tk.StringVar()
            entry = ttk.Combobox(frame_principal, font=("Georgia", 14), textvariable=var, state='readonly')
            entry['values'] = nombres_libros
        else:
            # Usar Entry normal para otros campos
            var = tk.StringVar()
            entry = tk.Entry(frame_principal, font=("Georgia", 14), bg="white", textvariable=var)
        
        entry.grid(column=1, row=row, **entry_options)
        entro.append((entry, row, var))

    # Añadir el diccionario de ids de libros al final de la lista
    entro.append(id_libros)

    return entro



# Lista para almacenar las entradas
regso = []
# Función para crear el formulario de devolución
def form_regreso(frame_principal):
    global regso  # Accede a la variable global

    # Configurar la cuadrícula del frame principal
    for i in range(2):
        frame_principal.grid_columnconfigure(i, weight=1)
    for i in range(10):
        frame_principal.grid_rowconfigure(i, weight=1)

    label_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}
    entry_options = {'padx': 10, 'pady': 10, 'sticky': 'EW'}

    campos = [
        ("Nombre del libro que reingresa:", 1),
        ("Estatus:", 2),
    ]

    # Limpiar la lista de regso y destruir widgets existentes
    for entry in regso:
        if isinstance(entry, dict):  # Saltar el diccionario de ids de libros
            continue
        entry[0].destroy()
    regso.clear()

    # Obtener la lista de libros prestados desde la base de datos
    libros_prestados = traerpres()
    libros_dict = {libro[2]: (libro[1], libro[0]) for libro in libros_prestados}  # Nombre del libro -> (ID, Estatus)

    # Crear nuevas entradas
    var_libro = tk.StringVar()
    var_estatus = tk.StringVar()

    for text, row in campos:
        ttk.Label(frame_principal, text=text, font=("Georgia", 14), background="white").grid(column=0, row=row, **label_options)
        
        if text == "Estatus:":
            # Usar Combobox para el estado
            entry = ttk.Combobox(frame_principal, font=("Georgia", 14), textvariable=var_estatus, state='readonly')
            entry['values'] = ('Devuelto')
        elif text == "Nombre del libro que reingresa:":
            # Usar Combobox para los nombres de libros prestados
            entry = ttk.Combobox(frame_principal, font=("Georgia", 14), textvariable=var_libro, state='readonly')
            entry['values'] = list(libros_dict.keys())
        else:
            continue
        
        entry.grid(column=1, row=row, **entry_options)
        regso.append((entry, row, var_libro, var_estatus, libros_dict))
        
    return var_libro, var_estatus, libros_dict
