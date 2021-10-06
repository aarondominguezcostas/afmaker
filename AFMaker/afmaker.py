#imports
import argparse
import fileparser
from automata import Automata

def main(args):
    #print(fileparser.getMachineInfo(args.file))
    allStates, finalState, symbols, transitions = fileparser.getMachineInfo(args.file)

    opt = True
    while opt:
        print("Bienvenido. Opciones:\n")
        print("1. Comprobar cadena")
        print("2. Salir")
        opt = input("Selecciona una opcion: ")
        if opt=="1":
            maquina = Automata(allStates, finalState, symbols, transitions)
            str = input("Introduce la cadena: ")
            maquina.run(str)
            print(maquina.actualState)
            print("\n\n")
        elif opt=="2":
            opt = False
        else:
            print("Por favor, introduce una opcion valida\n")


#execucion principal
if __name__ == "__main__":

    #parseo de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help="Fichero de especificacion de la maquina")
    args = parser.parse_args();

    main(args)
