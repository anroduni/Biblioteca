import tkinter as tk
from modelo_biblioteca import *
from tkinter import ttk
from tkinter import messagebox

def tabla(frame_principal):
    data = ver()

    # Establecer el estilo para el Treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.Treeview", background="white", fieldbackground="gray50", rowheight=25, font=('Arial', 12, 'bold'))
    style.configure("Custom.Treeview.Heading", background="gray20", foreground="white", font=('Arial', 16, 'bold'))

    # Aplicar el estilo alternativo para las filas
    style.map("Custom.Treeview",
              background=[('selected', 'gray50')],
              foreground=[('selected', 'white')])

    # Crear el Frame que contendrá el Treeview y las Scrollbars
    container = ttk.Frame(frame_principal)
    container.pack(fill=tk.BOTH, expand=True)

    # Crear el Treeview con las columnas especificadas y aplicar el estilo
    columns = ("ID", "Titulo", "Editorial", "N° de edicion", "Año publicacion", "Paginas", "Rama", "ISBN", "Publicacion")
    tree = ttk.Treeview(container, columns=columns, show="headings", style="Custom.Treeview")

    # Definir encabezados de columnas
    for col in columns:
        tree.heading(col, text=col)

    # Insertar datos en la tabla
    for row in data:
        #print("Inserting row:", row)  # Añadir impresión para verificar los datos
        tree.insert("", tk.END, values=row)

    # Crear las Scrollbars y configurarlas para trabajar con el Treeview
    scrollbar_vertical = ttk.Scrollbar(container, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_horizontal = ttk.Scrollbar(container, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Colocar el Treeview y las Scrollbars en el container
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar_vertical.grid(row=0, column=1, sticky='ns')
    scrollbar_horizontal.grid(row=1, column=0, sticky='ew')

    # Hacer que el container cambie de tamaño con la ventana
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

def tabla_prestados(frame_principal):
    data = verpres()

    # Establecer el estilo para el Treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.Treeview", background="white", fieldbackground="gray50", rowheight=25, font=('Arial', 12, 'bold'))
    style.configure("Custom.Treeview.Heading", background="gray20", foreground="white", font=('Arial', 16, 'bold'))

    # Aplicar el estilo alternativo para las filas
    style.map("Custom.Treeview",
              background=[('selected', 'gray50')],
              foreground=[('selected', 'white')])

    # Crear el Frame que contendrá el Treeview y las Scrollbars
    container = ttk.Frame(frame_principal)
    container.pack(fill=tk.BOTH, expand=True)

    # Crear el Treeview con las columnas especificadas y aplicar el estilo
    columns = ("ID", "Solicitante", "Carrera", "Fecha Inicio", "Fecha Fin", "Libro ID", "Estatus")
    tree = ttk.Treeview(container, columns=columns, show="headings", style="Custom.Treeview")

    # Definir encabezados de columnas
    for col in columns:
        tree.heading(col, text=col)

    # Insertar datos en la tabla
    for row in data:
        tree.insert("", tk.END, values=row)

    # Crear las Scrollbars y configurarlas para trabajar con el Treeview
    scrollbar_vertical = ttk.Scrollbar(container, orient=tk.VERTICAL, command=tree.yview)
    scrollbar_horizontal = ttk.Scrollbar(container, orient=tk.HORIZONTAL, command=tree.xview)
    tree.configure(yscrollcommand=scrollbar_vertical.set, xscrollcommand=scrollbar_horizontal.set)

    # Colocar el Treeview y las Scrollbars en el container
    tree.grid(row=0, column=0, sticky='nsew')
    scrollbar_vertical.grid(row=0, column=1, sticky='ns')
    scrollbar_horizontal.grid(row=1, column=0, sticky='ew')

    # Hacer que el container cambie de tamaño con la ventana
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    return tree
def agregar(entries):
    # Validar si alguna entrada está vacía
    if any(not entry[2].get() for entry in entries):
        mostrar_mensaje("Por favor completa todos los campos.")
        return
    
    # Si todas las entradas tienen valores, proceder con insertar
    valores = [entry[2].get() for entry in entries]
    respuesta = insertar(*valores)
    mostrar_mensaje(respuesta)

def actualizar(entries):
    # Validar si alguna entrada está vacía
    if any(not entry[2].get() for entry in entries):
        mostrar_mensaje("Por favor completa todos los campos.")
        return
    
    # Si todas las entradas tienen valores, proceder con actualizar
    valores = [entry[2].get() for entry in entries]
    respuesta = update(*valores)
    mostrar_mensaje(respuesta)

def prestar(entradas):
    # Validar si alguna entrada está vacía
    if any(not entry[2].get() for entry in entradas[:-1]):
        mostrar_mensaje("Por favor completa todos los campos.")
        return
    
    # Si todas las entradas tienen valores, proceder con prestar
    valores = [entry[2].get() for entry in entradas[:-1]]
    id_libros = entradas[-1]
    
    # Reemplazar el nombre del libro con su id correspondiente
    nombre_libro = valores[4]
    valores[4] = id_libros[nombre_libro] if nombre_libro in id_libros else None
    
    respuesta = prestamos(*valores)
    mostrar_mensaje(respuesta)

# Función para procesar los valores recibidos del formulario
def regresar(entries):
    libro_seleccionado = entries[0].get()  # Obtener el nombre del libro seleccionado
    estatus_seleccionado = entries[1].get()  # Obtener el estatus seleccionado
    
    # Validar si alguna de las dos entradas está vacía
    if not libro_seleccionado or not estatus_seleccionado:
        mostrar_mensaje("Por favor completa todos los campos.")
        return
    #Manejo de estatus
    if estatus_seleccionado=="Seleccione":
        estatus_seleccionado="Devuelto"
    libros_dict = entries[2]  # Obtener el diccionario de libros

    # Obtener el ID del libro seleccionado
    id_libro = libros_dict[libro_seleccionado][0]
    respuesta = atc_estatus(id_libro, estatus_seleccionado)
    mostrar_mensaje(respuesta)


def eliminarid(entradas):
    # Obtener el ID seleccionado del Combobox
    id_seleccionado = entradas[0][3][entradas[0][0].current()][0]  # El ID está en la primera entrada (index 0)
    # Llamar a la función eliminarle con el ID seleccionado
    respuesta = eliminarle(id_seleccionado)
    # Mostrar el mensaje de respuesta en una ventana emergente
    messagebox.showinfo("Resultado", respuesta)
    

def mostrar_mensaje(mensaje):
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    messagebox.showinfo("Información", mensaje)
    root.destroy()

import matplotlib.pyplot as plt

def grafica(incluir_todos_los_libros=False):
    prestamos, libros = obtener_datos_prestamos()

    # Crear un diccionario para contar los préstamos
    conteo_prestamos = {libro_id: 0 for libro_id, _ in libros}
    
    for libro_id, count in prestamos:
        conteo_prestamos[libro_id] = count
    
    if not incluir_todos_los_libros:
        conteo_prestamos = {libro_id: count for libro_id, count in conteo_prestamos.items() if count > 0}
    
    # Preparar los datos para el gráfico
    nombres_libros = [nombre for _, nombre in libros if _ in conteo_prestamos]
    conteos = [conteo_prestamos[_] for _, nombre in libros if _ in conteo_prestamos]
    
    # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(nombres_libros, conteos, color='skyblue')
    plt.xlabel('Libros')
    plt.ylabel('Número de Préstamos')
    plt.title('Cantidad de Préstamos por Libro')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Guardar el gráfico como imagen
    plt.savefig('grafico_prestamos.png')
