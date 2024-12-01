from .classes import Transacao
from .logger import successmessage


def deteccao_transacao_fraudulenta(modelo, df, treshold):
    successmessage('Inicianco predição pentavalente')
    df = df.fillna(0)
    resultados = df.iloc[:, 1:].apply(lambda linha: _definir_fraude(linha, modelo, treshold), axis=1)
    df['probabilidade'], df['fraude'] = zip(*resultados)
    return df

def _definir_fraude(linha, modelo, treshold):
    vetor = linha.values.reshape(1, -1)
    probabilidade = modelo.predict_proba(vetor)[:, 1]
    fraude = '1' if probabilidade > treshold else '0'
    return  probabilidade[0], fraude


def _criar_transacao(linha):
    return Transacao(id_transacao=linha['id_transacao'],
                     probabilidade=linha['probabilidade'], fraude=linha['fraude'])

def objeto_saida_transacao(df):
    successmessage('Criando lista de objetos pentavalente')
    return df.apply(_criar_transacao, axis=1)