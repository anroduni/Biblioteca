import tkinter as tk

def crear_menu_lateral(ventana):
    menu_lateral = tk.Frame(ventana, bg="white", width=250, height=800)
    return menu_lateral

def crear_frame_principal(ventana):
    frame_principal = tk.Frame(ventana, bg="white")
    return frame_principal
