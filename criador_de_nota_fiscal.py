# -*- coding: UTF-8 -*-
from nota_fiscal import Nota_fiscal, Item

class Criador_de_nota_fiscal(object):

    def __init__(self):
        self.__razao_social = None
        self.__cnpj = None
        self.__data_de_emissao = None
        self.__detalhes = None
        self.__itens = None

    def com_razao_social(self, razao_social):
        self.__razao_social = razao_social
        return self

    def com_cnpj(self, cnpj):
        self.__cnpj = cnpj
        return self

    def com_data_de_emissao(self, data_de_emissao):
        self.__data_de_emissao = data_de_emissao
        return self

    def com_detalhes(self, detalhes):
        self.__detalhes = detalhes
        return self

    def com_itens(self, itens):
        self.__itens = itens
        return self

    def constroi(self):
        if (self.__razao_social is None):
            raise NameError('Razão social deve ser preenchida')
        if (self.__cnpj is None):
            raise NameError('cnpj deve ser preenchida')
        if (self.__itens is None):
            raise NameError('itens deve ser preenchida')

        return Nota_fiscal(
            razao_social = self.__razao_social,
            cnpj = self.__cnpj,
            data_de_emissao = self.__data_de_emissao,
            detalhes = self.__detalhes,
            itens = self.__itens)


if __name__ == 'main':

    # nota_fiscal = (Criador_de_nota_fiscal()
    #     .com_razao_social('TESTE')
    #     .com_cnpj('11222333444000129')
    #     .com_data_de_emissao('2015-10-29')
    #     .com_detalhes('')
    #     .com_itens([Itens('abobora', '2.30')])
    #     .constroi()
    #     )

    nota_fiscal = (Criador_de_nota_fiscal()
        .com_razao_social('FHSA Limitada')
        .com_cnpj('012345678901234')
        .com_itens(itens)
        .constroi())

    print nota_fiscal.razao_social
    print nota_fiscal.cnpj
    print nota_fiscal.itens
    print nota_fiscal.detalhes

    print nota_fiscal.razao_social;
