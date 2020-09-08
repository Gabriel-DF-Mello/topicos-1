class Usuario:
    def __init__(self, matricula, nome, email, tipo):
        self.matricula = matricula
        self.nome = nome
        self.tipo = tipo
        self.email = email

    def __str__(self):
        return f"{self.matricula}:({self.nome}, {self.email})"