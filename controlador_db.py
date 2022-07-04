import pymysql
import hashlib




'''Aqui iran implementadas todas las funciones que toquen la base de datos'''
'''
mysql -h b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com -P 3306 -u ucprxfshxavxruqm -p b6sembtlcyhj27os1pwp
    passwd --> zNSwEFVIYhtaOcQyA03O'''

user='ucprxfshxavxruqm'
passwd='zNSwEFVIYhtaOcQyA03O'
bd='b6sembtlcyhj27os1pwp'
hostUrl='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com'

def insertar_usuarioNoDef(nombre,apellidos,mail,nickname,passwd,conf):

   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
       print('DB conectada user no def')
       '''Aqui hago una comprobacion de que el correo no existe ya, si no existe lo añado pero si no existe no'''
       buscarCorreo = "SELECT * FROM usuarios WHERE mail=%s"
       existe=cursor.execute(buscarCorreo,(mail,))
       if(existe): return False
       else:
            bytes = passwd.encode()
            hashPwd = hashlib.sha256(bytes)
            insercion = "INSERT INTO usuarios (nombre,apellidos,mail,nickname,passwd,puntuacion,confirmed) VALUES (%s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,(nombre,apellidos, mail, nickname, hashPwd.hexdigest(),0,conf))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa user no def')
            return True
   else: 
            print('No se conecto a la Db')
            return False

def obtienenumOTPVariables(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
        busqueda = "SELECT numOTP from variables WHERE email=%s;"
        cursor.execute(busqueda,(email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila[0][0]
        else:
            connection.close()
            return ''

def borraRegistroVariables(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
        query = "DELETE FROM variables WHERE email=%s;"
        cursor.execute(query,(email,))
        connection.commit()
        busqueda = "SELECT * FROM variables where email=%s"
        fila = cursor.execute(busqueda,(email,))
        if(fila==0):
           connection.close()
           return True
        else:
           connection.close()
           return False

def insertaVariables(email,nuevaPass,numOTP,numCuestionario):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

    cursor=connection.cursor()

    if(cursor):
        insercion = "INSERT INTO variables (email,nuevaContraseña,numOTP,numerosCuestionario) VALUES (%s, %s, %s, %s);"
        cursor.execute(insercion,(email,nuevaPass,numOTP,numCuestionario))
        connection.commit()
        connection.close()

        print("Inserción tabla variable exitosa")
        return True
    else:
        print("No se conecto a la DB")
        return False

def update_usuario(mail,conf):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
   cursor=connection.cursor()
   if(cursor):
       print('DB conectada user def')
       update = "UPDATE usuarios SET confirmed=%s WHERE mail=%s;"
       cursor.execute(update,(conf,mail))
       connection.commit()
       connection.close()
       
       print('Update exitosa user def')
       return True
   else: 
       print('No se conecto a la Db')
       return False

def update_passwd(mail,passwd):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
   cursor=connection.cursor()
   if(cursor):
       print('DB conectada user def')
       update = "UPDATE usuarios SET passwd=%s WHERE mail=%s;"
       cursor.execute(update,(passwd,mail))
       connection.commit()
       connection.close()
       
       print('Update exitosa de la contraseña de un usuario')
       return True
   else: 
       print('No se conecto a la Db')
       return False


def hashUsuario(hash):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
   cursor=connection.cursor()
   if(cursor):
       print('DB Connected')
       busqueda = "SELECT * FROM usuarios WHERE passwd=%s"
       fila=cursor.execute(busqueda,(hash,))
       if(fila==1):
           connection.close()
           return True
       else:
           connection.close()
           return False
           
def obtieneMail(hash):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB Connected')
        busqueda = "SELECT mail FROM usuarios WHERE passwd=%s"
        cursor.execute(busqueda,(hash,))
        fila=cursor.fetchall()
        
        if(fila):
            connection.close()
            return fila[0][0]
        else:
            connection.close()
            return ''

def hashEmailUsuarioYConfirmado(hash,email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
   cursor=connection.cursor()
   if(cursor):
       print('DB Connected')
       busqueda = "SELECT * FROM usuarios WHERE passwd=%s AND mail=%s AND confirmed='si'"
       fila=cursor.execute(busqueda,(hash,email,))
       if(fila==1):
           connection.close()
           return True
       else:
           connection.close()
           return False

def obtieneTodaLaFila(email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB Connected')
        busqueda = "SELECT * FROM usuarios WHERE mail=%s"
        cursor.execute(busqueda,(email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila
        else:
            connection.close()
            return ''
   

def obtieneNickname(hash,email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB Connected')
        busqueda = "SELECT nickname FROM usuarios WHERE passwd=%s AND mail=%s"
        cursor.execute(busqueda,(hash,email,))
        fila=cursor.fetchall()
        
        if(fila):
            connection.close()
            return fila[0][0]
        else:
            connection.close()
            return ''

def obtienePuntos(hash,email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB Connected')
        busqueda = "SELECT puntuacion FROM usuarios WHERE passwd=%s AND mail=%s"
        cursor.execute(busqueda,(hash,email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila[0][0]
        else:
            connection.close()
            return ''
def actualizaPuntos(hash,email,puntos):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB conectada user def')
        update = "UPDATE usuarios set puntuacion=%s WHERE mail=%s AND passwd=%s"
        cursor.execute(update,(puntos,email,hash,))
        connection.commit()
        connection.close()
        print('Update exitosa user def')
        return True
    else: 
        print('No se conecto a la Db')
        return False

def insertaAtributosLogued(email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        print('DB connectada')
        insercion = "INSERT INTO atributosLogueado (email,arraysLlenos,arraysLlenosMed,cambiaK) VALUES (%s, %s, %s, %s);"
        cursor.execute(insercion,(email,None,None,None))
        connection.commit()
        connection.close()

        print("Inserción tabla atributosLogued exitosa")
        return True
    else:
        print("No se conecto a la DB")
        return False

def obtieneFilaAtrCifrador(email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        busqueda = "SELECT * from atrCifrado WHERE email=%s"
        cursor.execute(busqueda,(email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila
        else:
            connection.close()
            return ''

def insertaAtrCifrado(email,krAlice,kuAlice,krBob,kuBob,hayK,secretoAlice,secretoBob):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
            
            insercion = "INSERT INTO atrCifrado (email,krAlice,krBob,kuAlice,kuBob,mensajesDeAlice,mensajesDeBob,mensajeClaroAlice,mensajeClaroBob,hayClaves,secretoDeAlice,secretoDeBob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,(email,krAlice,krBob,kuAlice,kuBob,None,None,None,None,hayK,secretoAlice,secretoBob))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa user no def')
            return True
   else: 
            print('No se conecto a la Db')
            return False

def borraFilaAtrCifrado(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
        query = "DELETE FROM atrCifrado WHERE email=%s;"
        cursor.execute(query,(email,))
        connection.commit()
        busqueda = "SELECT * FROM atrCifrado where email=%s"
        fila = cursor.execute(busqueda,(email,))
        if(fila==0):
           connection.close()
           return True
        else:
           connection.close()
           return False

def updatePilaDeBob(email,mensajesDBob,msgClaroAlice):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado SET mensajesDeBob=%s, mensajeClaroAlice=%s WHERE email=%s"
    cursor.execute(query,(mensajesDBob,msgClaroAlice,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de pila mensajesDeBob')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updatePilaDeAlice(email,mensajesDAlice,msgClaroBob):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado SET mensajesDeAlice=%s, mensajeClaroBob=%s WHERE email=%s"
    cursor.execute(query,(mensajesDAlice,msgClaroBob,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de pila mensajesDeBob')
    return True
   else: 
    print('No se conecto a la Db')
    return False
#########################################3
def insertaMsgEncripted(email,msgEncAlice, msgEncBob):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado set mensajesDeBob=%s, mensajesDeAlice=%s WHERE email=%s"
    cursor.execute(query,(msgEncAlice,msgEncBob,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de mensaje encriptado')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updateAtrCifrado(email,krAlice,kuAlice,krBob,kuBob,hayK,secretoAlice,secretoBob):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado set krAlice=%s, kuAlice=%s, krBob=%s, kuBob=%s, hayClaves=%s, secretoDeAlice=%s, secretoDeBob=%s WHERE email=%s"
    cursor.execute(query,(krAlice,kuAlice,krBob,kuBob,hayK,secretoAlice,secretoBob,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de atributos cifrado')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updateMensAlice(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado set mensajesDeAlice=%s, mensajeClaroBob=%s WHERE email=%s"
    cursor.execute(query,(None,None,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de atributos cifrado')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updateMensBob(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atrCifrado set mensajesDeBob=%s, mensajeClaroAlice=%s WHERE email=%s"
    cursor.execute(query,(None,None,email,))
    connection.commit() 
    connection.close()
       
    print('Update exitosa de atributos cifrado')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def insertarTablaPreg(email):
    
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
            
            insercion = "INSERT INTO preguntas (email,pregA,respA,pregB,respB,pregC,respC,pregAMed,respAMed,pregBMed,respBMed,pregCMed,respCMed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,(email,None,None,None,None,None,None,None,None,None,None,None,None))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa user no def')
            return True
   else: 
            print('No se conecto a la Db')
            return False

def actualizanumOTPVariables(email,numOTP):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE variables set numOTP=%s WHERE email=%s"
    cursor.execute(query,(numOTP,email,))
    connection.commit() 
    connection.close()
       
    print('Update exitosa de variables')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updateTablaPreguntasCE(email,pregA,respA,pregB,respB,pregC,respC):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE preguntas set pregA=%s,respA=%s,pregB=%s,respB=%s,pregC=%s,respC=%s WHERE email=%s"
    cursor.execute(query,(pregA,respA,pregB,respB,pregC,respC,email,))
    connection.commit() 
    connection.close()
       
    print('Update exitosa de preguntas')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def updateTablaPreguntasCM(email,pregMedA,respMedA,pregMedB,respMedB,pregMedC,respMedC):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE preguntas set pregAMed=%s,respAMed=%s,pregBMed=%s,respBMed=%s,pregCMed=%s,respCMed=%s WHERE email=%s"
    cursor.execute(query,(pregMedA,respMedA,pregMedB,respMedB,pregMedC,respMedC,email,))
    connection.commit() 
    connection.close()
       
    print('Update exitosa de preguntas')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def actualizaArrLlenos(email,arraysLlenos):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atributosLogueado set arraysLlenos=%s WHERE email=%s"
    cursor.execute(query,(arraysLlenos,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de preguntas')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def actualizaArrLlenosMed(email,arraysLlenosMed):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
    query = "UPDATE atributosLogueado set arraysLlenosMed=%s WHERE email=%s"
    cursor.execute(query,(arraysLlenosMed,email,))
    connection.commit()
    connection.close()
       
    print('Update exitosa de preguntas')
    return True
   else: 
    print('No se conecto a la Db')
    return False

def obtieneFilaAtrLogued(email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        busqueda = "SELECT * from atributosLogueado WHERE email=%s"
        cursor.execute(busqueda,(email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila
        else:
            connection.close()
            return ''

def obtieneFilaPreguntas(email):
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        busqueda = "SELECT * from preguntas WHERE email=%s"
        cursor.execute(busqueda,(email,))
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila
        else:
            connection.close()
            return ''

def insertaDataPregTemp(email,respApreg1,respBpreg1,respCpreg1,respApreg2,respBpreg2,respCpreg2,respApreg3,respBpreg3,respCpreg3):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
            
            insercion = "INSERT INTO dataPreguntasTemp (email,respApreg1,respBpreg1,respCpreg1,respApreg2,respBpreg2,respCpreg2,respApreg3,respBpreg3,respCpreg3) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,(email,respApreg1,respBpreg1,respCpreg1,respApreg2,respBpreg2,respCpreg2,respApreg3,respBpreg3,respCpreg3,))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa dataPregTemp')
            return True
   else: 
            print('No se conecto a la Db')
            return False

def obtieneRespuestas(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
   cursor=connection.cursor()
   if(cursor):
       print('DB Connected')
       busqueda = "SELECT * FROM dataPreguntasTemp WHERE email=%s"
       fila=cursor.execute(busqueda,(email,))
       fila=cursor.fetchall()
       if(fila):
            connection.close()
            return fila
       else:
            connection.close()
            return ''

def borraFilaPregTemp(email):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
        query = "DELETE FROM dataPreguntasTemp WHERE email=%s;"
        cursor.execute(query,(email,))
        update = "UPDATE preguntas set pregA=%s,respA=%s,pregB=%s,respB=%s,pregC=%s,respC=%s WHERE email=%s"
        cursor.execute(update,(None,None,None,None,None,None,email))
        update2 = "UPDATE preguntas set pregAMed=%s,respAMed=%s,pregBMed=%s,respBMed=%s,pregCMed=%s,respCMed=%s WHERE email=%s"
        cursor.execute(update2,(None,None,None,None,None,None,email))
        connection.commit()
        busqueda = "SELECT * FROM dataPreguntasTemp where email=%s"
        fila = cursor.execute(busqueda,(email,))
        if(fila==0):
           connection.close()
           return True
        else:
           connection.close()
           return False

def insertaPreguntas(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10):
   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
            
            insercion = "INSERT INTO preguntasyResp (pregunta1, pregunta2, pregunta3, pregunta4, pregunta5, pregunta6, pregunta7, pregunta8, pregunta9, pregunta10, correcta1, correcta2, correcta3, correcta4, correcta5, correcta6, correcta7, correcta8, correcta9, correcta10) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,(p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,c1,c2,c3,c4,c5,c6,c7,c8,c9,c10,))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa preguntasyRespuestas')
            return True
   else: 
            print('No se conecto a la Db')
            return False

def obtieneFilaPregResp():
    connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
    cursor=connection.cursor()
    if(cursor):
        busqueda = "SELECT * from preguntasyResp"
        cursor.execute(busqueda,())
        fila=cursor.fetchall()
        if(fila):
            connection.close()
            return fila
        else:
            connection.close()
            return ''