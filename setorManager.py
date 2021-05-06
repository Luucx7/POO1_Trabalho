import colaboradorManager
import model

setores = {}


def listaComandos():
    print("Lista de comandos:")
    print("listar - Lista todos os setores")
    print("adicionar <nome> - Cria um novo setor")
    print("remover <nome> - Remove um setor")
    print("gerente <setor> <colaborador> - Define o gerente de um setor")
    print(" ")


def definirGerente(entrada):
    setor = setores[entrada[1]]
    colaborador = colaboradorManager.colaboradores[entrada[2]]
    setor.gerente = colaborador


def removeSetor(entrada):
    podeRemover = True
    for colaborador in colaboradorManager.colaboradores:
        if colaborador.setor.nome == entrada[2]:
            podeRemover = False
            print("Ainda existem colaboradores neste setor!")
            break

    if podeRemover:
        setor = setores[entrada[2]]
        setores.pop(entrada[2], setor)
        print("Setor removido!")


def listaSetores():
    print("Lista de setores:\n")
    for setor in setores.values():
        print(setor.nome, "\n")
    print("Fim da lista")


def criaSetor(entrada):
    setor = model.Setor(entrada[2])
    setores[entrada[2]] = setor
    print("Setor criado!")
