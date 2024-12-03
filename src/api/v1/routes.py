from flask import Blueprint, request, jsonify
from .logger import success_message, error_message
from .utils import carregar_modelo, check_is_json, check_is_empty, montar_dataframe
from .deteccao_fraude import deteccao_transacao_fraudulenta, objeto_saida_transacao
from ..validators import validar_json
from ..validators.deteccao_fraude_schema import DeteccaoFraudeSchema

v1_blueprint = Blueprint('v1', __name__, url_prefix='/v1')


@v1_blueprint.before_request
def log_request_info():
    success_message(f"{request.remote_addr} {request.method} {request.path}")


@v1_blueprint.route('/inteligencia-artificial/deteccao-fraude', methods=['POST'])
def post_deteccao_fraude():
    if not check_is_json(request):
        error_message('A requisição precisa conter um JSON')
        return jsonify({'error': 'A requisição não possui um JSON'}), 400
    if not check_is_empty(request):
        error_message('Requisição vazia')
        return jsonify({'error': 'A requisição não possui dados no JSON'}), 400

    try:
        schema = DeteccaoFraudeSchema(many=True)
        valid_data, errors = validar_json(request, schema)
        if errors:
            return jsonify({"error": str(errors)}), 400

        df = montar_dataframe(valid_data)
        modelo = carregar_modelo('deteccao-fraude')
        treshold = 0.496
        df = deteccao_transacao_fraudulenta(modelo, df, treshold)
        lista_transacoes = objeto_saida_transacao(df)
        json_transacoes = [obj.__dict__ for obj in lista_transacoes]
        success_message('Classificação realizada!')
        return jsonify(json_transacoes), 200

    except Exception as e:
        error_message(f"Predição finalizada com erro! : {e}")
        return jsonify({"error": str(e)}), 500
