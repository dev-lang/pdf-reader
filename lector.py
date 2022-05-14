# PDF Reader
# by dev-lang (Frank Hathlev)
# en proceso de desarrollo
# versión 0.2.2 alpha

import PyPDF2 as LectorDePDF
import os

''' primero declaramos un diccionario donde guardaremos de forma indexada las palabras '''
#OPCIONAL TEMPORALMENTE (NO SE USA DE MOMENTO)
diccionarioWords = dict()

''' una variable vacía para almacenar el índice '''

indexPalabra = str()

''' una variable donde irá el formato del archivo '''
nombreDeArchivo = ''

''' una variable counter a modo de flag para poder agregar un indice que usaremos para el archivo guardado '''

contadorDocumento = int()

''' luego abrimos el pdf '''
documento = 'lorem-ipsum'
formatoDocumento = 'pdf'

nombreDeArchivoInput = str(documento + "." + formatoDocumento)

def AbrirArchivo(nombreDeArchivoInput):
    with open(nombreDeArchivoInput,'rb') as pdf_document:
        leerpdf = LectorDePDF.PdfFileReader(nombreDeArchivoInput)
        numero_paginas = leerpdf.getNumPages()
        pagina = leerpdf.pages[0]
        contenido = pagina.extractText()
        #print(contenido)
   
''' ejecución función '''
''' solo se ejecutará la funcion si el archivo existe '''
if os.path.exists(nombreDeArchivoInput):
    AbrirArchivo(nombreDeArchivoInput)
print("No existe el archivo")

''' solo se continuará si se ha ejecutado la función '''
''' la función creará las variables necesarias para continuar '''
''' pasamos el texto a una variable con un split() '''
if 'contenido' in globals():
    texto_splitteado = contenido.split()
print("No se puede continuar sin un archivo de origen!")

#print(texto_splitteado)

''' probamos ver un índice '''
#print(texto_splitteado[1])

''' guardamos el índice dentro de la variable anteriormente creada '''

if 'texto_splitteado' in globals():
    indexPalabra = texto_splitteado[1]
print("No se puede continuar sin haber guardado un contenido")

''' función para guardar el archivo con otro nombre según índice extraido '''

def GuardarArchivo(indiceExtraido):
    global nombreDeArchivo
    nombreDeArchivo = "{d}-{i}-{c}.{f}".format(d=documento, i=indiceExtraido, c=contadorDocumento, f=formatoDocumento)
    ''' guardar con nombreDeArchivo '''
    if os.path.exists(nombreDeArchivoInput):
        return "El archivo ya existe en el directorio. Se guardará con otro nombre"
        # función en desarrollo
    return "El archivo no existe? Copia algo :)"
    return nombreDeArchivo

print(GuardarArchivo(indexPalabra))