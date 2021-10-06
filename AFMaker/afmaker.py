#imports
import argparse

'''
-------------- CLASE DO AUTOMATA --------------
Define como crear e as funcions que realiza o obxecto automata
'''

class Automata:

    """
    Constructor do Automata
    Recibe: todos os estados, os que son finales, os simbolos, e as transicions
    O estado inicial se determina como o primeiro da lista de estados
    """
    def __init__(self, allStates, finalState, symbols, transitions):

        self.allStates = allStates
        self.finalState = finalState
        self.symbols = symbols
        self.transitions = transitions

        #estado actual: ao principio vai ser o primeiro de todos os estados
        self.actualState = []
        self.actualState.append(self.allStates[0])
        #facemos a clausura do estado inicial para obter 
        self.__getEmptyStringStates()


    """
    Obten o seguinte estado a partir do estado actual e do input recibido
    """
    def __getNextState(self, input):
        _auxState = []
        
        #obtemos o indice do simbolo introducido
        index = self.symbols.index(input)

        #recorremos todos os estados actuales e obtemos o seguinte
        for state in self.actualState:

            nextState = self.transitions[state][index]
            _auxState += nextState

        #eliminamos duplicados e estados baleiros
        _auxState = list(dict.fromkeys(_auxState))

        if '' in _auxState:
            _auxState.remove('')

        #devolve os novos estados da maquina
        return _auxState


    """
    Obten a clausura do estado actual da maquina
    """
    def __getEmptyStringStates(self):

        while True:
            #obtemos os estados correspondentes a introducir a cadea baleira
            statesFromEmpty = self.__getNextState('Ɛ')

            cmp = self.actualState + statesFromEmpty

            #elimina os duplicados e os estados baleiros
            cmp = list(dict.fromkeys(cmp))
            if '' in cmp:   
                cmp.remove('')

            #os ordenamos para comparalos
            self.actualState.sort()
            cmp.sort()

            #se non se actualizou ningun estado, podemos parar
            if( self.actualState == cmp ):
                break
            else:
                self.actualState = cmp

    """
    Implementa a funcion de transicion.
    """
    def delta(self, input):

        #comprobamos que a entrada exista para a nosa maquina
        if input not in self.symbols:
            print("Error")
        
        else:
            if(input!='Ɛ'):
                #obtemos os estados seguintes e os actualizamos
                nextStates = self.__getNextState(input)
                self.actualState = nextStates

                #eliminamos duplicados
                self.actualState = list(dict.fromkeys(self.actualState))

                #obtemos a clausura dos novos estados
                self.__getEmptyStringStates()

        #imprimimos estado actual
        print("Estado actual: ", self.actualState)


    """
    Chama a funcion de transicion para cada caracter dunha cadea introducida
    """
    def run(self, string):
        for char in string:
            self.delta(char)

    """
    Comproba se o estado actual da maquina e un estado final
    """
    def checkFinalState(self):
        print("Estado final: ", self.actualState)
        for state in self.finalState:
            if state in self.actualState:
                print("La cadena está en un estado final")
                break

    """
    Imprime a informacion da maquina
    """
    def info(self):
        print("\nINFORMACION DEL AUTOMATA:\n")
        print("Estados: ", self.allStates)
        print("Estados finales: ", self.finalState)
        print("Simbolos aceptados: ", self.symbols)
        print("Transiciones: ", self.transitions)
        print("")

    """
    Resetea o estado da maquina
    """
    def resetState(self):
        #estado actual: ao principio vai ser o primeiro de todos os estados
        self.actualState = []
        self.actualState.append(self.allStates[0])
        #facemos a clausura do estado inicial para obter 
        self.__getEmptyStringStates()



'''
-------------- PARSEO DE FICHEIROS --------------
'''

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




'''
-------------- EXECUCION PRINCIPAL --------------
'''


def main(args):
    #obtemos os datos do automata do ficheiro
    allStates, finalState, symbols, transitions = getMachineInfo(args.file)

    #creamos o obxeto 
    maquina = Automata(allStates, finalState, symbols, transitions)

    #menu da aplicacion
    opt = True
    while opt:
        print("Bienvenido. Opciones:\n")
        print("1. Comprobar cadena")
        print("2. Informacion sobre el autómata")
        print("3. Salir")
        opt = input("Selecciona una opcion: ")
        if opt=="1":
            str = input("Introduce la cadena: ")
            maquina.resetState()
            maquina.run(str)
            maquina.checkFinalState()
            print("\n\n")

        elif opt=="2":
            maquina.info()

        elif opt=="3":
            opt = False
        else:
            print("Por favor, introduce una opcion valida\n\n")


#execucion principal
if __name__ == "__main__":

    #parseo de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help="Fichero de especificacion de la maquina")
    args = parser.parse_args();

    #chamamos ao main
    main(args)
