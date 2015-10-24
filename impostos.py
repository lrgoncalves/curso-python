# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Imposto(object):
    """docstring for Imposto"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def calcula(self, orcamento):
        pass

    @abstractmethod
    def verifica_taxa_maxima(self, orcamento):
        pass;

    @abstractmethod
    def aplica_taxa_maxima(self, orcamento):
        pass;

    @abstractmethod
    def aplica_taxa_minima(self, orcamento):
        pass;

class ICMS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1

class ISS(object):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06

class ICPP(Imposto):
    def calcula(self, orcamento):
        if self.verifica_taxa_maxima(orcamento):
            return self.aplica_taxa_maxima(orcamento)
        else:
            return self.aplica_taxa_minima(orcamento)

    def verifica_taxa_maxima(self, orcamento):
        return (orcamento.valor > 500)

    def aplica_taxa_maxima(self, orcamento):
        return orcamento.valor * 0.07

    def aplica_taxa_minima(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(Imposto):
    def calcula(self, orcamento):
        if self.verifica_taxa_maxima(orcamento):
            return self.aplica_taxa_maxima(orcamento)
        else:
            return self.aplica_taxa_minima(orcamento)

    def verifica_taxa_maxima(self, orcamento):
        return (orcamento.valor > 500 and self.__tem_item_maior_que_100_reais(orcamento))

    def aplica_taxa_maxima(self, orcamento):
        return orcamento.valor * 0.10

    def aplica_taxa_minima(self, orcamento):
        return orcamento.valor * 0.06

    def __tem_item_maior_que_100_reais(self, orcamento):
        for item in orcamento.obtem_itens():
            if (item.valor > 100):
                return true
            return false
