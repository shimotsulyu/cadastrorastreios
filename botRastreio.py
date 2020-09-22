import time
import pandas as pd
print('class startMuambator loaded')

class startMuambator:
    def __init__(self,bot,usuario,senha,target,t=2,viewuser=False):
        self.bot = bot
        bot.openweb('https://www.muambator.com.br/'+target)
        time.sleep(t)
        if viewuser is True:
            print('login com:',usuario)
        if senha is not None:
            print('Autenticado com a senha.')
        pusuario ='//input[@id="username-form"]'
        psenha = '//input[@id="password-form"]'
        bot.login(usuario,senha,pusuario,psenha)
        time.sleep(2+t)
   
    def rastreioClientes(self,t=2):
        bot = self.bot
        bot.rolarbarra(1)
        paginas = bot.coletarinfo('//*[@id="wrapper"]/div[3]/div[1]/div[3]/nav/ul/li[1]')
        paginas = int(paginas[0].split('de')[1].strip()[0:-1])
        dataFULL = pd.DataFrame()
        time.sleep(t)
        for i in range(1,paginas):
            bot.openweb('https://www.muambator.com.br/pacotes/pendentes/?page='+str(i))
            time.sleep(2+t)
            data = pd.DataFrame()
            bot.rolarbarra(1)
            idvenda = bot.coletarinfo('//td[@class="title"]/span[1]')
            cliente = bot.coletarinfo('//td[@class="title"]/a[@href]')
            situacao = bot.coletarinfo('//td[@class="text-center infos"]/img[1]','data-original-title')
            postagem = bot.coletarinfo('//td[@class="text-center infos"]/small[1]')
            tempo = bot.coletarinfo('//td[@class="title"]/small[1]')
            link = bot.coletarinfo('//td[@class="title"]/a[@href]','href')
            data['idvenda'] = idvenda
            data['cliente'] = cliente            #bot.openweb(link)
            #bot.click('//*[@id="add_package"]/button')
            data['situacao'] = situacao
            data['postagem'] = postagem
            data['tempo'] = tempo
            data['link'] = link
            dataFULL = dataFULL.append(data)
            time.sleep(2+t)
        dataFULL = dataFULL.reset_index(drop=True)
        print('FIM rastreioClientes')
        return dataFULL
    
    def cadastro(self,envios,link):
        bot = self.bot
        print(len(envios), 'rastreios')
        for i in range(0,len(envios)):
            print(i+1,'cadastrando:',envios['Nome do destinatário'][i])
            print('    ',envios['Número de rastreamento'][i],'|',envios['ID do pedido'][i])
            time.sleep(1)
            bot.inserirtexto('//*[@id="id_codigo"]',envios['Número de rastreamento'][i],enter=False,fast=True,t=1)
            #envios['ID do pedido'][i]
            #envios['Nome do destinatário'][i]
            #envios['Nome do destinatário'][i].split(' ')[0]+' '+envios['Nome do destinatário'][i].split(' ')[-1]
            bot.inserirtexto('//*[@id="id_nome"]',envios['Nome do destinatário'][i].split(' ')[0]+' '+envios['Nome do destinatário'][i].split(' ')[-1]+' '+envios['ID do pedido'][i],enter=True,fast=True)
            #bot.inserirtexto('//input[@id="id_tags"]',envios['ID do pedido'][i],enter=True,fast=True)
            time.sleep(1)
        print('****Todos os rastreios foram cadastrados!')
        time.sleep(5)
