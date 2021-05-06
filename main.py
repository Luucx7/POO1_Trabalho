import cargoManager
import setorManager
import colaboradorManager

#
# O projeto utiliza POO para criar métodos que tornam mais legível a codificação,
# além da estruturação em objetos.
#
# Os comandos estão definidos na main, mas suas implementações estão definidas nas classes managers.
# A model contém as classes que serão base aos objetos do programa.
# Classes com GUIs não foram implementadas ainda.
#

#
# Chamada do comando colaborador
def comandoColaborador():
    if quantiaArgs == 1:  # Se apenas a entrada "colaborador" foi chamada, mostra os comandos disponíveis para a mesma
        colaboradorManager.listaComandos()
    # Senão, busca por algum comando válido
    elif entradaMultiAgrs[1] == "add":
        colaboradorManager.criaColaborador(entradaMultiAgrs)
    elif entradaMultiAgrs[1] == "listar":
        colaboradorManager.listarColaboradores()
    elif entradaMultiAgrs[1] == "remover":
        colaboradorManager.removerColaborador(entradaMultiAgrs)
    else:  # Mostra a lista se não encontrar um comando válido
        colaboradorManager.listaComandos()


def comandoSetor():  # Implementação similar ao comando colaborador, mas com o extra de "gerente"
    if quantiaArgs == 1:
        setorManager.listaComandos()
    elif entradaMultiAgrs[1] == "criar" and quantiaArgs > 2:
        setorManager.criaSetor(entradaMultiAgrs)
    elif entradaMultiAgrs[1] == "listar":
        setorManager.listaSetores()
    elif entradaMultiAgrs[1] == "remover" and quantiaArgs > 2:
        setorManager.removeSetor(entradaMultiAgrs)
    elif entradaMultiAgrs[1] == "gerente" and quantiaArgs > 2:
        setorManager.definirGerente(entradaMultiAgrs)
    else:
        setorManager.listaComandos()


def comandosCargo():  # Implementação similar a de colaborador.
    if quantiaArgs == 1:
        cargoManager.listaComandos()
    elif entradaMultiAgrs[1] == "criar" and quantiaArgs > 2:
        cargoManager.criaCargo(entradaMultiAgrs)
    elif entradaMultiAgrs[1] == "listar":
        cargoManager.listaCargos()
    elif entradaMultiAgrs[1] == "remover" and quantiaArgs > 2:
        cargoManager.removeCargo(entradaMultiAgrs)


def printComandos():  # Lista os comandos gerais do programa.
    print("Lista de comandos:")
    print("cargo - Gerencia cargos")
    print("setores - Gerencia setores")
    print("colaborador - Gerencia colaboradores")
    print(" ")


# Executa o programa indefinidamente, ou até o arquivo de comandos acabar.
while True:
    try:
        # Recebe a entrada em uma string única, transforma em lista de "strings" e conta a quantia de argymentos
        entrada = input()
        entradaMultiAgrs = entrada.split()
        quantiaArgs = len(entradaMultiAgrs)

        if quantiaArgs == 0:  # Se não há comando, imprime a lista de comandos
            printComandos()
        else:  # Caso haja algum comando, irá chamar os métodos que os implementam.
            if entradaMultiAgrs[0] == "cargo" or entradaMultiAgrs[0] == "c":
                comandosCargo()  # Comando cargo, pode ser abreviado com 'c'
            elif entradaMultiAgrs[0] == "setores" or entradaMultiAgrs[0] == "setor" or entradaMultiAgrs[0] == "s":
                comandoSetor()  # Comando setores, pode ser abreviado com 'setor' ou 's'
            elif entradaMultiAgrs[0] == "colaborador" or entradaMultiAgrs[0] == "colab" or entradaMultiAgrs[0] == "col":
                comandoColaborador()  # Comando colaborador, pode ser abreviado com 'colab' ou 'col'
            elif entradaMultiAgrs[0] == "ajuda" or entradaMultiAgrs[0] == "help":
                printComandos()  # 'comando de ajuda, imprime a lista de comandos base.
            else:  # Se inválido, imprime a lista base de comandos.
                printComandos()
    except EOFError:  # Fim do arquivo.
        break
