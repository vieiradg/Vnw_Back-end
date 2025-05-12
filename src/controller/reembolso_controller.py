# Tarefa -> Implementação

# Rota de visualização de todos os reembolsos -> GET
# Solicitação de reembolsos -> POST

# Para enviar multiplos dados para o BD, utilize: db.session.bulk_save_objects(lista[instancias])

from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model import db

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

# Rota para visualizar todos os reembolsos
@bp_reembolso.route('/todos-reembolsos', methods=['GET'])
def pegar_todos_reembolsos():
    reembolsos = db.session.execute(
        db.select(Reembolso)
    ).scalars().all()

    # Transformando os dados em formato de dicionário
    reembolsos = [reembolso.all_data() for reembolso in reembolsos]
    
    return jsonify(reembolsos), 200

# Rota para solicitar reembolso
@bp_reembolso.route('/solicitar', methods=['POST'])
def solicitar_reembolso():
    dados_requisicao = request.get_json()

    novo_reembolso = Reembolso(
        colaborador=dados_requisicao['colaborador'],
        empresa=dados_requisicao['empresa'],
        num_prestacao=dados_requisicao['num_prestacao'],
        descricao=dados_requisicao['descricao'],
        tipo_reembolso=dados_requisicao['tipo_reembolso'],
        centro_custo=dados_requisicao['centro_custo'],
        ordem_interna=dados_requisicao.get('ordem_interna', ''),
        divisao=dados_requisicao.get('divisao', ''),
        pep=dados_requisicao.get('pep', ''),
        moeda=dados_requisicao['moeda'],
        distancia_km=dados_requisicao.get('distancia_km', ''),
        valor_km=dados_requisicao.get('valor_km', ''),
        valor_faturado=dados_requisicao['valor_faturado'],
        despesa=dados_requisicao.get('despesa', 0),
        id_colaborador=dados_requisicao['id_colaborador']
    )
    
    db.session.add(novo_reembolso)
    db.session.commit()

    return jsonify({'mensagem': 'Reembolso solicitado com sucesso'}), 201
