# PDF Reader
# by dev-lang (Frank Hathlev)
# en proceso de desarrollo
# versión 0.1 alpha

import PyPDF2 as LectorDePDF

''' primero declaramos un diccionario donde guardaremos de forma indexada las palabras '''
diccionarioWords = dict()

''' luego abrimos el pdf '''
documento = 'lorem-ipsum.pdf'

with open(documento,'rb') as pdf_document:
    leerpdf = LectorDePDF.PdfFileReader(documento)
    numero_paginas = leerpdf.getNumPages()
    pagina = leerpdf.pages[0]
    contenido = pagina.extractText()
    #print(contenido)
   
''' pasamos el texto a una variable con un split() '''
texto_splitteado = contenido.split()

#print(texto_splitteado)

''' probamos ver un índice '''
print(texto_splitteado[1])
