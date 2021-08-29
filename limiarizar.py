import cv2 as cv
import numpy as np
import os


def limiarizar(origem, destino):
    nome = []
    for n in os.listdir(origem):
        nome.append(n)

    for i in nome:
        os.chdir(origem)
        img = cv.imread(i)
        img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        #Usando o método de Otsu para executar o limiar automático da imagem
        ret2,th2 = cv.threshold(img_gray,127,255,cv.THRESH_BINARY+cv.THRESH_OTSU) 
        #criação do kernel para usar na dilatação e erosão da imagem
        kernel = np.ones((1,1),np.uint8)
        #aumenta a área da imagem. Usada para aumentar as bordas da imagem
        dilation = cv.dilate(th2,kernel,iterations = 1)
        #corroi os limites do objeto. Usado para diminir as bordas da imagem
        erosion = cv.erode(th2, kernel, iterations=3) 
        os.chdir(destino)
        cv.imwrite(i, erosion)

origem = r'C:\Users\carlo\OneDrive\Documents\GitHub\tcc_uel\cinza\.'
destino = r'C:\Users\carlo\OneDrive\Documents\GitHub\tcc_uel\limiarizadas'        

limiarizar(origem, destino)

