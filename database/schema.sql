/*Tabla usuarios en la base de datos*/
CREATE TABLE usuarios(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellidos VARCHAR(50) NOT NULL,
    mail VARCHAR(50) NOT NULL,
    nickname VARCHAR(50) NOT NULL,
    passwd VARCHAR(150) NOT NULL,
    puntuacion BIGINT NOT NULL,
    confirmed VARCHAR(10) NOT NULL
);