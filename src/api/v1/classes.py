
class Transacao:
    def __init__(self,id_transacao, probabilidade, fraude):
        self.servico = 'Fraude'
        self.id_transacao = id_transacao
        self.probabilidade = probabilidade
        self.fraude = fraude

    def to_dict(self):
        return {
            "servico": self.servico,
            "id_transacao": self.id_transacao,
            "probabilidade": self.probabilidade,
            "fraude": self.fraude
        }
