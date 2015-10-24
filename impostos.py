# -*- coding: UTF-8 -*-
from abc import ABCMeta, abstractmethod

class Imposto(object):
    
    __metaclass__ = ABCMeta

    def __init__(self, outro_imposto = None):
        self.__outro_imposto = outro_imposto

    def calculo_do_outro_imposto(self, orcamento):
        if (self.__outro_imposto is None):
            return 0
        else:
            return self.__outro_imposto.calcula(orcamento)

    @abstractmethod
    def calcula(self, orcamento):
        pass

class ImpostoTemplate(Imposto):
    __metaclass__ = ABCMeta

    def calcula(self, orcamento):
        if self.verifica_taxa_maxima(orcamento):
            return self.aplica_taxa_maxima(orcamento) + self.calculo_do_outro_imposto(orcamento)
        else:
            return self.aplica_taxa_minima(orcamento) + self.calculo_do_outro_imposto(orcamento)

    @abstractmethod
    def verifica_taxa_maxima(self, orcamento):
        pass;

    @abstractmethod
    def aplica_taxa_maxima(self, orcamento):
        pass;

    @abstractmethod
    def aplica_taxa_minima(self, orcamento):
        pass;

class ICPP(ImpostoTemplate):

    def verifica_taxa_maxima(self, orcamento):
        return (orcamento.valor > 500)

    def aplica_taxa_maxima(self, orcamento):
        return orcamento.valor * 0.07

    def aplica_taxa_minima(self, orcamento):
        return orcamento.valor * 0.05

class IKCV(ImpostoTemplate):

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

class ICMS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.1 + self.calculo_do_outro_imposto(orcamento)

class ISS(Imposto):
    def calcula(self, orcamento):
        return orcamento.valor * 0.06 + self.calculo_do_outro_imposto(orcamento)
