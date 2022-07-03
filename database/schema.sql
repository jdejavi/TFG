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

CREATE TABLE atributosLogueado(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150),
    arraysLlenos VARCHAR(150),
    arraysLlenosMed VARCHAR(150),
    cambiaK VARCHAR(150)
);

CREATE TABLE variables(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150),
    nuevaContraseña VARCHAR(150),
    numOTP INT(4),
    numerosCuestionario VARCHAR(150)
);

CREATE TABLE atrCifrado(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150),
    krAlice VARCHAR(150),
    krBob VARCHAR(150),
    kuAlice VARCHAR(500),
    kuBob VARCHAR(500),
    mensajesDeAlice VARCHAR(500),
    mensajesDeBob VARCHAR(500),
    mensajeClaroAlice VARCHAR(150),
    mensajeClaroBob VARCHAR(150),
    hayClaves VARCHAR(150),
    secretoDeAlice VARCHAR(250),
    secretoDeBob VARCHAR(250)
);
