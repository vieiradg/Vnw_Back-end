# Armazenar as configurações do ambiente de desenvolvimento
from os import environ # Esse arquivo tem acesso as varíaveis de ambiente
from dotenv import load_dotenv # Carregamento das variáveis de ambiente nesse arquivo

load_dotenv()

class Config():
    #SQLALCHEMY_DATABASE_URI=environ.get('URL_DATABASE_DEV') #TA BUGADO, tem que pegar o link no .env e jogar aqui.
    SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') #roda online
    #SQLALCHEMY_DATABASE_URI="mysql://root:root@localhost:3306/sispar"
    SQLALCHEMY_TRACK_MODIFICATIONS=False 