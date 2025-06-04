import copy
import time

mapas = []

mapa1 = {
    "grafo" : {
        "1": ["2"],
        "2": ["1", "3"],
        "3": ["2", "4"],
        "4": ["3", "5"],
        "5": ["4", "6"],
        "6": ["5"]
    },
    "listaMonstros" : [],
    "listaTesouros" : ["4"],
    "objetivo" : "6"
}

mapa2 = {
    "grafo" : {
        "1": ["2"],
        "2": ["1", "3"],
        "3": ["2", "4", "10"],
        "4": ["3", "5"],
        "5": ["4", "6"],
        "6": ["5", "7"],
        "7": ["6", "8", "11"],
        "8": ["7", "9"],
        "9": ["8"],
        "10": ["3", "12"],
        "11": ["7", "16"],
        "12": ["10", "13"],
        "13": ["12", "14"],
        "14": ["13", "15"],
        "15": ["14", "16"],
        "16": ["11", "15"]
    },
    "listaMonstros" : ["5"],
    "listaTesouros" : ["6", "14"],
    "objetivo" : "9"
}

mapa3 = {
    "grafo" : {
        "1": ["2"],
        "2": ["1", "3"],
        "3": ["2", "4", "10", "17"],
        "4": ["3", "5"],
        "5": ["4", "6"],
        "6": ["5", "7"],
        "7": ["6", "8", "11", "18"],
        "8": ["7", "9"],
        "9": ["8"],
        "10": ["3", "12"],
        "11": ["7", "16"],
        "12": ["10", "13"],
        "13": ["12", "14"],
        "14": ["13", "15"],
        "15": ["14", "16"],
        "16": ["11", "15"],
        "17": ["3", "19"],
        "18": ["7", "23"],
        "19": ["17", "20"],
        "20": ["19", "21"],
        "21": ["20", "22"],
        "22": ["21", "23"],
        "23": ["18", "22"]
    },
    "listaMonstros" : ["5", "20"],
    "listaTesouros" : ["6", "14", "21"],
    "objetivo" : "9"
}

mapa4 = {
    "grafo" : {
        "1": ["2"],
        "2": ["1", "3", "4", "5"],
        "3": ["2", "6"],
        "4": ["2", "6", "7", "8"],
        "5": ["2", "8"],
        "6": ["3", "4", "9"],
        "7": ["4", "9", "10", "11"],
        "8": ["4", "5", "10"],
        "9": ["6", "7"],
        "10": ["7", "8"],
        "11": ["7"]
    },
    "listaMonstros" : ["6"],
    "listaTesouros" : ["3", "10", "11"],
    "objetivo" : "4"
}

mapa5 = {
    "grafo" : {
        "1" : ["2"],
        "2" : ["1", "3", "4"],
        "3" : ["2", "5"],
        "4" : ["2", "6", "38"],
        "5" : ["3", "7"],
        "6" : ["4", "8"],
        "7" : ["5", "9"],
        "8" : ["6", "10"],
        "9" : ["7", "11"],
        "10" : ["8", "12"],
        "11" : ["9", "13", "14", "15", "16"],
        "12" : ["10", "17", "18", "19", "20"],
        "13" : ["11", "21"],
        "14" : ["11", "23", "24", "38"],
        "15" : ["11"],
        "16" : ["11"],
        "17" : ["12", "25"],
        "18" : ["12"],
        "19" : ["12", "26", "27", "38"],
        "20" : ["12"],
        "21" : ["13", "28", "29"],
        "22" : ["33", "38"],
        "23" : ["14", "32"],
        "24" : ["14", "33"],
        "25" : ["17", "34", "35"],
        "26" : ["19", "32"],
        "27" : ["19", "33"],
        "28" : ["21"],
        "29" : ["21", "36"],
        "30" : ["32", "38"],
        "31" : ["33"],
        "32" : ["23", "26", "30", "37"],
        "33" : ["22", "24", "27", "31"],
        "34" : ["25", "36"],
        "35" : ["25"],
        "36" : ["29", "34"],
        "37" : ["32"],
        "38" : ["4", "19", "22", "30"]
    },
    "listaMonstros" : ["3", "15", "18", "25", "26", "28"],
    "listaTesouros" : ["16", "20", "31", "35", "37"],
    "objetivo" : "38"
}

mapa6 = {
    "grafo" : {
        "1": ["2"],
        "2": ["1", "3", "4", "5"],
        "3": ["2"],
        "5": ["2"],
        "4": ["2", "6", "7"],
        "6": ["4", "8"],
        "7": ["4", "9"],
        "8": ["6", "10", "11", "12"],
        "9": ["7", "13"],
        "11": ["8"],
        "10": ["8", "14"],
        "12": ["8", "15"],
        "13": ["9", "16", "17", "18", "19"],
        "14": ["10", "20"],
        "15": ["12", "21"],
        "16": ["13", "22"],
        "17": ["13", "23", "24", "25", "26"],
        "19": ["13"],
        "18": ["13", "27"],
        "20": ["14", "28", "29"],
        "21": ["15", "27", "31"],
        "22": ["16"],
        "25": ["17"],
        "24": ["17", "32", "33"],
        "23": ["17"],
        "26": ["17", "34", "35"],
        "27": ["18", "21"],
        "28": ["20", "29", "36"],
        "29": ["20", "28", "30", "36"],
        "30": ["29", "36"],
        "31": ["21", "37", "38"],
        "33": ["24"],
        "32": ["24"],
        "34": ["26"],
        "35": ["26", "39"],
        "36": ["28", "29", "30", "40"],
        "37": ["31"],
        "38": ["31", "39", "41"],
        "39": ["35", "38"],
        "40": ["36", "42", "43", "49"],
        "41": ["38", "44"],
        "42": ["40", "45"],
        "43": ["40", "46", "47"],
        "44": ["41", "48"],
        "45": ["42", "49"],
        "46": ["43", "49"],
        "47": ["43"],
        "48": ["44", "49"],
        "49": ["40", "45", "46", "48"]
    },
    "listaMonstros" : ["3", "9", "14", "23", "29", "32", "34", "37", "42"],
    "listaTesouros" : ["5", "11", "19", "25", "33", "47"],
    "objetivo" : "48"
}

mapas.append(mapa1)
mapas.append(mapa2)
mapas.append(mapa3)
mapas.append(mapa4)
mapas.append(mapa5)
mapas.append(mapa6)

mapaAtualIndice = 0
tesouroOn = False
monstroOn = False
while True:
    mapaEscolhido = input("Escolha um mapa (1 a 6): ")
    if mapaEscolhido.isdigit():
        mapaAtualIndice = int(mapaEscolhido)
        if (1 <= mapaAtualIndice <= 6):
            break
        else:
            print("Mapa fora do intervalo. Tente novamente.")
    else:
        print("Entrada inválida. Digite apenas números.")

while True:
    tesouro = input("Ativar Tesouros? (Sim - 1 Nao - 2): ")
    if tesouro.isdigit():
        escolhaTesouro = int(tesouro)
        if (escolhaTesouro == 1):
            tesouroOn = True
            break
        elif (escolhaTesouro == 2):
            tesouroOn = False
            break
        else:
            print("Entrada fora do intervalo. Tente novamente.")
    else:
        print("Entrada inválida. Digite apenas números.")

while True:
    monstro = input("Ativar Monstros? (Sim - 1 Nao - 2): ")
    if monstro.isdigit():
        escolhaMonstroo = int(monstro)
        if (escolhaMonstroo == 1):
            monstroOn = True
            break
        elif (escolhaMonstroo == 2):
            monstroOn = False
            break
        else:
            print("Entrada fora do intervalo. Tente novamente.")
    else:
        print("Entrada inválida. Digite apenas números.")

tempoInicial = time.time()

mapaAtual = mapas[mapaAtualIndice-1]
grafo = mapaAtual["grafo"]
listaMonstros = mapaAtual["listaMonstros"]
listaTesouros = mapaAtual["listaTesouros"]
objetivo = mapaAtual["objetivo"]

loop = []
loopRetorno = []
retornando = False

noInicial = {
    "estado" : "1",
    "pai" : None,
    "vida" : 3,
    "tesouro" : []
}

# funcao para calcular o tesouro
# considerando o tesouro do pai
def ColetarTesouro(estado, no):
    tesourosColetados = []
    tesourosColetados = copy.deepcopy(no["tesouro"])
    # copia array para alterar a lista sem afetar a lista pai

    if estado in listaTesouros:
        # evita duplicar os estados na lista
        if (estado not in tesourosColetados):
            tesourosColetados.append(estado)

    return tesourosColetados

def Objetivo(no):
    if (tesouroOn):
        return (no["estado"] == objetivo and len(no["tesouro"]) == len(listaTesouros))
    return (no["estado"] == objetivo)

def ValidarEstado(estado):
    estadosValidos = 0
    estadosRetornoValidos = 0
    global retornando

    if (monstroOn and estado in listaMonstros):
        return False

    # O algoritmo permite o retorno como caso especial
    # Um controle de loop normal e utilizado
    # A nao ser que o no atual nao tenha mais caminho
    if (retornando):
        # evita voltar para o caminho sem saida
        if (estado in loopRetorno):
            return False

        # "visualiza" os caminhos futuros
        # se houver caminhos que o loop principal nao mapeou
        # entao nao vai ser necessario "retornar" no futuro
        estadosRetorno = grafo[estado]
        for estadoRetorno in estadosRetorno:
            if (monstroOn and estadoRetorno in listaMonstros):
                    return False

            if (estadoRetorno not in loop):
                estadosValidos += 1

            if (estadoRetorno not in loopRetorno):
                estadosRetornoValidos += 1

        if (estadosValidos == 0 and estadosRetornoValidos == 0):
            return False

        if (estadosValidos >= 1):
            retornando = False
            loopRetorno.clear()
            # a lista e limpa
            # permitindo um retorno pelo mesmo caminho no futuro
    else:
        if (estado in loop):
            return False

    return True

def ChecarPossibilidades(estados):
    estadosValidos = 0
    for estado in estados:
        if (ValidarEstado(estado)):
            estadosValidos += 1

    return estadosValidos

def Expandir(no):
    estados = grafo[no["estado"]]
    estadosValidos = []
    global retornando

    if (not retornando):
        # checa os caminhos disponiveis
        # se nao houver, ele deve retornar
        if (ChecarPossibilidades(estados) == 0):
            retornando = True
            loopRetorno.append(no["estado"])

            # se ele esta retornando, ele deve ir direto para o no pai
            # evita que ele va para um no ja acessado
            novoNo = {
                "estado" : no["pai"]["estado"],
                "pai" : no,
                "vida" : 3,
                "tesouro" : ColetarTesouro(no["pai"]["estado"], no)
            }

            estadosRetorno = grafo[no["pai"]["estado"]]

            estadosRetornoValidos = 0
            for estadoRetorno in estadosRetorno:
                if (monstroOn):
                    if (estadoRetorno not in loop and estadoRetorno not in listaMonstros):
                        estadosRetornoValidos += 1
                elif (estadoRetorno not in loop):
                    estadosRetornoValidos += 1

            if (estadosRetornoValidos >= 1):
                retornando = False
                loopRetorno.clear()

            estadosValidos.append(novoNo)
            return estadosValidos

    for estado in estados:
        if (ValidarEstado(estado)):
            # monta as folhas
            novoNo = {
                "estado" : estado,
                "pai" : no,
                "vida" : 3,
                "tesouro" : ColetarTesouro(estado, no)
            }
            estadosValidos.append(novoNo)
    return estadosValidos

noAtual = noInicial
pilha = []

repeticoes = 0
sucesso = True
while not Objetivo(noAtual):
    #if (repeticoes >= 100):
    #    print("caralho")
    #print(noAtual["estado"])

    if (retornando):
        loopRetorno.append(noAtual["estado"])
    else:
        loop.append(noAtual["estado"])

    nos = Expandir(noAtual)

    for no in nos:
        pilha.append(no)

    # usando pop() para pegar o ultimo elemento na lista
    # devido a busca por profundidade

    if (len(pilha) > 0):
        noAtual = pilha.pop()
        repeticoes += 1
    else:
        print("Caminho nao encontrado!")
        sucesso = False
        break

if (sucesso):
    # calculo do tempo de execucao
    tempoFinal = time.time()
    tempoExecucao = tempoFinal - tempoInicial

    print(f"Tempo de execução: {tempoExecucao:.6f} segundos")
    print(f"Repeticoes: {repeticoes}")

    monstros = ""
    caminho = ""
    print("Caminho Encontrado: ")
    while noAtual != None:
        caminho += noAtual["estado"] + " <- "
        if (noAtual["estado"] in listaMonstros):
            monstros += noAtual["estado"] + " "
        noAtual = noAtual["pai"]
    caminho = caminho.rstrip(" <- ")
    print("Caminho: " + caminho)
    print("Monstros: " + monstros)