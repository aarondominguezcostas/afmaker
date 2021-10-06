
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
