from flask import Blueprint, request, jsonify
from src.model.reembolso_model import Reembolso
from src.model.colaborador_model import Colaborador
from src.model import db
from flasgger import swag_from
from datetime import date

bp_reembolso = Blueprint('reembolso', __name__, url_prefix='/reembolso')

def reembolso_para_dict(reembolso):
    return {
        'id': reembolso.id,
        'colaborador': reembolso.colaborador,
        'empresa': reembolso.empresa,
        'num_prestacao': reembolso.num_prestacao,
        'descricao': reembolso.descricao,
        'data': reembolso.data.isoformat() if reembolso.data else None,
        'tipo_reembolso': reembolso.tipo_reembolso,
        'centro_custo': reembolso.centro_custo,
        'ordem_interna': reembolso.ordem_interna,
        'divisao': reembolso.divisao,
        'pep': reembolso.pep,
        'moeda': reembolso.moeda,
        'distancia_km': reembolso.distancia_km,
        'valor_km': reembolso.valor_km,
        'valor_faturado': float(reembolso.valor_faturado) if reembolso.valor_faturado else 0.0,
        'despesa': float(reembolso.despesa) if reembolso.despesa else None,
        'id_colaborador': reembolso.id_colaborador,
        'status': reembolso.status
    }

@bp_reembolso.route('/todos-reembolsos', methods=['GET'])
@swag_from("../docs/reembolsos/todos-reembolsos.yml")
def pegar_todos_reembolsos():
    try:
        reembolsos = Reembolso.query.order_by(Reembolso.data.desc()).all()
        return jsonify([reembolso_para_dict(r) for r in reembolsos]), 200
    except Exception as e:
        return jsonify({'erro': 'Falha ao buscar reembolsos', 'detalhes': str(e)}), 500

@bp_reembolso.route('/<int:num_prestacao>', methods=['GET'])
@swag_from("../docs/reembolsos/prestacao.yml")
def buscar_por_prestacao(num_prestacao):
    try:
        reembolso = Reembolso.query.filter_by(num_prestacao=num_prestacao).first()
        if not reembolso:
            return jsonify({'erro': f'Reembolso com prestação {num_prestacao} não encontrado'}), 404
        return jsonify(reembolso_para_dict(reembolso)), 200
    except Exception as e:
        return jsonify({'erro': str(e)}), 500

@bp_reembolso.route('/solicitar', methods=['POST'])
@swag_from("../docs/reembolsos/solicitar.yml")
def solicitar_reembolso():
    try:
        dados = request.get_json()

        # Validação de campos obrigatórios
        campos_obrigatorios = [
            'colaborador', 'empresa', 'num_prestacao',
            'tipo_reembolso', 'centro_custo', 'moeda',
            'valor_faturado', 'id_colaborador'
        ]
        
        faltantes = [campo for campo in campos_obrigatorios if campo not in dados]
        if faltantes:
            return jsonify({'erro': 'Campos obrigatórios faltando', 'campos': faltantes}), 400

        # Verifica se colaborador existe
        if not Colaborador.query.get(dados['id_colaborador']):
            return jsonify({'erro': 'Colaborador não encontrado'}), 404
        
        # Criação do reembolso
        novo_reembolso = Reembolso(
            colaborador=dados['colaborador'],
            empresa=dados['empresa'],
            num_prestacao=int(dados['num_prestacao']),
            descricao=dados.get('descricao', ''),
            data=date.today(),
            tipo_reembolso=dados['tipo_reembolso'],
            centro_custo=dados['centro_custo'],
            ordem_interna=dados.get('ordem_interna', ''),
            divisao=dados.get('divisao', ''),
            pep=dados.get('pep', ''),
            moeda=dados['moeda'],
            distancia_km=str(dados.get('distancia_km', '')),
            valor_km=str(dados.get('valor_km', '')),
            valor_faturado=float(dados['valor_faturado']),
            despesa=float(dados.get('despesa', 0)),
            id_colaborador=int(dados['id_colaborador']),
            status='Em análise'
        )

        db.session.add(novo_reembolso)
        db.session.commit()

        return jsonify({
            'mensagem': 'Reembolso criado com sucesso!',
            'id': novo_reembolso.id,
            'dados': reembolso_para_dict(novo_reembolso)
        }), 201

    except ValueError as e:
        db.session.rollback()
        return jsonify({'erro': 'Dados inválidos', 'detalhes': str(e)}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({'erro': 'Erro interno no servidor', 'detalhes': str(e)}), 500