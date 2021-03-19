import re
import pandas as pd
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
#lei=law, n=article number, p=paragraph number, inciso=item, alinea=point
class Scrap:
    def __init__(self, lei, n=None, p=None, inciso=None):
        """Initializing the driver"""
        self.lei = lei
        self.n = n
        self.p = p
        self.art = str('Art. ' + str(self.n))
        self.lista_paragrafo = []
        self.lista_inciso = []
    
    def conecta(self):
        self.url = 'https://www2.camara.leg.br/busca/?q=' + self.lei
        option = Options()
        option.headless = False
        driver = webdriver.Firefox(options=option)
        driver.get(self.url)
        driver.find_element_by_xpath("//div[@id='resultadoBusca']//ul//li//span//a").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='sessao']//a").click()
        time.sleep(1)
        element = driver.find_element_by_xpath("//div[@class='texto']")
        self.titulo = driver.find_element_by_class_name('ementa')
        self.html_content = element.get_attribute('outerHTML')
        self.titulo = self.titulo.get_attribute('outerHTML')
        driver.quit()
        return self.html_content
        
    def title(self):
        """Returns the law title"""
        self.soup = BeautifulSoup(self.html_content, 'lxml')
        self.texto = self.soup.find_all(text=True)
        self.titulo = BeautifulSoup(self.titulo, 'lxml')
        self.titulo = self.titulo.find_all(text=True)
        for i in range(len(self.titulo)):
            self.titulo[i] = self.titulo[i].replace('\n', '')
            self.titulo[i] = self.titulo[i].replace('\t', '')
        return self.titulo[0]
   
    def article(self):
        self.inicio_article = re.search(f'Art. {self.n}', self.html_content).start()
        return self.html_content[self.inicio_article:].replace('&nbsp;', '-').split('<br>')[0]
    
    def paragraph(self):
        """Returns the requested paragraph"""
        self.conteudo = BeautifulSoup(self.html_content, 'lxml').find_all()[0]
        self.conteudo = str(self.conteudo).replace('\xa0', '')
        """buscando o artigo"""
        inicio_artigo = re.search(f'Art. {self.n}', self.conteudo).start()
        fim_artigo = re.search('<b', self.conteudo[(inicio_artigo):]).start()
        #str(paragrafo[0])[inicio_artigo:].replace('\xa0', '').split('<br/>')[0]
        fim_artigo += inicio_artigo
        self.conteudo[inicio_artigo: fim_artigo]
        if self.p == 0:
            inicio_article = re.search(f'Art. {self.n}', self.html_content).start()
            inicio_paragrafo_unico = re.search('Parágrafo único.', self.conteudo[fim_artigo:]).start()
            fim_paragrafo_unico = re.search('<br/>', self.conteudo[(fim_artigo + inicio_paragrafo_unico):]).start()
            fim_paragrafo_unico += inicio_paragrafo_unico
            conteudo2 = self.conteudo[fim_artigo:]
            conteudo2 = conteudo2[inicio_paragrafo_unico : fim_paragrafo_unico].replace('</i>', '')
            return(conteudo2)
        return('Ainda não implementado a busca de parágrafos numerados.')
   

teste = Scrap('lei 1.060', n=2, p=0)
teste.conecta()
print(f'Título da lei:{teste.title()}\n')
print(f'Artigo requisitado: {teste.article()}\n')
print(f'Parágrafo requisitado: {teste.paragraph()}\n')