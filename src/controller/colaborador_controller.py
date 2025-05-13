from flask import Blueprint, request, jsonify
from src.model.colaborador_model import Colaborador
from src.model import db
from src.security.security import hash_senha, checar_senha
from flasgger import swag_from

# request -> trabalha com as requisições. Pega o conteúdo da requisição
# jsonify -> Trabalha com as respostas. Converte um dado em Json

bp_colaborador = Blueprint('colaborador', __name__, url_prefix='/colaborador')


@bp_colaborador.route('/todos-colaboradores')
def pegar_dados_todos_colaboradores():
    
    colaboradores = db.session.execute(
        db.select(Colaborador)
    ).scalars().all()
    
    colaboradores = [ colaborador.all_data() for colaborador in colaboradores ]
    
    return jsonify(colaboradores), 200

@bp_colaborador.route('/cadastrar', methods=['POST'])
@swag_from ("../docs/colaboradores/cadastrar_colaborador.yml")
def cadastrar_novo_colaborador(): 
    
    dados_requisicao = request.get_json() 
    
    novo_colaborador = Colaborador(
        nome=dados_requisicao['nome'], # Pegue do json o valor relacionado a chave nome
        email=dados_requisicao['email'],
        senha= hash_senha(dados_requisicao['senha']) ,
        cargo=dados_requisicao['cargo'],
        salario=dados_requisicao['salario']
    )
    
#   INSERT INTO tb_colaborador (nome, email, senha, cargo, salario) VALUES (VALOR1,VALOR2,VALOR3,VALOR4,VALOR5)
    db.session.add(novo_colaborador)
    db.session.commit() 
    
    return jsonify( {'mensagem': 'Dado cadastrado com sucesso'}), 201

# Endereco/colaborador/atualizar/1
@bp_colaborador.route('/atualizar/<int:id_colaborador>', methods=['PUT'])
@swag_from("../docs/colaboradores/atualizar_colaborador.yml")
def atualizar_dados_do_colaborador(id_colaborador):
    dados_requisicao = request.get_json()
    
    # Busca o colaborador no banco de dados
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.id == id_colaborador)
    ).scalar()
    
    if not colaborador:
        return jsonify({'mensagem': 'Colaborador não encontrado'}), 404
    
    # Atualiza os campos se eles estiverem na requisição
    if 'nome' in dados_requisicao:
        colaborador.nome = dados_requisicao['nome']
    if 'cargo' in dados_requisicao:
        colaborador.cargo = dados_requisicao['cargo']
    
    # Confirma as alterações no banco de dados
    try:
        db.session.commit()
        return jsonify({'mensagem': 'Dados do colaborador atualizados com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'mensagem': f'Erro ao atualizar colaborador: {str(e)}'}), 500


@bp_colaborador.route('/login', methods=['POST'])
@swag_from("../docs/colaboradores/login.yml")
def login():
    
    dados_requisicao = request.get_json()
    
    email = dados_requisicao.get('email')
    senha = dados_requisicao.get('senha')
    
    if not email or not senha:
        return jsonify({'mensagem': 'Todos os dados precisam ser preenchidos'}), 400
    
    # SELECT * FROM [TABELA]
    colaborador = db.session.execute(
        db.select(Colaborador).where(Colaborador.email == email)
    ).scalar()
    
    if not colaborador:
        return jsonify({'mensagem': 'Usuario não encontrado'}), 404
    
    colaborador = colaborador.to_dict()
    
    if email == colaborador.get('email') and checar_senha(senha, colaborador.get('senha')):
        return jsonify({'mensagem': 'Login realizado com sucesso'}), 200
    else:
        return jsonify({'mensagem': 'Credenciais invalidas'}), 400
    
    