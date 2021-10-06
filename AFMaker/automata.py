
class Automata:


    def __init__(self, allStates, finalState, symbols, transitions):

        self.allStates = allStates
        self.finalState = finalState
        self.symbols = symbols
        self.transitions = transitions
        #estado actual: ao principio vai ser o primeiro de todos os estados
        self.actualState = []
        self.actualState.append(allStates[0])
        self.__getEmptyStringStates()

    def __getNextState(self, input):
        _auxState = []
        
        index = self.symbols.index(input)

        for state in self.actualState:

            if state == '' :
                nextState = ''
            else:
                nextState = self.transitions[state][index]
            _auxState += nextState

        _auxState = list(dict.fromkeys(_auxState))

        return _auxState

    def __getEmptyStringStates(self):

        while True:
            statesFromEmpty = self.__getNextState('Ɛ')

            cmp = self.actualState + statesFromEmpty
            cmp = list(dict.fromkeys(cmp))   
            self.actualState.sort()
            cmp.sort()

            if( self.actualState == cmp ):
                break;
            else:
                self.actualState = cmp

    def delta(self, input):

        if input not in self.symbols:
            print("Error")
        
        else:
            if(input!='Ɛ'):
                nextStates = self.__getNextState(input)
                self.actualState = nextStates
                self.__getEmptyStringStates()

                #eliminamos duplicados
                self.actualState = list(dict.fromkeys(self.actualState))
            
            else:
                statesFromEmpty = self.__getNextState('Ɛ')
                self.actualState += statesFromEmpty

    def run(self, string):
        for char in string:
            self.delta(char)
