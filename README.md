# Sobre
> Neste repositório utilizando poucas bibliotecas da linguagem python e a ferramenta Selenium, que é muita utilizada na criação de testes funcionais, é criado um script python que acesse dada lei, artigo, inciso e alínea fornecidos pelo usuário, retornando estes valores do acesso a fonte https://www2.camara.leg.br/busca/?q=' + lei.

# Como rodar
> Para a execução deste projeto, siga o passo a passo:
1. Criando um ambiente virtual,virtualenv, (apesar de não necessário, isola o projeto de outros notebooks, uma boa prática):
    * python3 -m venv .venv `para criar o virtualenv`
    * source .venv/bin/activate `para ativar este ambiente`

2. Clone o repositório:
    * git clone https://github.com/victor-s-santos/WebScraping.git

3. Instalar as dependências:
    3.1.1. Jupyter:
    * pip install ipython[notebook] `para instalar o jubpyter`
    3.1.2. Instalando as dependências do Jupyter:
    > Executar dentro de um kernel em execução do jupyter.
    import sys
    !{sys.executable} -m pip install -r requirements.txt

4. Rodar o Notebook:
> Dentro do virtualenv criado:
    * ipython notebook

# Scrap1.ipynb
> Neste notebook a ideia implementada é de extrair todas as leis presentes nas fontes usadas e exportá-las em um csv ou mesmo uma visualização melhor utilizando o pandas. Há uma quantidade muito grande de leis, portanto há uma grande necessidade de tratamento dos dados, haja vista que as páginas que contenham as leis não estão bem formatadas. 

# Scrap2.ipynb e Scrap_notebook.ipynb
> Neste notebook foi aplicada a ideia principal, de buscar somente a lei, artigo, inciso e alínea solicitados pelo usuário. O código central do notebook scrap2 foi refatorado e copiado para o notebook scrap_notebook.

# Scrap.py
> Arquivo python que contem somente a parte funcional do notebook scrap_notebook.ipynb.

# Selenium
> O Selenium foi escolhido pois sua integração permitia que informações contidas em páginas que são produtos de algum framework javascript (como Vue e React) possam ser coletadas, e então tratadas. Como o python, através de requests, não consegue ler javascript, o selenium foi utilizado por conseguir trazer estas informações através do navegador (no caso, Firefox). Foi definido que o navegador executasse em 'segundo plano' (não era aberto visualmente), e como trata-se de requisições assíncronas, é necessário um timer (usado 10 segundos, em virtude da instabilidade de minha conexão) para que o python só fosse coletar a informação após o navegador carregá-la. 


# BeautifulSoup
>Principal biblioteca python na função de webscrap. Neste repositório ele possui a função de parsear a informação coletada em html. Como as páginas requisitadas não possuem uma boa estruturação em html assim como não há um padrão, não foi possível explorar mais das funcionalidades desta biblioteca. O texto coletado teve de ser tratado com if's simples do python.  
