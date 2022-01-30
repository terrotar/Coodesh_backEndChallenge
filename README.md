# Coodesh_backEndChallenge


## Descrição do projeto

This is a challenge by <a href='https://coodesh.com/'>Coodesh</a>

Este projeto é um desafio de processo seletivo backend Python, o qual consiste em realizar uma API que irá consumir Space Flight News API com diversas funcionalidades e implementações, tendo os endpoints com a seguitne estrutura:

- [GET]/: Retornar um Status: 200 e uma Mensagem "Back-end Challenge 2021 🏅 - Space Flight News"

- [GET]/articles/: Listar todos os artigos da base de dados, utilizar o sistema de paginação para não sobrecarregar a REQUEST

- [GET]/articles/{id}: Obter a informação somente de um artigo

- [POST]/articles/: Adicionar um novo artigo

- [PUT]/articles/{id}: Atualizar um artigo baseado no id

- [DELETE]/articles/{id}: Remover um artigo baseado no id


## Como rodar o Programa


Primeiramente é necessário ter instalado o Python e o pip.


Instalar dependências encontradas em requirements.txt:

- <code>pip install -r requirements.txt</code>


Agora com todos requisitos instalados, basta dar o comando no diretório raiz do projeto:

- <code>./run.sh</code>

ou

- <code>python run.py</code>


Para rodar os testes('/app/test_app.py'), basta estar dentro da pasta '/app' e rodar o comando:
- pytest

OBS: Os testes seram exacutados corretamente apenas se a API estiver rodando previamente, caso contrário os teste não irão conseguir acessar os endpoints com suas devidas requisições e informações.


## Tecnologias e Ferramentas

Dentre as ferramentas utilizadas para desenvolver o projeto, foi utilizado:

- Python

- Framework FastAPI

- Heroku

- PostgreSQL

- Docker

- GitHub

- pytest


# Heroku

O projeto foi subido para o Heroku no link <link>https://coodesh-fastapi-backend.herokuapp.com/</a>

OBS: Devido a quantidade grande de linhas da tabela Article e o limite grátis do serviço do postgreSQL do heroku, a aplicação
não ficará disponível após uma semana.


# Docker

Adicionado Dockerfile e publicado o container com nome <strong>terrotar/coodesh-backend-challenge</strong> o qual pode ser encontrado no DockerHub https://hub.docker.com/ e utilizado através do comando:
- docker pull terrotar/coodesh-backend-challenge:latest


# Finalização

Este desafio foi bem legal de ser feito, principalmente pela escolha do framework, se adequando bem à proposta do projeto. Foi utilizado a estrutura de routers dentro do diretório da API(/app) para uma melhor modularização e visualização dos arquivos.

Muitos desafios e aprendizado ocorreram ao decorrer do desenvolvimento, o qual foi muito corrido devido o tempo limite(5 dias).
A parte inicial de realizar a lógica dos endpoints e suas estruturas não foi tão complicado, como a parte de paginação para não sobrecarregar o request e funcionalidades de CRUD.

Por outro lado, algumas partes foram muito complexas para serem criadas, como o setup de um cron, o qual eu nunca havia usado e foi bem difícil de implementar, o qual ainda não está funcionando corretamente. Passei um bom tempo tentando resolver esse problema, e como no escopo ressaltava a palavra CRON, tentei ser fiel ao escopo e realizar a implementação do próprio cron pelo bash, sem utilizar pacotes terceiros de gerenciamento no primeiro momento. Por esse motivo há um run.sh no diretório raiz, sendo uma das alternativas as quais tentei para solucionar o problema. Tentei utilizar posteriormente, mesmo não sendo o ideial, bibliotecas como apscheduler e python-crontab, não tendo sucesso em ambas também.

Eu já havia criado outros projetos utilizando o framework FastAPI porém não com todas essas funcionalidades, como integração de banco de dados, CRUD's, heroku e docker simultaneamente. Foi certamente um aprendizado que obtive, e aprendi mais ainda sobre o funcionamento das tecnologias utilizadas. Infelizmente a parte do cron não foi implementada corretamente mas certamente é um dos tópicos que o projeto me incentivou a estudar sobre. Ainda tive a oportunidade de conhecer e trabalhar mais com scripts, algo que não estou muito acostumado a fazer e que certamente é muito interessante e funcional, principalmente para realizar diversos comandos ao criar o Dockerfile, visto que o mesmo só aceita um CMD por arquivo.

Busquei entregar o máximo de meus conhecimentos em Python e desenvolvimento de API's que obtive desde meus estudos em programação, e apesar de não ter ficado muito satisfeito com o cronograma de atualizar o database, gostei do resultado final da aplicação e pela oportunidade de participar desse processo e de aprender mais ainda. Apesar de não ter muita experiência na área de tecnologia, fico feliz em ver que cada vez mais há processos os quais recomendam o uso do FastAPI, um framework que realmente é muito efetivo e está cada vez mais solido no mercado de Python. Apesar de não dominar complemente ainda as suas funcionalidades e principais conceitos, como async e await, busquei implementar o meu melhor e da melhor forma. Acredito que poderia ter explorado melhor as funções assincronas no gerador automático para atualizar o banco de dados, consumindo assim menos memória e deixando o projeto mais rápido, inclusive as vezes tendo alguns 'timeouts', mas mesmo sendo possível uma melhoria de performance está funcional.
