from contextlib import nullcontext
from turtle import st


from matplotlib import pyplot as plt
import numpy as np
import cv2
import os





def carregar_imagem(caminho, color):
    if(caminho != nullcontext):
        img = cv2.imread(caminho)  # Carrega Imagem apartir do caminho passado
    else:
        print("Nenhum caminho passado no parametro ""caminho""")

    match color:  # Informa o padão de cor que vai retornar
        case 0:
            # Converte imagem para Escala de Cinza
            imgAux = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            return imgAux
        case 1:
            # Converte imagem de BGR para RGB
            imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return imgRGB
        case 2:
            
            return img  # Retorna Imagem em formato BGR
        case _:
            print("Valor invalido para o parametro ""color""")
            return False


def start_recortar_imagens(linha, coluna, espacamento, flagAnalise):

    dir_principal = "backend/image/cache"
    filename = os.listdir(dir_principal)
    num_img = 0
    total_fotos = 0
    for fn in filename:
        fotos = 0
        num_img = num_img + 1
        dir = dir_principal +"/"+ str(fn)

        img = carregar_imagem(dir, 2)
       
        img, cont_linhas ,cont_colunas = recortar_imagem(linha, coluna, espacamento, img)

        if(flagAnalise == True):

            filename = os.listdir("dataset/analise/")

            for a in filename:
                os.remove("dataset/analise/"+str(a))

            for i in range(0, cont_linhas):
                for z in range(0, cont_colunas):
                    cv2.imwrite('dataset/analise/img_'+ str(num_img) +'_new_'+ str(i + 1) +'_' + str(z + 1) +'_.png', img[fotos])
                    fotos = fotos + 1
            total_fotos = total_fotos + fotos

        else:

            filename = os.listdir("dataset/new/")

            for a in filename:
                os.remove("dataset/new/"+str(a))
            #Salva as imagens cortadas na pasta de Testes dentro do DATASET
            for i in range(0, cont_linhas):
                for z in range(0, cont_colunas):
                    cv2.imwrite('dataset/new/img_'+ str(num_img) +'_analise_'+ str(i + 1) +'_' + str(z + 1) +'_.png', img[fotos])
                    fotos = fotos + 1
            total_fotos = total_fotos + fotos
    
    return total_fotos

def recortar_imagem(linha, coluna, espacamento, imagem):
    
    cont_linhas = 0
    img_cut_array = []

    espacamento = int(espacamento)
    linha = int(linha)
    coluna = int(coluna)

    
    for y in range(0, imagem.shape[0], espacamento):  # percorre linhas, ultimo numero é  a distancia que vai percorer para cortar uma nova imagem
        if(imagem.shape[0] < y + espacamento):
            break
        cont_colunas = 0
        cont_linhas = cont_linhas + 1
        for x in range(0, imagem.shape[1], espacamento):

            if(imagem.shape[1] < x + espacamento):
                break
            
            img_cut = imagem[y : y + linha, x : x + coluna]
            
            cont_colunas = cont_colunas + 1 
            img_cut_array.append(img_cut)

    return img_cut_array, cont_linhas, cont_colunas