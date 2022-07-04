import controlador_db

arrayPreguntas = []
arrayRespuestas = []

arrayPreguntasMed = []
arrayRespuestasMed = []

fila = controlador_db.obtieneFilaPregResp()

def devuelvePreguntas(ind):
    fila = controlador_db.obtieneFilaPregResp()
    if(str(ind) == 'Easy'):
        return fila [0]
    else: return fila [1]

preguntasE = devuelvePreguntas('Easy')
split = str(preguntasE[1]).split(sep=";")
for i in range(len(preguntasE)):
    print(preguntasE[i])
'''print(fila[0])
print(fila[1])'''
'''with open('static/preguntasEASY.txt', 'r', encoding='utf-8') as f:
                contenido = f.read()
                todo1 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
                for i in range (len(todo1)):
                    arrayPreguntas.append(todo1[i])
with open('static/respuestasEASY.txt', 'r', encoding='utf-8') as f:
            contenido = f.read()
            todo2 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
            for i in range (len(todo2)):
                arrayRespuestas.append(todo2[i])

controlador_db.insertaPreguntas(arrayPreguntas[0],arrayPreguntas[1],arrayPreguntas[2],arrayPreguntas[3],
                                arrayPreguntas[4],arrayPreguntas[5],arrayPreguntas[6],arrayPreguntas[7],
                                arrayPreguntas[8],arrayPreguntas[9],arrayRespuestas[0],arrayRespuestas[1],
                                arrayRespuestas[2],arrayRespuestas[3],arrayRespuestas[4],arrayRespuestas[5],
                                arrayRespuestas[6],arrayRespuestas[7],arrayRespuestas[8],arrayRespuestas[9])


with open('static/preguntasMED.txt', 'r', encoding='utf-8') as f:
                contenido = f.read()
                todo1 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
                for i in range (len(todo1)):
                    arrayPreguntasMed.append(todo1[i])
with open('static/respuestasMED.txt', 'r', encoding='utf-8') as f:
            contenido = f.read()
            todo2 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
            for i in range (len(todo2)):
                arrayRespuestasMed.append(todo2[i])


controlador_db.insertaPreguntas(arrayPreguntasMed[0],arrayPreguntasMed[1],arrayPreguntasMed[2],arrayPreguntasMed[3],
                                arrayPreguntasMed[4],arrayPreguntasMed[5],arrayPreguntasMed[6],arrayPreguntasMed[7],
                                arrayPreguntasMed[8],arrayPreguntasMed[9],arrayRespuestasMed[0],arrayRespuestasMed[1],
                                arrayRespuestasMed[2],arrayRespuestasMed[3],arrayRespuestasMed[4],arrayRespuestasMed[5],
                                arrayRespuestasMed[6],arrayRespuestasMed[7],arrayRespuestasMed[8],arrayRespuestasMed[9])'''

'''
with open('static/preguntasMED.txt', 'r', encoding='utf-8') as f:
                contenido = f.read()
                todo3 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
                for i in range (len(todo3)):
                    arrayPregMed.append(todo3[i])
with open('static/respuestasMED.txt', 'r', encoding='utf-8') as f:
            contenido = f.read()
            todo4 = str(contenido.replace("Â","").replace("Ã­","í").replace("Ã¡","á").replace("Ã³","ó").replace("Ãº","ú").replace("Ã©","é").replace("Ã±","ñ")).split(sep="\n")
            for i in range (len(todo4)):        
                arrayRespMed.append(todo4[i])
print('Vectores inicializados correctamente')
'''