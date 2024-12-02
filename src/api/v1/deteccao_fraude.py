from .classes import Transacao
from .logger import success_message


def deteccao_transacao_fraudulenta(modelo, df, treshold):
    """
    Função para realizar a detecção de transações fraudulentas.
    Parâmetros:
        modelo : Artefato treinado para calcular as probabilidades de fraude.
        df: DataFrame contendo os dados das transações a serem analisadas.
        treshold (float): Limite de probabilidade para classificar uma transação como fraudulenta.
    Retorno:
        pandas.DataFrame: DataFrame atualizado com duas colunas adicionais:
            - 'probabilidade': Probabilidade de a transação ser fraudulenta, calculada pelo modelo.
            - 'fraude': Classificação da transação ('1' para fraudulenta e '0' para não fraudulenta).
    """
    success_message('Inicianco predição pentavalente')
    df = df.fillna(0)
    resultados = df.iloc[:, 1:].apply(lambda linha: _definir_fraude(linha, modelo, treshold), axis=1)
    df['probabilidade'], df['fraude'] = zip(*resultados)
    return df

def _definir_fraude(linha, modelo, treshold):
    """
       Função auxiliar para definir se uma transação é fraudulenta com base no modelo preditivo.
       Parâmetros:
           linha (pandas.Series): Uma linha do DataFrame contendo os dados da transação (características).
            modelo : Artefato treinado para calcular as probabilidades de fraude.
            treshold (float): Limite de probabilidade para classificar uma transação como fraudulenta.
       Retorno:
           tuple: Uma tupla contendo:
               - probabilidade (float): Probabilidade calculada de a transação ser fraudulenta.
               - fraude (str): Classificação da transação ('1' para fraudulenta, '0' para não fraudulenta).
       """
    vetor = linha.values.reshape(1, -1)
    probabilidade = modelo.predict_proba(vetor)[:, 1]
    fraude = '1' if probabilidade[0] > treshold else '0'
    return  probabilidade[0], fraude


def _criar_transacao(linha):
    """
    Função auxiliar para criar um objeto Transacao a partir de uma linha do DataFrame.
    Parâmetros:
        linha: Uma linha do DataFrame contendo as informações da transação.
                   Deve incluir as colunas:
                   - 'id_transacao': Identificador único da transação.
                   - 'probabilidade': Probabilidade de fraude associada à transação.
                   - 'fraude': Classificação da transação ('1' para fraudulenta, '0' para não fraudulenta).
    Retorno:
        Transacao: Objeto Transacao criado a partir dos dados fornecidos na linha.
    """
    return Transacao(id_transacao=linha['id_transacao'],
                     probabilidade=linha['probabilidade'], fraude=linha['fraude'])

def objeto_saida_transacao(df):
    """
        Função para criar uma lista de objetos Transacao a partir de um DataFrame.
        Parâmetros:
            df (pandas.DataFrame): DataFrame contendo os dados das transações.
                                   Deve incluir as colunas:
                                   - 'id_transacao': Identificador único da transação.
                                   - 'probabilidade': Probabilidade de fraude associada à transação.
                                   - 'fraude': Classificação da transação ('1' para fraudulenta, '0' para não fraudulenta).
        Retorno:
            pandas.Series: Série contendo objetos Transacao, um para cada linha do DataFrame.
        """
    success_message('Criando lista de objetos transações')
    return df.apply(_criar_transacao, axis=1)