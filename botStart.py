from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random
print('class startBot loaded')

class startBot:
    def __init__(self,driver):
        self.driver = driver
    
    def openweb(self,target,t=2):
        driver = self.driver
        driver.get(target)
        time.sleep(t)
        
    def login(self,usuario,senha,pusuario,psenha):
        print('conectando')
        driver = self.driver
        self.inserirtexto(pusuario,usuario,enter=False,fast=True)
        self.inserirtexto(psenha,senha,enter=True,fast=True)
        
    def click(self,target):
        driver = self.driver
        driver.find_element_by_xpath(target).click()
        
    def rolarbarra(self,vezes,t=2):
        driver = self.driver
        for i in range(0,vezes):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight/0.001);')
            time.sleep(t)
            
    def coletarinfo(self,target,attribute=None):
        driver= self.driver
        caixa = driver.find_elements_by_xpath(target)
        if attribute is None:
            return [elem.text for elem in caixa]
        else:
            hrefs = [elem.get_attribute(attribute) for elem in caixa]
            return hrefs
        
    @staticmethod
    def digitaraleatorio(frase, target):
        for letra in frase:
            target.send_keys(letra)
            time.sleep(random.randint(1,5)/30)
            
    def inserirtexto(self,target,texto,enter=True,fast=False,t=2):
        driver = self.driver
        driver.find_element_by_xpath(target).click()
        caixa = driver.find_element_by_xpath(target)
        #time.sleep(t)
        caixa.clear()
        time.sleep(t)
        #caixa.clear()
        if fast is True:
            caixa.send_keys(texto)
        else:
            for letra in texto:
                caixa.send_keys(letra)
                time.sleep(random.randint(1,5)/30)
        time.sleep(t)
        if enter is True:
            caixa.send_keys(Keys.RETURN)
