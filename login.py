import tkinter as tk
from tkinter import ttk
from fomularios import *
from controlador_biblioteca import *
from tkinter import messagebox
import sqlite3
import subprocess
import sys
from PIL import Image, ImageTk, ImageDraw

def create_rounded_rectangle_image(width, height, radius, color):
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, width, height), radius=radius, fill=color)
    return image

def login(frame_principal, usuario, contrasena):
    conn = sqlite3.connect('BibliotecaCUC/bibliotecaCelsus.db')
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


def limpiar(frame):
    for widget in frame.winfo_children():
        widget.destroy()
# Función para crear la pantalla de login
def crear_pantalla_login(frame_principal):
    limpiar(frame_principal)

    imagen = Image.open("logo.png")
    imagen = imagen.resize((150, 200))
    img = ImageTk.PhotoImage(imagen)
    lbl_img = tk.Label(frame_principal, image=img, bg="white")
    lbl_img.image = img  # keep a reference to prevent garbage collection
    lbl_img.pack(pady=10)
    
    tk.Label(frame_principal,bg="white", text="Usuario:").pack(pady=0)
    usuario_entry = tk.Entry(frame_principal)
    usuario_entry.pack(pady=5)

    tk.Label(frame_principal, bg="white", text="Contraseña:").pack(pady=5)
    contrasena_entry = tk.Entry(frame_principal, show="*")
    contrasena_entry.pack(pady=5)

    login_button = tk.Button(frame_principal, text="Login",pady=5, padx=50, bg="black",fg="white",relief="flat", command=lambda: login(frame_principal, usuario_entry.get(), contrasena_entry.get()))
    login_button.pack(pady=10)

# Crear la ventana principal
root = tk.Tk()
root.title("Sistema de Login")
root.geometry("300x450")

frame_principal = tk.Frame(root, bg="white")
frame_principal.pack(expand=True, fill='both')

# Crear la pantalla de login al iniciar la aplicación
crear_pantalla_login(frame_principal)

root.protocol("WM_DELETE_WINDOW", root.destroy)

root.mainloop()