import pymysql

''' Para conectarme a la base de datos directamente desde mysql
mysql -h b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com -P 3306 -u ucprxfshxavxruqm -p b6sembtlcyhj27os1pwp
'''

'''Conexion con la base de datos proporcionada por serviceCloud, con las credenciales seteadas ya'''
def obtiene_conex():
    return pymysql.connect(host='b6sembtlcyhj27os1pwp-mysql.services.clever-cloud.com',
                           user='ucprxfshxavxruqm',
                           password='zNSwEFVIYhtaOcQyA03O',
                           db='b6sembtlcyhj27os1pwp')
