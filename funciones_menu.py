import tkinter as tk
from tkinter import ttk
from fomularios import *
from controlador_biblioteca import *
from tkinter import messagebox
from PIL import Image, ImageTk

def funcion_ver(frame_principal):
    limpiar(frame_principal)
    tabla(frame_principal)

def funcion_verprestados(frame_principal):
    limpiar(frame_principal)
    tabla_prestados(frame_principal)
    
def funcion_agregar(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Agregar", font=("Helvetica", 22, "bold"), bg="gray61", fg="white")
    entries = fomulario(frame_principal)
    ttk.Button(frame_principal, text="Agregar", command=lambda: agregar(entries)).grid(column=0, row=11, columnspan=2, pady=10, sticky='NSEW')

def funcion_editar(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Editar", font=("Helvetica", 22, "bold"), bg="gray61", fg="white")
    label.grid(column=0, row=0, columnspan=2, pady=10, sticky='NSEW')
    entries = fomulario(frame_principal)
    ttk.Button(frame_principal, text="Editar", command=lambda: actualizar(entries)).grid(column=0, row=11, columnspan=2, pady=10, sticky='NSEW')


def funcion_eliminar(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Eliminar", font=("Helvetica", 22, "bold"), bg="gray61", fg="white")
    label.grid(column=0, row=0, columnspan=2, pady=10, sticky='NSEW')
    entries = formeliminar(frame_principal)
    ttk.Button(frame_principal, text="Eliminar", command=lambda: eliminarid(entries)).grid(column=0, row=11, columnspan=2, pady=10, sticky='NSEW')

def funcion_prestar(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Prestar", font=("Helvetica", 22, "bold"), bg="gray61", fg="white")
    label.grid(column=0, row=0, columnspan=2, pady=10, sticky='NSEW')
    entries = form_prestar(frame_principal)
    ttk.Button(frame_principal, text="Prestar", command=lambda: prestar(entries)).grid(column=0, row=11, columnspan=2, pady=10, sticky='NSEW')

def funcion_reingreso(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Reingresar", font=("Helvetica", 22, "bold"), bg="gray61", fg="white")
    label.grid(column=0, row=0, columnspan=2, pady=10, sticky='NSEW')
    entries = form_regreso(frame_principal)
    ttk.Button(frame_principal, text="Reingresar", command=lambda: regresar(entries)).grid(column=0, row=11, columnspan=2, pady=10, sticky='NSEW')

def salir(frame_principal):
    for widget in frame_principal.winfo_children():
        widget.destroy()


def limpiar(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def mostrar_grafica(frame_principal, incluir_todos_los_libros=False):
    limpiar(frame_principal)
    # Limpiar el frame_principal
    for widget in frame_principal.winfo_children():
        widget.destroy()
    
    # Generar el gráfico
    grafica(incluir_todos_los_libros)
    
    # Cargar la imagen del gráfico
    imagen = Image.open('grafico_prestamos.png')
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Crear un widget Label para mostrar la imagen
    label_imagen = ttk.Label(frame_principal, image=imagen_tk)
    label_imagen.image = imagen_tk  # Necesario para evitar que la imagen sea recolectada por el garbage collector
    label_imagen.pack(padx=10, pady=10)