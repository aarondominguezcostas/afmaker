#imports
import argparse
import fileparser

def main(args):
    print(fileparser.getMachineInfo(args.file))


#execucion principal
if __name__ == "__main__":

    #parseo de argumentos
    parser = argparse.ArgumentParser()
    parser.add_argument('file', type=argparse.FileType('r'), help="Fichero de especificacion de la maquina")
    args = parser.parse_args();

    main(args)
