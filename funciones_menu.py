import tkinter as tk
from tkinter import ttk
from fomularios import *
from controlador_biblioteca import *
from tkinter import messagebox
import sqlite3
import subprocess
import sys

def limpiar(frame_principal):
    for root in frame_principal.winfo_children():
        root.destroy()


def funcion_inicio(frame_principal):
    limpiar(frame_principal)
    label = tk.Label(frame_principal, text="Inicio", font=("Helvetica", 16), bg="white")
    label.pack(expand=True, fill='both')

def funcion_ver(frame_principal):
    limpiar(frame_principal)
    tabla(frame_principal)


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

def login(frame_principal, usuario, contrasena):
    conn = sqlite3.connect('usuarios.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT * FROM usuarios WHERE usuario = ? AND contrasena = ?
    ''', (usuario, contrasena))

    usuario_encontrado = cursor.fetchone()
    conn.close()

    if usuario_encontrado:
        messagebox.showinfo("Login", "Acceso concedido.")
        root.destroy()
        root.quit()  # Cerrar la ventana actual
        subprocess.Popen(['python', 'main.py'])  # Ejecutar main.py
        
    else:
        messagebox.showerror("Login", "Acceso denegado. Credenciales incorrectas.")

# Función para crear la pantalla de login
def crear_pantalla_login(frame_principal):
    limpiar(frame_principal)
    
    tk.Label(frame_principal, text="Usuario:").pack(pady=5)
    usuario_entry = tk.Entry(frame_principal)
    usuario_entry.pack(pady=5)

    tk.Label(frame_principal, text="Contraseña:").pack(pady=5)
    contrasena_entry = tk.Entry(frame_principal, show="*")
    contrasena_entry.pack(pady=5)

    login_button = tk.Button(frame_principal, text="Login", command=lambda: login(frame_principal, usuario_entry.get(), contrasena_entry.get()))
    login_button.pack(pady=20)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Login")
root.geometry("300x200")

frame_principal = tk.Frame(root, bg="white")
frame_principal.pack(expand=True, fill='both')

# Crear la pantalla de login al iniciar la aplicación
crear_pantalla_login(frame_principal)

root.protocol("WM_DELETE_WINDOW", root.destroy)
root.mainloop()
