
"""
Neste ficheiro se definen as funciones encargadas de parsear o ficheiro de texto introducido
que conten a especificacion da maquina.
"""

def getMachineInfo(inputFile):
        #lee o arquivo e devolve o seu contido como unha lista de strings, eliminando /n
        allLines = inputFile.read().splitlines()

        #parseamos cada unha das liñas que conteñen informacion sobre os estados ou os simbolos
        allStates = __getSpecs(allLines[0])
        finalState = __getSpecs(allLines[1])
        symbols = __getSpecs(allLines[2])
        symbols.append('Ɛ')

        #eliminamos as liñas anteriores para quedarnos coas que conteñen informacion sobre as transicions
        allLines = allLines[4:]
        transitions = __getTransitions(allLines, allStates)
        return allStates, finalState, symbols, transitions

        inputFile.close()

"""
specString: string con formato "#num x y z"
devolve [x, y, z], num
"""

def __getSpecs(specString):
    list = specString.split(' ')
    #eliminamos o primer elemento da lista
    list.pop(0)

    #devolvemos a lista
    return list

"""
recibe unha lista con todas as transicions e os estados
devolve un diccionario que ten como claves os estados e como valores unha lista das transicions
"""

def __getTransitions(list, states):
    transitions = {}
    for i in range(len(list)):
        #obtenemos todos e os separamos por #
        nextStates = list[i].split('#')
        #o ultimo sobra, e o eliminamos
        nextStates.pop()
        afnList = []
        for state in nextStates:
            #separamos os estados cando son varios
            state=state.strip()
            afnList.append(state.split(' '))

        transitions[states[i]] = afnList

    return transitions
