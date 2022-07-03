import pymysql
import controlador_db
import ecdsa
import DHAES

def insert():

   connection=pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')

   cursor=connection.cursor()

   if(cursor):
            
            insercion = "INSERT INTO atrCifrado (email,krAlice,krBob,kuAlice,kuBob,mensajesDeAlice,mensajesDeBob,mensajeClaroAlice,mensajeClaroBob,hayClaves,secretoDeAlice,secretoDeBob) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
            cursor.execute(insercion,("jdejavi5@gmail.com",None,None,None,None,None,None,None,None,None,None,None))
            connection.commit()
            connection.close()
            
            print('Insercion exitosa user no def')
            return True
   else: 
            print('No se conecto a la Db')
            return False
insert()
mail = "jdejavi5@gmail.com"
fila = controlador_db.obtieneFilaAtrCifrador(mail)
print('Estructura de la query -> (id,email,krAlice,krBob,kuAlice,kuBob,mensajesParaAlice,mensajesParaBob,mensajeClaroAlice,mensajeClaroBob,hayClaves,secretoDeAlice,secretoDeBob)')
print("La fila [0] es -> "+str(fila[0]))

krAlice,kuAlice = ecdsa.make_keypair()
krBob,kuBob = ecdsa.make_keypair()
secretoAlice = DHAES.ECDH_secretTrunc(krAlice,kuBob)
secretoBob = DHAES.ECDH_secretTrunc(krBob,kuAlice)



mensajes=['Hola','que','tal']
temp = ''
final = ''
enc = DHAES.encriptarAES_EAX(secretoAlice.encode(),mensajes[0])
controlador_db.updatePilaDeBob(mail,str(enc),mensajes[0])
print(enc)

byteS = DHAES.encriptarAES_EAX(secretoBob.encode(),"Hola")

print(byteS)
#controlador_db.updatePilaDeBob(mail,str(enc),mensajes[0])
    
    #Descubrir como meter los valores aqui, tipo el encriptado para poder desencriptar
    #desencriptado = DHAES.desencriptarAES_EAX(secretoBob.encode(), mensaje)
    #print('El valor de desencriptado es : '+str(desencriptado))

#controlador_db.insertaMsgEncripted(mail,str(enc),None)



'''spliteada = final.split(sep=',')
cont = 0
for mens in spliteada:
    print(type(mens.replace('b\'','').replace('\'','')))
    desencriptado = DHAES.desencriptarAES_EAX(secretoBob.encode(), mens)
    print("El mensaje "+str(cont)+" es -> "+str(spliteada[cont])+" y su desencriptado es ->"+str(desencriptado))
    cont +=1

split = mensajes.split(sep="&")
print(len(split[:-1]))
print(len(split[1:-1]))
for msg in split:
    print(msg)'''