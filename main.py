import tkinter as tk
from estructura import crear_menu_lateral, crear_frame_principal
from funciones_menu import *


def main():
    ventana = tk.Tk()
    ventana.geometry("1200x800")
    ventana.title("Biblioteca")

    menu_lateral = crear_menu_lateral(ventana)
    menu_lateral.pack(side="left", fill="y")
    frame_principal = crear_frame_principal(ventana)
    frame_principal.pack(side="left", fill="both", expand=True)

    botones = [
        
        ("Ver", lambda: funcion_ver(frame_principal)),
        ("Agregar", lambda: funcion_agregar(frame_principal)),
        ("Editar", lambda: funcion_editar(frame_principal)),
        ("Eliminar", lambda: funcion_eliminar(frame_principal)),
        ("Prestar", lambda: funcion_prestar(frame_principal)),
        ("Ver prestados", lambda: funcion_verprestados(frame_principal)),
        ("Reingresar prestados", lambda: funcion_reingreso(frame_principal))
        
    ]

    for text, command in botones:
        btn = tk.Button(menu_lateral, text=text, command=command, font=("Helvetica", 14), height=2)
        btn.pack(fill="x", padx=10, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    main()
