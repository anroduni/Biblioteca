import tkinter as tk
from modelo_biblioteca import *
from tkinter import ttk


def tabla(frame_principal):
    data = ver()

  # Establecer el estilo para el Treeview
    style = ttk.Style()
    style.theme_use("default")
    style.configure("Custom.Treeview", background="lightblue", fieldbackground="lightblue", rowheight=25, font=('Arial', 16, 'bold'))
    style.configure("Custom.Treeview.Heading", background="gray20", foreground="red", font=('Arial', 20, 'bold'))

    # Aplicar el estilo alternativo para las filas
    style.map("Custom.Treeview",
              background=[('selected', 'blue')],
              foreground=[('selected', 'white')])



    # Crear el Treeview con las columnas especificadas y aplicar el estilo
    columns = ("ID", "Titulo", "Editorial", "Numero de edicion", "Año publicacion", "Paginas", "Rama", "ISBN", "Publicacion")
    tree = ttk.Treeview(frame_principal, columns=columns, show="headings", style="Custom.Treeview")

    # Definir encabezados de columnas
    for col in columns:
        tree.heading(col, text=col)

    # Definir el ancho de las columnas
    for col in columns:
        tree.column(col, width=100)
    

    
    # Insertar datos en la tabla
    for row in data:
        print("Inserting row:", row)  # Añadir impresión para verificar los datos
        tree.insert("", tk.END, values=row)
    
    # Empaquetar el Treeview
    
    tree.pack(fill=tk.BOTH, expand=True)
    


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