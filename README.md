# Univesp_BOT
**Projeto Integrador, BOT Informacional que ajuda alunos e interessados, a respeito da UNIVESP.
As informaçõe no BOT estão estáticas, pois não temos uma API da Universidade, com determinadas informaçções para consumir. Porém, é um ótima maneira de demonstrar o básico de um projeto de bot já com a utilização de padrẽs de projeto.**

## Tecnologias Utilizadas 
* [Discord Developer 💬](https://discord.com/developers/applications)
* [Python 🐍](https://www.python.org/)

## Como criar um BOT  
**É fácil criar um robô no Discord, porém acredito que seria bem mais fácil seguir um vídeo. Pensando nisso disponibilizarei um link de um vídeo qual explica como criar um bot, já com script python indexado.**

📎 [Link do video 📹](https://www.youtube.com/watch?v=Pi5I-vVxPZw)

## Como rodar o BOT 
**Primeiramente precisamos ter o Python instalado na máquina. 
Após ter o Python instalado, vamos baixar o código com o git ou baixando o código fonte em .zip.
Então temos essa estrutura de código.**

![Estrutura do Código](https://github.com/janderteodoro/Univesp_BOT/blob/master/img/codeStructure.png?raw=true)

**Então criamos um ambiente virtual do Python:** 

* Linux<br>
`python3 -m venv venv`

* Windows<br>
`py -m venv venv`

**Agora ativamos o ambiente que criamos, para poder instalar as dependências de maneira isolada:**

* Linux<br>
`source venv/bin/activate`

* Windows<br>
`venv\Scripts\activate`

Após ativar, temos a seguinte extrutura, e uma indicação que nosso ambiente virtual está ativo


* Estrutura do código após criar ambiente virtual<br>
![Estutura atualizada](https://github.com/janderteodoro/Univesp_BOT/blob/master/img/Captura%20de%20Tela-20220326144440-223x297.png?raw=true)

* Ambiente ativo<br>
![Ambiente Ativo](https://github.com/janderteodoro/Univesp_BOT/blob/master/img/Captura%20de%20Tela-20220326144137-409x20.png?raw=true)

* Agora vamos instalar as dependências do projeto<br>
`pip install -r requirements.txt`

* Agora só falta colocarmos nosso token, que está disponível no Discord Developers. Na raiz do projeto crie um novo arquivo `.env` e ele coloque seu token. `TOKEN=coloqueseutokenaqui`