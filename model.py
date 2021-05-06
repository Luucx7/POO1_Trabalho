# -*- coding: utf-8 -*-

#
# Classe modelo que contém as classes utilizadas no projeto.
#

class Cargo:  # Classe cargo, que possui o atributo Nome
    def __init__(self, nome):
        self.nome = nome


class Gerente(Cargo):  # Classe gerente, instância de cargo, com nome estático.
    def __init__(self):
        super().__init__("Gerente")


class Setor:  # Classe setor, que possui os atributos nome e gerente
    gerente = ""

    def __init__(self, nome: str):
        self.nome = nome

    def setGerente(self, gerentesetor):
        self.gerente = gerentesetor


class Colaborador:  # Classe colaborador, com os atributos nome, cargo e setor.
    def __init__(self, nome, cargo, setor: Setor):
        self.nome = nome
        self.cargo = cargo
        self.setor = setor
