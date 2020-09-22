from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
import getpass
from botStart import startBot
from botRastreio import startMuambator

driver = webdriver.Chrome('/usr/bin/chromedriver')
bot = startBot(driver)
usuario = input('Usuario: ')
senha = getpass.getpass('Digite sua senha: ')
botMuambator = startMuambator(bot,usuario,senha,'pacotes/pendentes/')

import pandas as pd
estado = True
while estado:
    arquivo = input('arquivo:')
    end = '../etiquetas/arquivos/'+arquivo
    print('Deseja cadastrar',end,'?')
    confirma = input('S/N: ')
    if confirma.upper() == 'S':
        estado = False
        input('Pressione ENTER para continuar.')
        envios = pd.read_excel(end,sep=';')
        envios = envios[['ID do pedido','Número de rastreamento','Nome do destinatário']].dropna().reset_index(drop=True)
        botMuambator.cadastro(envios,'https://www.muambator.com.br/login/?next=/pacotes/pendentes/')
        try:            
            print('Autenticado com a senha')
            input('FIM. Pressione ENTER para continuar.')
            #driver.quit()
        except SyntaxError:
            pass
    elif confirma.upper() == 'N':
        print('\nInsira um arquivo novamente.')
    else:
        print('\nErro. Insira um arquivo novamente.')
