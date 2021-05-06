import colaboradorManager
import model
import setorManager

cargos = {}


def listaComandos():
    print("Lista de comandos:")
    print("listar - Lista todos os cargos")
    print("adicionar <nome> - Cria um novo cargo")
    print("remover <nome> - Remove um cargo")
    print(" ")


def criaCargo(entrada):  # Entrada = valores de entrada separados em coleção de strings
    cargo = model.Cargo(str(entrada[2]).lower())
    cargos[entrada[2]] = cargo
    print("Cargo criado!")


def listaCargos():
    print("Lista de cargos:\n")
    for cargo in cargos.values():
        print(cargo.nome, "\n")
    print("Fim da lista")


def removeCargo(entrada):  # Entrada = valores de entrada separados em coleção de strings
    valor = entrada[2]

    remover = True
    for colab in colaboradorManager.colaboradores.values():
        if colab.cargo.nome == valor:
            remover = False
            print("Ainda existem colaboradores neste cargo!")
            break

    if remover:
        cargo = cargos[valor]
        if isinstance(cargo, model.Gerente):
            print("Gerente não pode ser removido!")
        else:
            setorManager.setores.pop(valor, cargo)
            print("Cargo removido!")
