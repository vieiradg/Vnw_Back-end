# 💸 SISPAR Backend

Sistema de gerenciamento de reembolsos desenvolvido com Python + Flask e SQLAlchemy.


## 📂 Estrutura do Projeto
```
sispar-backend/
├── .gitignore
├── config.py
├── requirements.txt
├── run.py
└── src/
├── app.py
├── controller/
│ ├── colaborador_controller.py
│ └── reembolso_controller.py
├── model/
│ ├── colaborador_model.py
│ └── reembolso_model.py
├── security/
│ └── security.py
└── tests/
└── test_app.py
```


## 🚀 Como Executar

1. Clone o repositório:
```
git clone https://github.com/vieiradg/Vnw_Back-end.git
cd sispar-backend
```

2. Configure o ambiente virtual:
```
python -m venv venv

# Windows:
venv/Scripts/activate

# Linux/Mac:
source venv/bin/activate
Instale as dependências:
```

3. Instale as dependências
```
pip install -r requirements.txt
Configure o banco em config.py:
```

4. No arquivo config, verifique:
```
SQLALCHEMY_DATABASE_URI=environ.get('URL_DATABASE_DEV')  #roda o projeto local
SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD')  #roda o projeto online
```

5. Execute:
```
python run.py
```

📡 Endpoints Principais

🔐 Autenticação
POST /colaborador/login
```
{
  "email": "usuario@email.com",
  "senha": "123456"
}
```

👤 Colaboradores
GET /colaborador/todos-colaboradores
PUT /colaborador/atualizar/<id_colaborador>
POST /colaborador/cadastrar
```
{
  "nome": "Novo Colaborador",
  "email": "email@empresa.com",
  "senha": "senha123",
  "cargo": "Cargo",
  "salario": 5000
}
```

💵 Reembolsos
GET /reembolso/todos-reembolsos
GET /reembolso/<num_prestacao>
POST /reembolso/solicitar
```
{
  "colaborador": "Nome",
  "empresa": "Empresa",
  "num_prestacao": 12345,
  "tipo_reembolso": "Transporte",
  "centro_custo": "TI",
  "moeda": "BRL",
  "valor_faturado": 150.50,
  "id_colaborador": 1
}
```

📚 Documentação
Acesse a API Docs em:
https://vnw-back-end.onrender.com/apidocs/#

🛡️ Segurança
Hash de senhas com bcrypt
Validação de dados em todas as rotas
CORS configurado

🛠 Tecnologias
Python 3.8+
Flask
SQLAlchemy
SQLite (desenvolvimento)
PostgreSQL (produção)
Flasgger (documentação)

FALTA IMPLEMENTAR 

- SQLALCHEMY_DATABASE_URI=environ.get('URL_DATABASE_DEV') | só está rodando com o link do SQL direto no arquivo
📌 Autorização com Tokens nas rotas
📌 Utilizar bibliotecas para Validações
📌 Relacionamentos no Banco de dados
📌 Funções auxiliare

👨‍💻 Autor - Diego Vieira
💼 Desenvolvedor Backend em formação
📍 Rio de Janeiro, RJ








