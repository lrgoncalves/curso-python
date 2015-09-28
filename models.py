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

    @staticmethod
    def gerar_perfis(nome_arquivo):
        perfis = []

        arquivo = open(nome_arquivo, 'r')

        for linha in arquivo:
            valores = linha.split(',')

            if(len(valores) is not 3):
                raise PerfilErro('Uma linha no arquivo deve ter 3 valores')

            perfis.append(Perfil(*valores))

        arquivo.close()

        return perfis


class Perfil_Vip(Perfil):
    'classe para perfis de usuário vip'

    def __init__(self, nome, telefone, empresa, apelido):
        super(Perfil_Vip, self).__init__(nome, telefone, empresa)
        self.apelido = apelido

    def obter_creditos(self):
        return super(Perfil_Vip, self).obter_curtidas() * 10.0

class PerfilErro(Exception):
    def __init(self, mensagem):
        self.mensagem = mensagem
    def __str__(self):
        return repr(self.mensagem)

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
