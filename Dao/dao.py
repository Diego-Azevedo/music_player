import random
import pickle
from abc import ABC, abstractmethod

class DAO(ABC):
    @abstractmethod
    def __init__(self, datasource=''):
        self.__datasource = datasource
        self.__cache = {}
        try:
            self.__load()
        except FileNotFoundError:
            self.__dump()

    def __dump(self):
        pickle.dump(self.__cache, open(self.__datasource, 'wb'))

    def __load(self):
        self.__cache = pickle.load(open(self.__datasource,'rb'))

    def add(self, key, obj):
        self.__cache[key] = obj
        self.__dump() 

    def update(self, key, obj):
        try:
            if(self.__cache[key] != None):
                self.__cache[key] = obj 
                self.__dump()
        except KeyError:
            print("ERRO AO REALIZAR O UPDATE")

    def get_random(self):
        variavel = self.__cache['2']
        return variavel
       
    def remove(self, key):
        try:
            self.__cache.pop(key)
            self.__dump()
        except KeyError:
            print("NÃO FOI POSSÍVEL REMOVER")

    def get_all(self):
        return self.__cache.values()
