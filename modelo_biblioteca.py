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


def versi():
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar la consulta
    cursor.execute('''SELECT ID, Titulo FROM libros''')

    # Obtener todos los resultados
    datos = cursor.fetchall()

    #Cerrar cursor
    cursor.close()
    # Cerrar la conexión
    conexion.close()
    
    return datos

def verpres():
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")

    # Crear un cursor
    cursor = conexion.cursor()

    # Ejecutar la consulta
    cursor.execute('''SELECT * FROM prestar''')

    # Obtener todos los resultados
    datos = cursor.fetchall()

    #Cerrar cursor
    cursor.close()
    # Cerrar la conexión
    conexion.close()
    
    return datos

def traerpres():
    import sqlite3 as sql
    try:
        # Conectar a la base de datos
        conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")
        cursor = conexion.cursor()

        cursor.execute('''
            SELECT p.id, p.libro_id, l.Titulo
            FROM prestar AS p
            INNER JOIN libros AS l ON p.libro_id = l.ID
            WHERE p.estatus="Prestado" OR p.estatus="Seleccione"
        ''')

        # Obtener todos los registros
        libros_prestados = cursor.fetchall()

        # Cerrar cursor y conexión
        cursor.close()
        conexion.close()
        #print(libros_prestados)
        return libros_prestados

    except sql.Error as error:
        print("Error al obtener libros prestados:", error)
        return []

def atc_estatus(id, nuevo_estatus):
    import sqlite3 as sql
    # Conectar a la base de datos
    conn = sql.connect('BibliotecaCUC/bibliotecaCelsus.db')
    cursor = conn.cursor()
    
    # Ejecutar la actualización en la tabla prestar
    cursor.execute('''
        UPDATE prestar
        SET estatus = ?
        WHERE libro_id = ? AND estatus = "Prestado"
    ''', (nuevo_estatus, id))
    
    # Confirmar los cambios
    conn.commit()
    
    # Cerrar la conexión
    conn.close()
    
    return "Devolucion exitosa"
    
    
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


def eliminarle(ID):
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")
    cursor = conexion.cursor()
    #print(ID)
    # Ejecutar la consulta de eliminación
    cursor.execute('''
        DELETE FROM libros
        WHERE ID = ?
    ''', (ID,))  # Corregido para pasar ID como una tupla

    # Confirmar los cambios
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    return "Libro eliminado"

def prestamos(solicitante, carrera, fecha_inicio, fecha_fin, libro_id, estatus):
    import sqlite3 as sql
    # Conectar a la base de datos
    conexion = sql.connect("BibliotecaCUC/bibliotecaCelsus.db")

    # Crear un cursor
    cursor = conexion.cursor()
    
    #Manejo estatus
    if estatus=="Seleccione":
        estatus="Prestado"
    # Sentencia SQL para insertar datos en la tabla 'prestar'
    cursor.execute('''
    INSERT INTO prestar (
        solicitante, carrera, fecha_inicio, fecha_fin, libro_id, estatus
    ) VALUES (?, ?, ?, ?, ?, ?)
    ''', (solicitante, carrera, fecha_inicio, fecha_fin, libro_id, estatus))
    # Confirmar los cambios
    conexion.commit()

    # Cerrar el cursor y la conexión
    cursor.close()
    conexion.close()

    return "Prestamo concretado"

def obtener_datos_prestamos():
    import sqlite3 as sql
    
    conn = sql.connect('BibliotecaCUC/bibliotecaCelsus.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT libro_id, COUNT(*) FROM prestar GROUP BY libro_id')
    prestamos = cursor.fetchall()
    
    cursor.execute('SELECT ID, Titulo FROM libros')
    libros = cursor.fetchall()
    print(prestamos)
    conn.close()
    return prestamos, libros