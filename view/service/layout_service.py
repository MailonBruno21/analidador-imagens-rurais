import os, sys
from pickle import FALSE
import shutil
import tkinter as tk
from tkinter import filedialog

import time

from view.style.layout import Ui_MainWindow

from PyQt5 import QtGui
from PyQt5.QtWidgets import QMainWindow

from backend.service import image_service as ims
from backend.service import rede_neural as rn


class Layout_service:
    def __init__(self) -> None:
        self.main_win = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)

        #-- MAPEANDO OS BOTÕES DO MENU DO HEADER
        self.ui.pushButton_analizar.clicked.connect(self.analisar_header)
        self.ui.pushButton_imagem.clicked.connect(self.imagem_header)
        

        #######################################
        #-- MAPEANDO OS BOTÕES DO MENU ANALISAR
        #######################################
        self.ui.pushButton_load_cortar.clicked.connect(self.cortar)
        self.ui.pushButton_analisar_img.clicked.connect(self.analisar)
        self.ui.pushButton_relatorio.clicked.connect(self.relatorio)
        self.ui.pushButton_home_analisar.clicked.connect(self.show)


        #######################################
        #-- MAPEANDO OS BOTÕES DO MENU IMAGEM
        #######################################
        self.ui.pushButton_aplic_filtros.clicked.connect(self.filtros)
        self.ui.pushButton_abrir_imagem.clicked.connect(self.imagem_header)
        self.ui.pushButton_voltar_img.clicked.connect(self.show)

        ###################################################
        #-- MAPEANDO OS BOTÕES DA PAGINA ANALISAR -> CORTAR
        ###################################################
        self.ui.pushButton_busca_cortar.clicked.connect(self.buscar_imagem_no_sistema)
        self.ui.pushButton_abrir_cortar.clicked.connect(self.abrir_imagem)
        self.ui.radioButton_dataset.clicked.connect(self.cotar_img_radion_button)
        self.ui.radioButton_analise.clicked.connect(self.cotar_img_radion_button)
        self.ui.pushButton_proximo.clicked.connect(self.proxima_imagem)
        self.ui.pushButton_anterior.clicked.connect(self.anterior_imagem)
        self.ui.pushButton_salvar_cut.clicked.connect(self.recortar_imagem)

        ###################################################
        #-- MAPEANDO OS BOTÕES DA PAGINA ANALISAR -> ANALISAR
        ###################################################
        self.ui.pushButton_treinar_novo_modelo.clicked.connect(self.treinar)
        

   
        
    #-- MAPEANDO AS FUNÇÕES DO MENU DO HEADER
    def analisar_header(self):
        self.ui.stackedWidget_Analise.setCurrentWidget(self.ui.page_analisar_imagem)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_analisar)

    def imagem_header(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.abrir_imagem)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_imagens)
    

    #-- MAPEANDO AS FUNÇÕES DA HOME
    def show(self):
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_main)
        self.main_win.show()
    

    #-- MAPEANDO AS FUNÇÕES DO MENU ANALISAR
    def cortar(self):

        filename = os.listdir("backend/image/cache")

        for a in filename:
            os.remove("backend/image/cache/"+str(a))


        self.ui.radioButton_analise.setChecked(True)

        var = self.ui.radioButton_analise.isChecked()
        if(var == True):
            self.ui.lineEdit_largura.setEnabled(False)
            self.ui.lineEdit_altura.setEnabled(False)
            self.ui.lineEdit_espacamento.setEnabled(False)

            self.ui.lineEdit_largura.setText("342")
            self.ui.lineEdit_altura.setText("342")
            self.ui.lineEdit_espacamento.setText("342")
        else:
            self.ui.lineEdit_largura.setEnabled(True)
            self.ui.lineEdit_altura.setEnabled(True)
            self.ui.lineEdit_espacamento.setEnabled(True)

        self.ui.stackedWidget_Analise.setCurrentWidget(self.ui.page_cortar_imagem)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_analisar)

    def analisar(self):
        self.ui.stackedWidget_Analise.setCurrentWidget(self.ui.page_analisar_imagem)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_analisar)
    
    def relatorio(self):
        self.ui.stackedWidget_Analise.setCurrentWidget(self.ui.page_montar_imagem)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_analisar)


    #-- MAPEANDO AS FUNÇÕES DO MENU IMAGEM
    def filtros(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.aplicar_filtros)
        self.ui.stackedWidget_analisar.setCurrentWidget(self.ui.page_imagens)


    #-- MAPEANDO AS FUNÇÕES DA PAGINA ANALISAR -> ANALISAR


    #####################################################
    ##-- MAPEANDO AS FUNÇÕES DA PAGINA ANALISAR -> CORTAR
    #####################################################
    def buscar_imagem_no_sistema(self):
        root = tk.Tk()
        root.withdraw()
        file_path = filedialog.askopenfilenames()
        num = 1
        for a in file_path:

            path_interna = "backend/image/cache/imagem_selecionada_"+str(num)+".jpg"
            print(a)
            shutil.copy(a, path_interna)
            num = num + 1
            time.sleep(0.5)

        self.ui.label_num_fotos.setText("1")
        self.ui.lineEdit_cortar_img.setText(str(file_path[0]))
        self.ui.label_img_cut.setPixmap(QtGui.QPixmap(str(file_path[0])))
        
        filename = os.listdir("backend/image/cache")
        caminho = str(filename[0])
        img = ims.carregar_imagem("backend/image/cache/" + caminho, 2)
        self.ui.label_largura_cut.setText(str(img.shape[1]))
        self.ui.label_altura_cut.setText(str(img.shape[0]))
         
    def abrir_imagem(self):

        filename = os.listdir("backend/image/cache")
        #FUNCAO DE CARREGAR A IMAGEM
        caminho = str(filename[0])
        print(filename)
        img = ims.carregar_imagem("backend/image/cache/" + caminho, 2)
        self.ui.label_largura_cut.setText(str(img.shape[1]))
        self.ui.label_altura_cut.setText(str(img.shape[0]))
       
    def proxima_imagem(self):
        filename = os.listdir("backend/image/cache")
        qtd_file = 0
        for a in filename:
            qtd_file = qtd_file + 1
        #FUNCAO DE CARREGAR A IMAGEM
        a = self.ui.label_num_fotos.text()
        a = int(a)
        
        print(qtd_file)
        print("proxima")
        print(a)
        if(a < qtd_file):
            a = int(a) + 1
            caminho = str(filename[a-1])
            img = ims.carregar_imagem("backend/image/cache/" + caminho, 2)

            self.ui.label_img_cut.setPixmap(QtGui.QPixmap("backend/image/cache/" + caminho))
            self.ui.label_largura_cut.setText(str(img.shape[1]))
            self.ui.label_altura_cut.setText(str(img.shape[0]))
            
            self.ui.label_num_fotos.setText(str(a))
    
    def anterior_imagem(self):
        filename = os.listdir("backend/image/cache")
        
        #FUNCAO DE CARREGAR A IMAGEM
        a = self.ui.label_num_fotos.text()
        a = int(a)

        print("anterior")
        print(a)
        if(a > 1):
            a = int(a) - 1
            caminho = str(filename[a-1])
            img = ims.carregar_imagem("backend/image/cache/" + caminho, 2)

            self.ui.label_img_cut.setPixmap(QtGui.QPixmap("backend/image/cache/" + caminho))
            self.ui.label_largura_cut.setText(str(img.shape[1]))
            self.ui.label_altura_cut.setText(str(img.shape[0]))
            
            self.ui.label_num_fotos.setText(str(a))

    def cotar_img_radion_button(self):

        var = self.ui.radioButton_analise.isChecked()
        if(var == True):
            self.ui.lineEdit_largura.setEnabled(False)
            self.ui.lineEdit_altura.setEnabled(False)
            self.ui.lineEdit_espacamento.setEnabled(False)

            self.ui.lineEdit_largura.setText("342")
            self.ui.lineEdit_altura.setText("342")
            self.ui.lineEdit_espacamento.setText("342")
        else:
            self.ui.lineEdit_largura.setEnabled(True)
            self.ui.lineEdit_altura.setEnabled(True)
            self.ui.lineEdit_espacamento.setEnabled(True)
    
    def recortar_imagem(self):
        linha = self.ui.lineEdit_largura.text()
        coluna = self.ui.lineEdit_altura.text()
        espacamento = self.ui.lineEdit_espacamento.text()

        

        var = self.ui.radioButton_analise.isChecked()

        total_fotos = ims.start_recortar_imagens(linha,coluna,espacamento, var)

        self.ui.label_tota_fotos_num.setText(str(total_fotos))


    #######################################################
    ##-- MAPEANDO AS FUNÇÕES DA PAGINA ANALISAR -> ANALISAR
    #######################################################
    def treinar(self):
        altura = self.ui.lineEdit_altura_novo_modelo.text()
        largura = self.ui.lineEdit_largura_novo_modelo.text()
        rn.treinar_rede_neural(int(altura), int(largura))


    
    


