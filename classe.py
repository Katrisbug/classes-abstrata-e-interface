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
    def emitir_som(self):
        return "Rugido"

class Pinguim(Ave, INadador):
    def emitir_som(self):
        return "Piu"
    
    def nadar(self):
        return f"{self.__nome} está nadando."

class Aguia(Ave, IVoador):
    def emitir_som(self):
        return "Grito agudo"
    
    def voar(self):
        return f"{self.__nome} está voando alto."
