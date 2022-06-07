from pydoc import doc
from flask import Flask, render_template, request, redirect, make_response
import random
import hashlib
import time
import controlador_db
import ecdsa
import smtplib
from email.message import EmailMessage
import re
import DHAES
'''implementar el toast con bootstrap y js'''

'''conex=mysql.connector.connect(host="localhost", user="root", passwd="")'''



app = Flask(__name__)
app.config['SECRET_KEY'] = '123123123'

'''Variables globales'''

global correoOTP
global mensajesEncriptadosParaAlice
global mensajesEncriptadosParaBob
global hayClaves
global cambiaK
global arraysLlenos
global numAleat


numAleat=0
arraysLlenos = False
cambiaK = False
hayClaves = False


'''Funciones sin ruta'''
def es_correo_valido(correo):
    expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
    return re.match(expresion_regular, correo) is not None

''' Solo devuelve true cuando el hash se encuentra en la base de datos, con lo cual, si meten un hash
    que no se encuentra en la base de datos devolvera false, unicamente podran hacer cookie injection cuando 
    adivinen el hash de una contraseña de un usuario'''

def compruebaCookie():
    '''if(email is None): return False'''
    prueba = request.cookies.get('cookie_key')
    email = request.cookies.get('email_user')
    #email = controlador_db.obtieneMail(prueba)
    if(controlador_db.hashEmailUsuarioYConfirmado(prueba,email)): return True
    else: return False

def enviar_correo(email):
    
    nickname = email.split(sep='@')
    confirmation = 'si'
    controlador_db.update_usuario(email,confirmation)
    message = EmailMessage()
    email_subject = "Registro realizado con éxito"
    sender_email = "eccmati2022@hotmail.com"
    email_pass = "SMcJ#Bj4OPgl"
    receiver_em = email

    message['Subject'] = email_subject
    message['From'] = sender_email
    message['To'] = receiver_em

    message.set_content("La cuenta ha sido creada satisfactoriamente. Esperamos desde ECC que disfrutes de la página!\nSu nuevo nickname es: "+nickname[0])

    email_smtp = "smtp.outlook.com"
    server = smtplib.SMTP(email_smtp, '587')
    server.ehlo()
    server.starttls()
        
    server.login(sender_email, email_pass)
    server.send_message(message)
        
    server.close()

def enviar_correoOTP(nombre,apellido,apellido2,passwd,email):
    apellidos = apellido + ' ' + apellido2
    nickname = email.split(sep='@')
    confirmation = 'no'
    controlador_db.insertar_usuarioNoDef(nombre,apellidos,email,nickname[0],passwd,confirmation)
    message = EmailMessage()
    email_subject = "Es necesario que verifique su identidad"
    sender_email = "eccmati2022@hotmail.com"
    email_pass = "SMcJ#Bj4OPgl"
    receiver_em = email

    message['Subject'] = email_subject
    message['From'] = sender_email
    message['To'] = receiver_em

    message.set_content("Antes de proceder con el registro, debemos comprobar su identidad, para ello, introduzca el siguiente numero: "+str(numOTP)+"\nGracias por registrarse en ECCParaTodos!")

    email_smtp = "smtp.outlook.com"
    server = smtplib.SMTP(email_smtp, '587')
    server.ehlo()
    server.starttls()
        
    server.login(sender_email, email_pass)
    server.send_message(message)
        
    server.close()

def leeEInicializa():
    global arrayPreguntas
    global arrayRespuestas
    arrayPreguntas=[]
    arrayRespuestas=[]

    with open('static/preguntasEASY.txt', 'r') as f:
                contenido = f.read()
                todo = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
                for i in range (len(todo)):
                    arrayPreguntas.append(todo[i])
    with open('static/respuestasEASY.txt', 'r') as f:
            contenido = f.read()
            todo = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
            for i in range (len(todo)):        
                arrayRespuestas.append(todo[i])
    print('Vectores inicializados correctamente')

'''Funciones con app route '''

@app.errorhandler(404)
def access_error(error):
    return render_template('error_404.html'), 404

@app.route('/')
def home():
    if(compruebaCookie()):
        return redirect('/logged/home')
    else:
        return render_template('home.html')

@app.route('/teoria')
def aboutSinLog():
    return render_template('teoria.html')

@app.route('/login', methods=["GET","POST"])
def login():
    if(compruebaCookie()):
        return redirect('/logged/home')
    email = request.form.get('inputemail')
    passwdPT = request.form.get('inputpwd')
    
    if(email==None or passwdPT==None):
        return render_template('login.html')
    else:
        bytes=passwdPT.encode()
        hash=hashlib.sha256(bytes)
        existe=controlador_db.hashEmailUsuarioYConfirmado(hash.hexdigest(),email)
        if(existe):
            '''hacerle un redirect a la pagina de inicio, meterle la cookie de sesion etc
            '''
            print ('Existe el hash')
            
            res = make_response(redirect('/logged/home'))
            res.set_cookie('cookie_key', hash.hexdigest(), max_age=None)
            res.set_cookie('email_user', email, max_age=None)
            return res
        else:
            '''Podria llevar una cuenta del num de intentos erroneos y a la 3 o asi envio correo.'''
            print('No existe el hash')
            
            return render_template('loginNoSuccess.html')


@app.route('/validadorFirmas', methods=["GET", "POST"])
def validaFirmas():
    if(compruebaCookie()):
        mens=str(request.form.get('inputMsg'))
        publ=str(request.form.get('inputKu'))
        sign=str(request.form.get('inputSign'))
        if(mens == None or mens == ''): return render_template('validadorFirmas.html',resultadoFirma='Mensaje no seteado')
        if(publ == None or publ == ''): return render_template('validadorFirmas.html',resultadoFirma='Clave pública no seteada')
        if(sign == None or sign == ''): return render_template('validadorFirmas.html',resultadoFirma='Firma no seteada')
        result=ecdsa.verify_signaturePerso(publ,mens,sign)
        #print(result)
        return render_template('validadorFirmas.html', resultadoFirma=result)
    else: return redirect ('/login')
    

@app.route('/logged/home' , methods=["POST","GET"])
def logged():
    if(compruebaCookie()):
        hash=request.cookies.get('cookie_key')
        email = request.cookies.get('email_user')

        nick=controlador_db.obtieneNickname(hash,email)
        return render_template('homeLogueado.html',nickname=nick)
    else:
        return redirect('/login')

@app.route('/logged/teoria')
def about():
    if(compruebaCookie()):
        return render_template('teoria.html')
    else:
        return redirect('/login')

#Aqui va el procedimiento donde los usuarios van a poder firmar y comprobar firmas de textos.
@app.route('/generadorFirmas', methods=["GET", "POST"])
def juegaFirmas():
    global kprivada,kpublica

    global mensaje

    global firma

    kprivada=''
    kpublica=''
    mensaje=''
    firma=''
    if(compruebaCookie()):
            mensaje = str(request.form.get('inputMsg'))
            if(kprivada=='' and kpublica==''):
                kprivada,kpublica=ecdsa.make_keypair()
                publica = "(0x{:x}, 0x{:x})".format(*kpublica)
                privada = hex(kprivada)
            
            if(mensaje == '' or mensaje == None or mensaje == 'None'): return render_template('juegaFirmas.html',mensajeSigned='', huellaMensaje='', priv=privada, pub=publica, sign='')
            else:
                
                
                huella = '0x'+hashlib.sha256(mensaje.encode()).hexdigest()
                mensaje.encode()
                firma = ecdsa.sign_message(kprivada,mensaje)
                
                return render_template('juegaFirmas.html', priv=kprivada, pub=kpublica, sign=firma, mensajeSigned=mensaje,huellaMensaje=huella)
    else:
            return redirect('/login')

@app.route('/cifrador',methods=["POST","GET"])
def cifrador():
    
    global krAlice,kuAlice
    global krBob,kuBob
    global secretoAlice,secretoBob

    global hayClaves
    global mensajesEncriptadosParaAlice
    global mensajesEncriptadosParaBob
    global descAlice,descBob

    if(compruebaCookie()):
        if(hayClaves==False):
            hayClaves=True
            mensajesEncriptadosParaAlice=[]
            mensajesEncriptadosParaBob=[]
            krAlice,kuAlice = ecdsa.make_keypair()
            krBob,kuBob = ecdsa.make_keypair()
            secretoAlice = DHAES.ECDH_secretTrunc(krAlice,kuBob)
            secretoBob = DHAES.ECDH_secretTrunc(krBob,kuAlice)
        
        cambiaK=request.form.get('cambiaClaves')
        encMsgAlice = request.form.get('inputAliceMsg')
        encMsgBob = request.form.get('inputBobMsg')
        descAlice=request.form.get('traduceDAli')
        descBob = request.form.get('traduceDBob')
        '''print(krAlice,kuAlice)
        print(krBob,kuBob)'''
        
        desencriptado=''

        if(cambiaK != None):
            mensajesEncriptadosParaAlice=[]
            mensajesEncriptadosParaBob=[]
            krAlice,kuAlice = ecdsa.make_keypair()
            krBob,kuBob = ecdsa.make_keypair()
            secretoAlice = DHAES.ECDH_secretTrunc(krAlice,kuBob)
            secretoBob = DHAES.ECDH_secretTrunc(krBob,kuAlice)
        if(descAlice != None):
            if(len(mensajesEncriptadosParaBob)==0): return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
            
            desencriptado = DHAES.desencriptarAES_EAX(secretoBob.encode(),mensajesEncriptadosParaBob[0])
            mensajesEncriptadosParaBob.pop(0)
            
            return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice=str(desencriptado).replace("b'","").replace("'",""), kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
        
        if(descBob != None):
            if(len(mensajesEncriptadosParaAlice)==0): return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
            desencriptado = DHAES.desencriptarAES_EAX(secretoAlice.encode(),mensajesEncriptadosParaAlice[0])
            mensajesEncriptadosParaAlice.pop(0)
            return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob=str(desencriptado).replace("b'","").replace("'",""), mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
        
        #Si no hay nada puesto
        if( (encMsgAlice == None or encMsgAlice == '') and (encMsgBob == None or encMsgBob=='') ):
            return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
        
        #Si hay algun mensaje de Alice para Bob, lo añado al array y devuelvo el tam
        if(encMsgAlice != None and encMsgAlice != '' and encMsgAlice!='None'):
            
            msgEncriptedAlice = DHAES.encriptarAES_EAX(secretoAlice.encode(),encMsgAlice)
            mensajesEncriptadosParaBob.append(msgEncriptedAlice)
            return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
        
        #Si hay algun mensaje de Bob para Alice, lo añado al array y devuelvo el tam
        if(encMsgBob != None and encMsgBob != '' and encMsgBob!='None'):
            
            msgEncriptedBob = DHAES.encriptarAES_EAX(secretoBob.encode(),encMsgBob)
            mensajesEncriptadosParaAlice.append(msgEncriptedBob)
            return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
        
        return render_template('encriptt.html', nMsgPendientesAlice=len(mensajesEncriptadosParaAlice), nMsgPendientesBob=len(mensajesEncriptadosParaBob), mensajitoDeBob='No hay mensajes', mensajitoDeAlice='No hay mensajes', kuAlice=kuAlice, kuBob=kuBob, aliceSecret=secretoAlice, bobSecret=secretoBob)
    else: return redirect('/login')

@app.route('/easy', methods=["POST","GET"])
def generaCuestionarioEasy():
    global arrayPreguntas
    global arrayRespuestas
    global pregRandom
    global respRandom
    global arraysLlenos
    global numAleat
    global pregs
    global resp
    
    if(compruebaCookie()):
        answ1 = request.form.get('answ1')
        answ2 = request.form.get('answ2')
        answ3 = request.form.get('answ3')
       
        if(arraysLlenos==False):
            pregs = []
            resp = []
            pregRandom = []
            respRandom = []
            arraysLlenos=True
            ant = 0
            for i in range(3):
                #random.seed(time.time())
                numAleat = random.randint(0, 9)
                while numAleat == ant:
                    numAleat = random.randint(0, 9)
                pregRandom.append(arrayPreguntas[numAleat])
                respRandom.append(arrayRespuestas[numAleat])
                ant=numAleat
            for i in range(len(pregRandom)):
                split=str(pregRandom[i]).split(sep=";")
                pregs.append(split[0])
                resp.append(split[1])
                resp.append(split[2])
                resp.append(split[3])
            return render_template('cuestEasy.html',preguntaE1=pregs[0], preguntaE2=pregs[1], preguntaE3=pregs[2], resp11=resp[0],resp12=resp[1], resp13=resp[2],
            resp21=resp[3], resp22=resp[4], resp23=resp[5],resp31=resp[6],resp32=resp[7], resp33=resp[8])

        if((answ1 == None or answ1 == ' ') or (answ2 == None or answ2 == ' ') or (answ3 == None or answ3 == ' ')):
            
            return render_template('cuestEasy.html',preguntaE1=pregs[0], preguntaE2=pregs[1], preguntaE3=pregs[2], resp11=resp[0],resp12=resp[1], resp13=resp[2],
            resp21=resp[3], resp22=resp[4], resp23=resp[5],resp31=resp[6],resp32=resp[7], resp33=resp[8])
        else:
            puntuacion = 0
            primera = 'Errónea'
            segunda = 'Errónea'
            tercera='Errónea'
            
            if(str(answ1).lower() == respRandom[0]):
                puntuacion +=50
                primera = 'Acierto'
            if(str(answ2).lower() == respRandom[1]):
                puntuacion +=50
                segunda = 'Acierto'
            if(str(answ3).lower() == respRandom[2]):
                puntuacion +=50
                tercera='Acierto'
            pregRandom = []
            respRandom = []
            arraysLlenos=False
            
            return render_template('resultadosCuestionario.html', puntaje=puntuacion,resPreg1=primera, resPreg2=segunda, resPreg3=tercera, preguntaE1=pregs[0], preguntaE2=pregs[1], preguntaE3=pregs[2], resp11=resp[0],resp12=resp[1], resp13=resp[2],
        resp21=resp[3], resp22=resp[4], resp23=resp[5],resp31=resp[6],resp32=resp[7], resp33=resp[8], letra1=str(answ1).lower(),letra2=str(answ2).lower(),letra3=str(answ3).lower())
    else:
        return redirect('/login')

@app.route('/logged/encdec', methods=["POST","GET"])
def encdec():
    if(compruebaCookie()):
        return render_template('encdec.html')
    else: return redirect('/login')


@app.route('/perfil', methods=["POST","GET"])
def perfil():
    if(compruebaCookie()):
        hash=request.cookies.get('cookie_key')
        email=request.cookies.get('email_user')
        nick=controlador_db.obtieneNickname(hash,email)
        puntosAnt = controlador_db.obtienePuntos(hash,email)
        puntos = request.form.get('puntuacion')
        if(puntos!=None):
            total = int(puntos) + int(puntosAnt)
            controlador_db.actualizaPuntos(hash,email,total)
            return render_template('perfil.html',name=nick, puntosAntCuestionario=puntos, puntosTotales=total)
        return render_template('perfil.html',name=nick, puntosAntCuestionario=0,puntosTotales=puntosAnt)
    else:
        return redirect('/login')
@app.route('/logout')
def logout():
    res = make_response(redirect('/'))
    res.delete_cookie('cookie_key')
    res.delete_cookie('email_user')
    return res

@app.route('/register' , methods=["POST","GET"])
def register():
    
    nombre=request.form.get('inputName')
    apellido = request.form.get('inputSurname')
    apellido2 = request.form.get('inputSurname2')
    email = request.form.get('inputEmail')
    
    passwd = request.form.get('inputPwd')
    if(compruebaCookie()):
            hash=request.cookies.get('cookie_key')
            nickn = controlador_db.obtieneNickname(hash,email)
            
            return redirect('/perfil',name=nickn,puntosAntCuestionario=0)
    else:
        if(email is not None):
            isValid = es_correo_valido(email)
        if(nombre==None or apellido==None or apellido2==None or email==None or passwd==None or isValid==False):
            return render_template('register.html')
        else:
            '''Generar numero random para el otp'''
            global correoOTP
            global numOTP
            
            numOTP = random.randint(100000,999999)
            correoOTP=email
            enviar_correoOTP(nombre,apellido,apellido2,passwd,email)
            return redirect('/introOTP')
            
@app.route('/introOTP',methods=["POST","GET"])
def introduceOTP():
    otp=request.form.get('inputOTP')
    if(otp==None):
        return render_template('introOTP.html')
    else:
        if(otp == str(numOTP)):
            enviar_correo(correoOTP)
            return redirect('/')
        else:
            return redirect('/register')

@app.route('/resendOTP', methods=["GET","POST"])
def resend():
    data=controlador_db.obtieneTodaLaFila(correoOTP)
    apellidos = data[0][2].split(sep=' ')
    ape1=apellidos[0]
    ape2=apellidos[1]
    numOTP=random.randint(100000,999999)
    '''reenviar otro codigo'''
    
    enviar_correoOTP(data[0][1],ape1,ape2,data[0][5],correoOTP)
    return redirect('/introOTP')

@app.route('/tutorialFirma', methods=["POST","GET"])
def tutorialFirma():
    return render_template('tutoECDSA.html')

'''---------------------------------------------------------------------------'''
'''Aqui estan las rutas para el graficador en caso de que no estemos logueados'''
'''---------------------------------------------------------------------------'''
@app.route('/graficador/adicionReales')
def sumaReales():
    return render_template('reals-add.html')

@app.route('/graficador/multiReales')
def multiReales():
    return render_template('reals-mul.html')

@app.route('/graficador/adicionDiscr')
def adicionDiscr():
    return render_template('modk-add.html')

@app.route('/graficador/multiDiscr')
def multiDiscr():
    return render_template('modk-mul.html')

'''------------------------------------------------------------------------'''
'''Aqui estan las rutas para el graficador en caso de que estemos logueados'''
'''------------------------------------------------------------------------'''
@app.route('/logged/graficador/adicionReales')
def sumaRealesLog():
    if(compruebaCookie()):
        return render_template('reals-addLog.html')
    else:
        return redirect('/graficador/adicionReales')
  
@app.route('/logged/graficador/multiReales')
def multiRealesLog():
    if(compruebaCookie()):
        return render_template('reals-mulLog.html')
    else:
        return redirect('/graficador/multiReales')

@app.route('/logged/graficador/adicionDiscr')
def adicionDiscrLog():
    if(compruebaCookie()):
        return render_template('modk-addLog.html')
    else:
        return redirect('/graficador/adicionDiscr')

@app.route('/logged/graficador/multiDiscr')
def multiDiscrLog():
    if(compruebaCookie()):
        return render_template('modk-mulLog.html')
    else:
        return redirect('/graficador/multiDiscr')


if __name__ == '__main__':
    leeEInicializa()
    app.run(host="192.168.1.65", port=5000, debug=True)
    