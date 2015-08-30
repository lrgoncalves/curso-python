# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa
        self.__curtidas = 0

    def imprimir(self):
        print 'Nome: %s, telefone: %s, empresa: %s, curtidas: %s' % (self.nome, self.telefone, self.empresa, self.__curtidas)

    def curtir(self):
        self.__curtidas+=1

    def obter_curtidas(self):
        return self.__curtidas


class Pessoa(object):
    'Classe para pessoa'

    def __init__(self, nome, peso, altura):
        self.nome = nome
        self.peso = peso
        self.altura = altura

    def imprimeImc(self):
        imc = self.altura * self.altura
        imc = self.peso / self.altura
        print 'Imc de %s: %s' % (self.nome, imc)
