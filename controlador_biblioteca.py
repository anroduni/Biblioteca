import tkinter as tk
from modelo_biblioteca import *
from tkinter import ttk


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
        print("Inserting row:", row)  # Añadir impresión para verificar los datos
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

# Crear la ventana principal
#root = tk.Tk()
#root.geometry("800x600")

# Crear el frame principal
#frame_principal = ttk.Frame(root)
#frame_principal.pack(fill=tk.BOTH, expand=True)
    


def agregar(entries):
    
# Imprimir los valores actuales de las entradas
   valores = [entry[2].get() for entry in entries]
   respuesta=insertar(*valores)
   print(respuesta)
   
def actualizar(entries):
    
# Imprimir los valores actuales de las entradas
   valores = [entry[2].get() for entry in entries]
   respuesta=update(*valores)
   print(respuesta)
   
def eliminarid(entradas):
        
# Imprimir los valores actuales de las entradas
   valores = [entry[2].get() for entry in entradas]
   id=valores[0]
   respuesta=eliminar(id)
   print(respuesta)


#DESGLOZAR LOS VALORES Y COMPARARAR; SI LA TUPLA[?]ESTA VACIA ENTONCES MANDO MENSAJE DE POR FAVOR LLEVE EL VALOR DL CAMPO TAL, SI NO ESTA VACIO CONTINUO NORMALMENTE

 
#ENTONCES FALTA: VALIDAR DATOS ANTES DE CRUD, PRESTR Y OBTNEER DEVUELTA LIBROS, AGREGAR BARRA DE SCROLL A LA TABLA DE VER; COMO PLUS, EDITAR, ELIMINAR O PRESTAR/OBTENETR LIBRO DESDE LA TABLA VER