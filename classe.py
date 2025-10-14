from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str, idade:int):
        self._nome = nome
        self._idade = idade

    @abstractmethod
    def emitir_som(self):
        pass

    def descrever(self):
        return f'{self._nome} tem {self._idade} anos.'
        
class IVoador (ABC):
    @abstractmethod
    def voar(self):
        pass

class INadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Mamifero(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return '...' 

class Ave(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return '@@@'

class Leao(Mamifero):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "Rugido"

class Pinguim(Ave, INadador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)

    def emitir_som(self):
        return "Piu"
    
    def nadar(self):
        return f"{self._nome} está nadando."

class Aguia(Ave, IVoador):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        
    def emitir_som(self):
        return "Grito agudo"
    
    def voar(self):
        return f"{self._nome} está voando alto."

def interagir_no_zoologico(animais):
    for animal in animais:
        print(animal.descrever())
        animal.emitir_som()

        if isinstance(animal, IVoador):
            animal.voar()

        if isinstance(animal, INadador):
            animal.nadar()

#------------------------------------------------------
if __name__ == '__main__':
    leao = Leao("Simba", 5)
    pinguim = Pinguim("Tux", 3)
    aguia = Aguia("Altair", 4)

    animais = [leao, pinguim, aguia]
    interagir_no_zoologico(animais)