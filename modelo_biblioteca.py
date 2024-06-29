# Este archivo contiene funciones para interactuar con una base de datos SQLite que almacena información de una biblioteca.
# Las funciones incluyen ver todos los libros, insertar un nuevo libro, actualizar la información de un libro y eliminar un libro.

def ver():
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar la consulta
    cursor.execute('''SELECT * FROM libros''')

    # Obtener todos los resultados
    datos = cursor.fetchall()

    #Cerrar cursor
    cursor.close()
    # Cerrar la conexión
    conexion.close()
    
    return datos




def insertar(ID, Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion):
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar la consulta
    cursor.execute('''
        INSERT INTO libros (
            ID, Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (ID, Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion))

    # Confirmar los cambios
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    return "Libro guardado"


def update(ID, Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion):
    import sqlite3 as sql
    
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")
    cursor = conexion.cursor()
    
    # Actualizar el registro
    cursor.execute('''
        UPDATE libros
        SET Titulo = ?, Autor = ?, Editorial = ?, Num_Edicion = ?, Año_publicacion = ?, paginas = ?, rama = ?, ISBN = ?, ubicacion = ?
        WHERE ID = ?
    ''', (Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion, ID))
    
    # Confirmar los cambios
    conexion.commit()
    
    # Cerrar la conexión
    conexion.close()
    
    return "Actualizado correctamente"



def eliminar(ID):
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")
    cursor = conexion.cursor()

    # Ejecutar la consulta de eliminación
    cursor.execute('''
        DELETE FROM libros
        WHERE ID = ?
    ''', (ID)) 

    # Confirmar los cambios
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    return "Libro eliminado"

