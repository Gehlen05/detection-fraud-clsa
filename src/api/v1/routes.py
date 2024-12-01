from flask import Blueprint, request, jsonify
from .logger import successmessage, errormessage
from .utils import carregar_modelo, check_is_json, check_is_empty, montar_dataframe, carregar_treshold
from .deteccao_fraude import deteccao_transacao_fraudulenta, objeto_saida_transacao


v1_blueprint = Blueprint('v1', __name__, url_prefix='/v1')


@v1_blueprint.before_request
def log_request_info():
    successmessage(f"{request.remote_addr} {request.method} {request.path}")


@v1_blueprint.route('/inteligencia-artificial/deteccao-fraude', methods=['GET'])
def get_deteccao_fraude():
    if not check_is_json(request):
        errormessage('A requisição precisa conter um JSON')
        return jsonify({'erro': 'A requisição não possui um JSON'}), 400
    if not check_is_empty(request):
        errormessage('Requisição vazia')
        return jsonify({'erro': 'A requisição não possui dados no JSON'}), 400
    try:
        df = montar_dataframe(request.json)
        modelo = carregar_modelo('deteccao-fraude')
        treshold = carregar_treshold('./src/api/v1/mapa/mapa-treshold', 'fraude', 'treshold_atual')
        df = deteccao_transacao_fraudulenta(modelo, df, treshold)
        lista_transacoes = objeto_saida_transacao(df)
        json_transacoes = [obj.__dict__ for obj in lista_transacoes]
        successmessage('Classificação realizada!')
        return jsonify(json_transacoes), 200

    except Exception as e:
        errormessage(f"Predição finalizada com erro! : {e}")
        return jsonify(f"erro: {e}"), 500
