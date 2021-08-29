import cv2 as cv
from PIL import Image
import os
from pytesseract import pytesseract as ocr


def extracaoTexto(origem, destino):
    nome = []
    for n in os.listdir(origem):
        nome.append(n)
      
    for i in nome:
        os.chdir(origem)
        texto = str(ocr.image_to_string(Image.open(i), lang='por'))
        os.chdir(destino)
        arquivo = open(i[:-4]+'.txt','a')
        arquivo.write(texto)
        arquivo.close()
            
origem = r'C:\Users\carlo\OneDrive\Documents\GitHub\tcc_uel\limiarizadas\.'
destino = r'C:\Users\carlo\OneDrive\Documents\GitHub\tcc_uel\textos'

extracaoTexto(origem, destino)