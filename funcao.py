from classe import *

def interagir_no_zoologico(animais: list):
    for animal in animais:
        print(animal.descrever())
        print(animal.emitir_som())
        if isinstance(animal, IVoador):
            print(animal.voar())
        if isinstance(animal, INadador):
            print(animal.nadar())
        print()

#------------------------------------------------------
if __name__ == '__main__':
    leao = Leao("Simba", 5)
    pinguim = Pinguim("Tux", 3)
    aguia = Aguia("Altair", 4)
    animais = [leao, pinguim, aguia]
    interagir_no_zoologico(animais)