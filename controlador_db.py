from email.mime import base
from sqlite3 import connect
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
