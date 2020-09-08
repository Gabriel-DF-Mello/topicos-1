class Ata:
    def __init__(self, data, hora, local, pauta):
        self.data = data
        self.hora = hora
        self.local = local
        self.pauta = pauta
        self.redator = None
        self.texto = ""
        self.validade = False
        self.integrantes = []