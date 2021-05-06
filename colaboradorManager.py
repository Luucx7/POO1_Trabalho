import cargoManager
import model
import setorManager

colaboradores = {}  # Dicionário de colaboradores, sendo a chave o nome e o valor sua instância.


def criaColaborador(entrada):  # Função que cria colaborador, buscando os objetos das outras classes ou informando erro.
    try:
        nome = str(entrada[2])
        cargo = cargoManager.cargos[str(entrada[3])]
        setor = setorManager.setores[str(entrada[4])]
        colaborador = model.Colaborador(nome, cargo, setor)
        colaboradores[nome] = colaborador
        print("Colaborador adicionado!")
    except Exception:
        print("Erro ao adicionar colaborador.")


def removerColaborador(entrada):  # Remove um colaborador.
    nome = entrada[2]
    colaborador = colaboradores[nome]
    colaboradores.pop(nome, colaborador)
    print("Colaborador removido.")


def listarColaboradores():  # Lista todos os colaboradores e seus dados.
    print("Lista de colaboradores:")
    for colaborador in colaboradores.values():
        print("Nome:", colaborador.nome, "Setor:", colaborador.setor.nome, "Cargo:", colaborador.cargo.nome)
    print("Fim da lista.")


def listaComandos():  # Lista os comandos relacionados a colaborador.
    print("Lista de comandos de colaborador:")
    print("add <nome> <cargo> <setor>")
    print("remover <nome>")
    print("listar")
    print(" ")
