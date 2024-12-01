from flask import Request
from .logger import successmessage, errormessage
import pickle
import pandas as pd
import configparser

def carregar_modelo(aplicacao_modelo):
    modelo_carregado = ''
    modelo = {'deteccao-fraude': 'modelo_regressao_v0112.pkl'}
    if modelo[aplicacao_modelo]:
        if aplicacao_modelo == 'deteccao-fraude':
            successmessage(f'Encontrado modelo: {modelo[aplicacao_modelo]}')
            with open(f'./src/api/v1/modelos/{modelo[aplicacao_modelo]}', 'rb') as arquivo:
                modelo_carregado = pickle.load(arquivo)
                successmessage(f'Modelo {aplicacao_modelo} carregado com sucesso')
    else:
        errormessage('Modelo de aplicacao não encontrado')

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
    successmessage('Inicianco criação dataframe')
    return pd.DataFrame(requisicao)

def carregar_treshold(nome_arquivo, seccao, treshold_atual):
    config = configparser.ConfigParser()
    config.read(nome_arquivo)
    if seccao in config and treshold_atual in config[seccao]:
        valor = float(config.get(seccao, treshold_atual))
        successmessage(f'Treshold = {valor}')
        return valor
