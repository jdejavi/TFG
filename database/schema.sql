/*Tabla usuarios en la base de datos*/
CREATE TABLE usuarios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(150) NOT NULL,
    apellidos VARCHAR(150) NOT NULL,
    mail VARCHAR(150) NOT NULL,
    nickname VARCHAR(150) NOT NULL,
    passwd VARCHAR(150) NOT NULL,
    puntuacion BIGINT NOT NULL,
    confirmed VARCHAR(10) NOT NULL
);