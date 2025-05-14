from src.model import db #traz a instancia do SQLALchemy para este arquivo
from sqlalchemy.schema import Column # Traz o recurso para o ORM entender que o atributo será uma coluna na tabela
from sqlalchemy.types import String, DECIMAL, Integer, Boolean # Importando os tipos de dados que as colunas vão aceitar


class Colaborador(db.Model):
    
#   id INT AUTO_INCREMENT PRIMARY KEY
    id = Column(Integer, primary_key=True, autoincrement=True)
#   nome VARCHAR(100)
    nome = Column(String(100))
    email = Column(String(100))
    senha = Column(String(150))
    cargo = Column(String(100))
    salario = Column(DECIMAL(10,2))
    ativo = Column(Boolean, default=True)

    def __init__(self, nome, email, senha, cargo, salario, ativo=True):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cargo = cargo
        self.salario = salario
        self.ativo = ativo

    def to_dict(self) -> dict:
        return {
            'email': self.email,
            'senha': self.senha,
            'ativo': self.ativo
        }
        
    def all_data(self) -> dict:
        return {
            'id': self.id,
            'nome': self.nome,
            'cargo': self.cargo,
            'salario': self.salario,
            'email': self.email,
            'ativo': self.ativo
        }