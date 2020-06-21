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