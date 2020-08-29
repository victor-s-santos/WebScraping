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
        self.inciso1 = inciso
        
        self.art = str('Art. ' + str(self.n))
        self.lista_paragrafo = []
        self.lista_inciso = []
        
        url = 'https://www2.camara.leg.br/busca/?q=' + lei
        option = Options()
        option.headless = True
        driver = webdriver.Firefox(options=option)
        driver.get(url)
        driver.find_element_by_xpath("//div[@id='resultadoBusca']//ul//li//span//a").click()
        driver.find_element_by_xpath("//div[@class='sessao']//a").click()
        element = driver.find_element_by_xpath("//div[@class='texto']")
        self.titulo = driver.find_element_by_class_name('ementa')
        html_content = element.get_attribute('outerHTML')
        self.titulo = self.titulo.get_attribute('outerHTML')
        #time.sleep(2)
        driver.quit()

        self.soup = BeautifulSoup(html_content, 'lxml')
        self.texto = self.soup.find_all(text=True)

        self.titulo = BeautifulSoup(self.titulo, 'lxml')
        self.titulo = self.titulo.find_all(text=True)
        
    def title(self):
        """Returns the law title""" 
        for i in range(len(self.titulo)):
            self.titulo[i] = self.titulo[i].replace('\n', '')
            self.titulo[i] = self.titulo[i].replace('\t', '')
            if '' in self.titulo:
                self.titulo.remove('')
            return(self.titulo[0])
   
    def article(self):
        for i in range(len(self.texto)):
            if (f'Art. {int(self.n)}') in self.texto[i]:
                self.texto[i] = self.texto[i].replace('\n', '')
                self.texto[i] = self.texto[i].replace('\t', '')
                self.texto[i] = self.texto[i].replace('\xa0', '')
                self.i2 = i
                return(self.texto[i])

    def paragraph(self):
        self.article()
        """Returns every laws paragraph of the inserted article or the requested paragraph"""
        for i in range(self.i2,len(self.texto)):
            if '' in self.texto:
                self.texto.remove('')
        
        for i in range(self.i2, len(self.texto)):
            if (f'Art. {int(self.n) +1}') in self.texto[i]:
                break

            if '§' in self.texto[i]:
                self.texto[i] = self.texto[i].replace('\n', '')
                self.texto[i] = self.texto[i].replace('\t', '')
                self.texto[i] = self.texto[i].replace('\xa0', '')
                self.lista_paragrafo.append(self.texto[i])
                
        if len(self.lista_paragrafo) == 0:
            return('O artigo requisitado não possui parágrafos.')
        
        if self.p is not None:
            return(self.article(),self.lista_paragrafo[(self.p)-1])
        else:
            return(self.article(),self.lista_paragrafo)
    
    
    def inciso(self):
        """Returns the requested item from the article / law, 
        if no item was requested the entire list is returned"""
        if self.inciso1 is not None:
            for i in range(self.i2, len(self.texto)):
                if (f'Art. {int(self.n) +1}') in self.texto[i]:
                    break
                if (str(self.inciso1)) in self.texto[i]:
                    self.texto[i] = self.texto[i].replace('\xa0', '')
                    return(self.texto[i])
                return('O inciso requisitado não foi encontrado!')
        else:
            for i in range(self.i2, len(self.texto)):
                if (f'Art. {int(self.n) +1}') in self.texto[i]:
                    break
                if ('I' or 'II' or 'III' or 'IV' or 'V'
                   or 'VI' or 'VII' or 'VIII' or 'IX' or 'X') in self.texto[i][0:6]:
                    self.texto[i] = self.texto[i].replace('\xa0', '')
                    self.lista_inciso.append(self.texto[i])
            if(len(self.lista_inciso) == 0):
                return('O artigo requisitado não possui incisos!')
            else:
                return(self.lista_inciso)