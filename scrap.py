import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def web_scrap(lei='lei 9503', n=29, inciso='III', alinea='a)'):
    """Deve retornar o título da lei, o Inciso e a alinea solicitados"""
    print('Aguarde enquanto nossos robos procuram pelas informações solicitadas...')
    url = 'https://www2.camara.leg.br/busca/?q=' + lei
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)
    driver.get(url)
    time.sleep(10)
    driver.find_element_by_xpath("//div[@id='resultadoBusca']//ul//li//span//a").click()
    time.sleep(10)
    driver.find_element_by_xpath("//div[@class='sessao']//a").click()
    time.sleep(10)
    element = driver.find_element_by_xpath("//div[@class='texto']")
    titulo = driver.find_element_by_class_name('ementa')
    html_content = element.get_attribute('outerHTML')
    titulo = titulo.get_attribute('outerHTML')
    time.sleep(5)
    driver.quit()

    soup = BeautifulSoup(html_content, 'lxml')
    text = soup.find_all(text=True)

    titulo = BeautifulSoup(titulo, 'lxml')
    titulo = titulo.find_all(text=True)

    for i in range(len(text)):
        text[i] = text[i].replace('\n', '')
        text[i] = text[i].replace('\t', '')
        text[i] = text[i].replace('\xa0', '')

    for i in range(len(titulo)):
        titulo[i] = titulo[i].replace('\n', '')
        titulo[i] = titulo[i].replace('\t', '')

    for i in range(len(text)):
        if '' in text:
            text.remove('')

    for i in range(len(titulo)):
        if '' in titulo:
            titulo.remove('')

    m = 0
    a = 0
    an = 0
    at = 0
    art = str('Art. ' + str(n))
    lista_paragrafo = []
    lista_inciso = []
    lista_alinea = []
    for i in range(len(text)):
        if art in text[i]:
            lista_paragrafo.append(text[i])
            m += 1
        if m != 0 and '§' in text[i]:
            lista_paragrafo.append(text[i])

        if m != 0 and 'Parágrafo único.' in text[i]:
            lista_paragrafo.append(text[i+1])

        if m != 0 and inciso in text[i]:
            lista_inciso.append('Inciso' + text[i])
            m = 0
            a += 1
            if text[i + 1] != 'a)':
                break
         
            for j in range(i, len(text)):
                if m == 0 and '§' in text[j]:
                    lista_paragrafo.append(text[j])
                if str('Art. ' + str(n+1)) in text[j]:
                    break

        if a != 0 and an == 0 and alinea != '' and alinea in text[i]:
            lista_alinea.append('Alinea '+ alinea + text[i+1])
            an += 1

        if str('Art. ' + str(n+1)) in text[i]:
            break

    print(titulo[0])
    print('Nº: ' + lista_paragrafo[0])
    for i in range(1, len(lista_paragrafo)): 
        print(lista_paragrafo[i])
    if len(lista_inciso) > 0:
        print(lista_inciso[0])
    if len(lista_alinea) > 0:
        print(lista_alinea[0])
    print('\n')
    print('Muito obrigado!')