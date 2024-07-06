--CREATE TABLE libros(
--    ID int(4),
--    Titulo char(35),
--     Autor char(30),
--      Editorial char(20),
--       Num_Edicion int(3),
--        Año_publicacion int(4),
--        paginas int(5),
--        rama char(15),
--        ISBN int(13),
--         ubicacion text,
--          PRIMARY KEY (ID)) 
INSERT INTO libros(
    ID, Titulo, Autor, Editorial, Num_Edicion, Año_publicacion, paginas, rama, ISBN, ubicacion
) VALUES (
    8,--id
    "Mexico",--titulo
    "Teresa de Maria y Campos",--autor
    "Banamex",--editorial
    1,--edicion
    1990,--año publicacion
    178,--paginas
    "Historia",--Rama
    9687009217,--ISBN
    "Librero de cultura general, fila 3 columna 4"--Ubicacion
)
