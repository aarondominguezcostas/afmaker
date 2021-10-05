


class Automata:


    def __init__(self, allStates, finalState, symbols, transitions):

        self.allStates = allStates
        self.finalState = finalState
        self.symbols = symbols
        self.transitions = transitions
        #estado actual: ao principio vai ser o primeiro de todos os estados
        self.actualState = allStates[0]

    def getNextState(self, input):
        index = self.symbols.index(input)
        return self.transitions[self.actualState][index]
