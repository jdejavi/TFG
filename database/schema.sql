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

CREATE TABLE preguntas(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150),
    pregA VARCHAR(350),
    respA VARCHAR(350),
    pregB VARCHAR(350),
    respB VARCHAR(350),
    pregC VARCHAR(350),
    respC VARCHAR(350),
    pregAMed VARCHAR(350),
    respAMed VARCHAR(350),
    pregBMed VARCHAR(350),
    respBMed VARCHAR(350),
    pregCMed VARCHAR(350),
    respCMed VARCHAR(350)
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

CREATE TABLE dataPreguntasTemp(
    id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    email VARCHAR(150),
    respApreg1 VARCHAR(250),
    respBpreg1 VARCHAR(250),
    respCpreg1 VARCHAR(250),
    respApreg2 VARCHAR(250),
    respBpreg2 VARCHAR(250),
    respCpreg2 VARCHAR(250),
    respApreg3 VARCHAR(250),
    respBpreg3 VARCHAR(250),
    respCpreg3 VARCHAR(250)
);