import cv2 as cv
import os


def converteCinza(origem, destino):
    name = []
    #percorre o diretório de origem e extrai nome dos arquivos
    for n in os.listdir(origem):
        name.append(n)

    for i in name:
        #vai para o diretorio de origem
        os.chdir(origem)
        img = cv.imread(i)
        #converte as imagens em escala de cinza
        imgCinza = cv.cvtColor(img, cv.COLOR_BGR2GRAY,9)
        #salva os arquivos em escala de cinza no diretorio de destino
        os.chdir(destino)
        cv.imwrite(i, imgCinza)

origem = 'coloridas\.'
destino = '\cinzas'

converteCinza(origem, destino)

