/* 

CREATE TABLE prestar(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    solicitante CHAR(30),
    carrera CHAR(30),
    fecha_inicio DATE,
    fecha_fin DATE,
    libro_id INT,
    estatus CHAR(8),
    FOREIGN KEY (libro_id) REFERENCES libros(ID)
); */
/* SELECT p.id, p.libro_id, l.Titulo
FROM prestar AS p
INNER JOIN libros AS l ON p.libro_id = l.ID; */
UPDATE prestar
        SET estatus = Devuelto
        WHERE id = 