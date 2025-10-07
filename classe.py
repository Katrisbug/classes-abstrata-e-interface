from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome:str, idade:int):
        self.__nome = nome
        self.__idade = idade

        @abstractmethod
        def emitir_som(self):
            pass

        def descrever():
            return f'{self.__nome} tem {self.__idade} anos.'
        
class IVoador (ABC):
    @abstractmethod
    def voar(self):
        pass

class INadador(ABC):
    @abstractmethod
    def nadar(self):
        pass

class Mamifero(Animal):
    pass 

class Ave(Animal):
    pass

class Leao(Mamifero):
    pass

class Pinguim(Ave, INadador):
    pass

class Aguia(Ave, IVoador):
    pass
