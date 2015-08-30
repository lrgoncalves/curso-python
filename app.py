# -*- coding: UTF-8 -*-

import re

def cadastrar(nomes):
	print ('Digite o nome')
	nome = raw_input()
	nomes.append(nome)

def listar(nomes):
	print 'Listando nomes:'
	for nome in nomes:
		print nome

def remover(nomes):
	print 'qual nome?'
	nome = raw_input()
	nomes.remove(nome)

def alterar(nomes):
	print 'qual nome?'
	nome = raw_input()
	if (nome in nomes):
		print 'novo nome para %s:' % (nome)
		indice = nomes.index(nome)
		nomes[indice] = raw_input()
	else:
		print '%s não encontrado' % (nome)

def procurar(nomes):
	print 'digite um nome:'
	nome = raw_input()
	if (nome in nomes):
		print '%s encontrado' % (nome)
	else:
		print '%s nao encontrado' % (nome)

def procurar_regex(nomes):
	print('Digite a expressao regular')
	regex = raw_input()
	nomes_concatenados = ' '.join(nomes)
	resultados = re.findall(r'('+regex+')', nomes_concatenados);
	print resultados

def menu():
	nomes = []
	escolha = ''
	while (escolha != '0'):
		print '0 - sair, 1 - cadastrar, 2 - listar, 3 - remover, 4 - alterar, 5 - procurar, 6 - regex'
		escolha = raw_input()

		if (escolha == '1'):
			cadastrar(nomes)

		if (escolha == '2'):
			listar(nomes)

		if (escolha == '3'):
			remover(nomes)

		if (escolha == '4'):
			alterar(nomes)

		if (escolha == '5'):
			procurar(nomes)

		if (escolha == '6'):
			procurar_regex(nomes)
menu()
