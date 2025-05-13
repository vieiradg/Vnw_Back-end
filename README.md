# 💸 Sispar Backend

Este é o backend da aplicação **Sispar**, desenvolvido com **Python + Flask** e **SQLAlchemy**, que permite o gerenciamento de reembolsos de colaboradores em empresas.

---

## 📂 Estrutura do Projeto

```
.
├── .gitattributes
├── .gitignore
├── LICENSE
├── README.md
├── config.py
├── package-lock.json
├── package.json
├── requirements.txt
├── run.py
├── node_modules/
│   └── .package-lock.json
└── src/
    ├── __init__.py
    ├── app.py
    ├── controller/
    │   ├── colaborador_controller.py
    │   └── reembolso_controller.py
    ├── model/
    │   ├── __init__.py
    │   ├── colaborador_model.py
    │   └── reembolso_model.py
    ├── security/
    │   └── security.py
    └── tests/
        ├── __init__.py
        └── test_app.py
```

---

## 🚀 Como executar o projeto

### 1. Clone o repositório

```bash
git clone https://github.com/vieiradg/Vnw_Back-end.git
cd sispar-backend
```

### 2. Crie e ative o ambiente virtual

```bash
No Windows:
python -m venv venv
source venv/Scripts/activate

No Linux/Mac:
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Na pasta config: use:
```
SQLALCHEMY_DATABASE_URI = 'sqlite:///db.sqlite' => para rodar o projeto local
SQLALCHEMY_DATABASE_URI = environ.get('URL_DATABASE_PROD') => para rodar o projeto com banco de dados do render
```

### 5. Execute o projeto

```bash
python run.py
```


📡 Principais Rotas

🔐 Autenticação
POST - /colaborador/login
Realiza o login do colaborador.

Exemplo de corpo:

```
{
  "email": "usuario@email.com",
  "senha": "123456"
}
```

👤 Colaboradores
GET - /colaborador/todos-colaboradores
Lista todos os colaboradores.

POST - /colaborador/cadastrar
Cadastra um novo colaborador.

Exemplo:
```
{
  "nome": "Diego Vieira",
  "email": "diego@email.com",
  "senha": "123456",
  "cargo": "Analista",
  "salario": 5000
}
```

PUT - /colaborador/atualizar/<id_colaborador>
Atualiza nome e cargo do colaborador com base no ID.

💵 Reembolsos
GET - /reembolso/todos-reembolsos
Retorna todos os reembolsos cadastrados.

POST - /reembolso/solicitar
Cria uma nova solicitação de reembolso.

Exemplo:
```
{
  "colaborador": "Diego Vieira",
  "empresa": "OpenAI",
  "num_prestacao": "12345",
  "descricao": "Viagem de trabalho",
  "tipo_reembolso": "Transporte",
  "centro_custo": "TI01",
  "ordem_interna": "OI998",
  "divisao": "TI",
  "pep": "PEP002",
  "moeda": "BRL",
  "distancia_km": 20,
  "valor_km": 2.5,
  "valor_faturado": 50.0,
  "despesa": 10.0,
  "id_colaborador": 1
}
```

📚 Documentação da API (Swagger)
Se estiver usando o Flasgger e configurou corretamente:

Acesse:
```
http://localhost:5000/apidocs
```


🛡️ Segurança
O sistema utiliza hash de senha com bcrypt para garantir a segurança dos dados de login dos colaboradores.


🛠 Tecnologias utilizadas
Python 3.13
Flask
SQLAlchemy
Flasgger (Swagger UI)
Banco local (SQLite apenas para testes).
Banco externo (PostgreSQL do Render) para produção.
Werkzeug (para hash de senha)


👨‍💻 Autor - Diego Vieira
💼 Desenvolvedor Backend em formação
📍 Rio de Janeiro, RJ








