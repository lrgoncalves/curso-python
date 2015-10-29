# -*- coding: UTF-8 -*-
from datetime import date
from observadores import (envia_por_email,
    salva_no_banco, imprime)

class Item(object):

    def __init__(self, descricao, valor):
        self.__descricao = descricao
        self.__valor = valor

    @property
    def descricao(self):
        return self.__descricao

    @property
    def valor(self):
        return self.__valor

class Nota_fiscal(object):

    def __init__(self, razao_social, cnpj, itens, data_de_emissao=date.today(), detalhes='', observadores = []):
        self.__razao_social = razao_social
        self.__cnpj = cnpj
        self.__data_de_emissao = data_de_emissao
        if(len(detalhes) > 20):
            raise NameError('Detalhes da nota não pode ter mais do que 20 caracteres')
        self.__detalhes = detalhes
        self.__itens = itens

        for observador in observadores:
            observador(self)

    @property
    def razao_social(self):
        return self.__razao_social

    @property
    def cnpj(self):
        return self.__cnpj

    @property
    def data_de_emissao(self):
        return self.__data_de_emissao

    @property
    def detalhes(self):
        return self.__detalhes


if __name__ == '__main__':

    lista_itens = [Item('prato', 10.0), Item('copo', 5.0)]

    nota_fiscal = Nota_fiscal(
        razao_social = 'EMPRESA TESTE',
        cnpj = '11888999000198',
        itens = lista_itens,
        observadores = [envia_por_email, salva_no_banco, imprime]
    );

    print nota_fiscal;
