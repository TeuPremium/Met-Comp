from flask import Flask

app = Flask(__name__)   #variável responsável por receber os atributos da Classe Flask para utilização.

from app import routes  #Importanto os scripts para integração web