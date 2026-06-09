

#  :::::::::::::::::::::::::::

#  ÍNDICE:

#   ex00 - Introdução
#   ex01 - Variáveis
#   ex02 - Inputs
#   ex03 - Condição If
#   ex04 - Condição If e Operadores Lógicos
#   ex05 - Condição If e Operadores Lógicos
#   ex06 - for loop
#   ex07 - While loop
#   ex08 - #   exercícios
#   ex09 - Try Except
#   ex10 - #   exercícios
#   ex11 - Validação de inputs
#   ex12 - Funções
#   ex13 - Exercícios
#   ex14 - Listas
#   ex15 - Dicionários
#   ex16 - Sets
#   ex17 - all(), any(), not any()
#   ex18 - Exercícios


#  :::::::::::::::::::::::::::

#  COMO INICIAR?

#  1. Instalar Python
#     Ir ao site oficial: Python
#     Instalar versão 3.x (>= 3.10 recomendado)
#     MUITO IMPORTANTE: marcar a opção "Add Python to PATH"
#     Testar no terminal:
#     python --version

#  2. Instalar VS Code

#  3. Instalar extensões

#  4. Criar pasta do projeto
#     mkdir meu_projeto_flask
#     cd meu_projeto_flask
#     Abrir no VS Code:
#     code .

# 5. Criar ambiente virtual (boa prática):
#    python -m venv venv
#    Ativar o ambiente virtual:
#    venv\Scripts\activate
#    Se der erro de permissões: 
#    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

#   OS PASSOS SEGUNTES SÃO PARA PROJETOS FLASK

#  6. Instalar Flask
#     pip install flask
#     Confirmar instalação:
#     pip list (deverá aparecer "Flask")

#  7. Criar ficheiro inicial - app.py
#     from flask import Flask
#    
#     app = Flask(__name__)
#    
#     @app.route('/')
#     def home():
#         return "Olá Flask!"
#    
#     if __name__ == '__main__':
#         app.run(debug=True)

#  8. Executar o projeto
#     python app.py
#     e abrir no browser: http://127.0.0.1:5000

#  9. (Opcional mas recomendado) requirements.txt  para replicar o ambiente virtual noutro computador
#     pip freeze > requirements.txt
#     pip install -r requirements.txt


#  PROBLEMAS COMUNS NA INSTALAÇÃO:
#     Python não está no PATH → python não funciona
#     PowerShell bloqueia venv → resolver com Set-ExecutionPolicy
#     VS Code não detecta Python → selecionar interpreter manualmente

#  :::::::::::::::::::::::::::
#  Ambientes virtuais (MUITO importante)
#  Criar ambiente virtual
#  python -m venv venv
#  Ativar
#  source venv/bin/activate
#  venv\Scripts\activate
#  Sair / desativar
#  deactivate """
# Nota: Quando não é permitido executar o ambiente virtual:
# Allow local scripts for your user account
# Open PowerShell as Administrator and run:
# Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
# Reiniciar powershell


#  :::::::::::::::::::::::::::
#  Comandos mais usados:

#  cd
#  ls / dir      (linux / windows)
#  python ficheiro.py
#  pip install
#  python -m venv
#  source venv/bin/activate
#  deactivate
#  clear / cls   (linux / windows)
#  python -m pip install --upgrade pip
#  pip list   -> (listar os packages instalados no virtualenv)



#  :::::::::::::::::::::::::::
#  Fluxo profissional típico

#  Criar pasta do projeto
#  Entrar na pasta
#  Criar ambiente isolado
#  Ativar ambiente
#  Instalar dependências
#  Correr a aplicação



#  :::::::::::::::::::::::::::
#  Na prática:

#  mkdir projeto                         -> Cria uma pasta chamada projeto onde ficará o código da aplicação.
#  cd projeto                            -> Entra dentro da pasta do projeto para trabalhares no seu conteúdo.
#  python -m venv venv                   -> Cria um ambiente virtual chamado venv. Faz-se apenas uma vez por projeto.
#                                           O ambiente virtual isola as dependências do projeto das bibliotecas globais do sistema.
#                                           O primeiro venv é o módulo Python.
#                                           O segundo venv é o nome da pasta onde ficará o ambiente.
#  source venv/bin/activate  OU          -> Ativar o ambiente virtual, sempre que se abre um terminal para trabalhar no projeto. Se for Linux/macOS
#  venv\Scripts\activate                    Se for Windows
#                                           Depois desta ativação, os comandos python e pip passam a usar as bibliotecas dentro do venv.
#  pip install flask                     -> Instala o framework web Flask dentro do ambiente virtual, e não globalmente.
#                                           Assim o projeto fica mais controlado e reproduzível.
#  python app.py                         -> Executa o ficheiro principal da aplicação. Normalmente este ficheiro contém o servidor Flask que começa a ouvir pedidos HTTP.



#  ::::::::::::::::::::::
#  Dicas úteis:

#  Atualizar o pip "python -m pip install --upgrade pip" :
#  quando crias o projeto
#  quando aparece aviso de versão desatualizada
#  quando precisas de features novas do pip
#  Normalmente basta uma vez no início do projeto.

#  Não precisas de executar diariamente, atualizar pip sem necessidade pode até ser indesejável porque:
#  pode introduzir mudanças comportamentais
#  pode quebrar dependências antigas



#  ::::::::::::::::::::::::::
#  Regra profissional:
#    Nunca se desenvolve Python fora do venv.
#    Sempre:
#         . Ativar venv
#         - Instalar packages
#         - Trabalhar



#  :::::::::::::::::::::::::::  REQUIREMENTS  ::::::::::::::::::::::::::::::::::::
#  Muito importante (nível profissional)
#  Quando o projeto crescer crias:
#  pip freeze > requirements.txt
#  Isso permite reproduzir o ambiente que mais tarde pode ser reproduzido com:
#  pip install -r requirements.txt



#  :::::::::::::::::::::::::::
#  Variáveis de ambiente

#  Nunca guardes segredos diretamente no código.
#  Usa ficheiros .env:
#  DATABASE_URL=...
#  SECRET_KEY=...
#  E carrega-os com:
#  pip install python-dotenv

#  :::::::::::::::::::::::::::
#  Ferramenta
#  venv          -> Padrão Python moderno       
#  virtualenv    -> Mais antigo, mas ainda usado
#  conda         -> Projetos científicos e ML   



#  :::::::::::::::::::::::::::
#  Estrutura profissional de projeto Flask (boa prática)
#  Exemplo de estrutura limpa: 

#   pasta_do_projeto/
#  │
#  ├── app/
#  │   ├── __init__.py
#  │   ├── routes.py
#  │   ├── models.py
#  │   ├── config.py
#  │   ├── static/
#  │   └── templates/
#  │
#  ├── venv/
#  ├── requirements.txt
#  ├── .env
#  ├── app.py
#  └── README.md

#  Explicação:

#  app/          -> código principal da aplicação
#  static/       -> CSS, JS, imagens
#  templates/    -> HTML (se usares renderização server-side)
#  models.py     -> base de dados
#  config.py     -> configurações
#  app.py        -> ponto de entrada



#  :::::::::::::::::  PACKAGES  ::::::::::::::::::::
#  Packages Python comuns 

#  1️ mysql-connector-python
#  pip install mysql-connector-python
#  Conector oficial MySQL para Python. Permite queries, commit/rollback.
#  import mysql.connector

#  2️ pymysql
#  pip install pymysql
#  Conector MySQL puro Python, muito usado em web apps.
#  Suporta cursor como dict e 'with' para gestão automática de recursos.
#  import pymysql

#  3️ fastapi
#  pip install fastapi
#  Framework moderna para APIs REST, async e rápida.
#  from fastapi import FastAPI

#  4️ uvicorn
#  pip install uvicorn
#  Servidor ASGI para correr FastAPI ou Starlette.
#  Exemplo: uvicorn main:app --reload
#  import uvicorn

#  5️ sqlalchemy
#  pip install sqlalchemy
#  ORM para mapear tabelas como classes Python.
#  from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

#  6️ python-dotenv
#  pip install python-dotenv
#  Lê variáveis de ambiente de ficheiros .env
#  from dotenv import load_dotenv

#  7️ requests
#  pip install requests
#  Requisições HTTP simples para consumir APIs externas
#  import requests

#  8️ pandas
#  pip install pandas
#  Manipulação de dados em tabelas (DataFrames)
#  import pandas as pd

#  9️ pytest
#  pip install pytest
#  Framework de testes unitários e integração
#  import pytest

#   python-multipart
#  pip install python-multipart
#  Necessário para uploads em FastAPI (ex.: fotos de veículos)
#  from fastapi import File, UploadFile

#  1️1️ jinja2
#  pip install jinja2
#  Template engine para gerar HTML dinâmico (usado em FastAPI ou Flask)
#  from jinja2 import Template

#  1️2️ passlib
#  pip install passlib
#  Biblioteca para hash de passwords seguro
#  from passlib.context import CryptContext

#  1️3️ python-dateutil
#  pip install python-dateutil
#  Manipulação avançada de datas e horários
#  from dateutil import parser

#  1️4️ arrow
#  pip install arrow
#  Manipulação de datas e horários mais intuitiva que datetime
#  import arrow

#  1️5️ pillow
#  pip install pillow
#  Manipulação de imagens (redimensionar, criar miniaturas)
#  from PIL import Image

#  1️6️ aiofiles
#  pip install aiofiles
#  Ler/escrever ficheiros de forma assíncrona (FastAPI async)
#  import aiofiles

#  1️7️ python-jose
#  pip install python-jose
#  Gerar/verificar JWT tokens para autenticação
#  from jose import jwt

#  1️8️ bcrypt
#  pip install bcrypt
#  Hash seguro de passwords (alternativa ou complemento ao passlib)
#  import bcrypt

#  1️9️ loguru
#  pip install loguru
#  Logging avançado, mais simples que módulo logging nativo
#  from loguru import logger

#  2️0️ email-validator
#  pip install email-validator
#  Validação de emails (FastAPI, formulários)
#  from email_validator import validate_email, EmailNotValidError

