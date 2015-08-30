# -*- coding: UTF-8 -*-

class Perfil(object):
    'Classe padrão para perfis de usuários'

    def __init__(self, nome, telefone, empresa):
        self.nome = nome
        self.telefone = telefone
        self.empresa = empresa

    def imprimir(self):
        print 'Nome: %s, telefone: %s, empresa: %s' % (self.nome, self.telefone, self.empresa)
