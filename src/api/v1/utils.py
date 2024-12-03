from flask import Request
from .logger import success_message, error_message
import pickle
import pandas as pd
import configparser

def carregar_modelo(aplicacao_modelo):
    modelo_carregado = ''
    modelo = {'deteccao-fraude': 'modelo_regressao_v0112.pkl'}
    if modelo[aplicacao_modelo]:
        if aplicacao_modelo == 'deteccao-fraude':
            success_message(f'Encontrado modelo: {modelo[aplicacao_modelo]}')
            with open(f'./src/api/v1/modelos/{modelo[aplicacao_modelo]}', 'rb') as arquivo:
                modelo_carregado = pickle.load(arquivo)
                success_message(f'Modelo {aplicacao_modelo} carregado com sucesso')
    else:
        error_message('Modelo de aplicacao não encontrado')

    return modelo_carregado


def check_is_json(request: Request) -> bool:
    if not request.is_json:
        return False
    else:
        return True


def check_is_empty(request: Request) -> bool:
    data = request.get_json()
    if not data:
        return False
    else:
        return True

def montar_dataframe(requisicao):
    success_message('Inicianco criação dataframe')
    return pd.DataFrame(requisicao)

def carregar_treshold(nome_arquivo, seccao, treshold_atual):
    config = configparser.ConfigParser()
    config.read(nome_arquivo)
    if seccao in config and treshold_atual in config[seccao]:
        valor = float(config.get(seccao, treshold_atual))
        success_message(f'Treshold = {valor}')
        return valor
