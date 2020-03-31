# Exercicio calcular salario

import ac02


def verifica_funcoes1():
    try:
        salario = ac02.calcular_salario(
            ["Josuel", "email@email.com", 5000.00, "DESENVOLVEDOR"])
        assert salario == 4000.0
    except AssertionError:
        print('erro:', salario, 'Valor correto: 4000.0')
    else:
        print(salario, 'OK')


def verifica_funcoes2():
    try:
        salario = ac02.calcular_salario(
            ["Amanda", "email@email.com", 2200.00, "DESENVOLVEDOR"])
        assert salario == 1980.0
    except AssertionError:
        print('erro:', salario, 'Valor correto: 1980.0')
    else:
        print(salario, 'OK')


def verifica_funcoes3():
    try:
        salario = ac02.calcular_salario(
            ["Josefa", "email@email.com", 2500.00, "GERENTE"])
        assert salario == 2000.0
    except AssertionError:
        print('erro:', salario, 'Valor correto: 2000.0')
    else:
        print(salario, 'OK')


def verifica_funcoes4():
    try:
        salario = ac02.calcular_salario(
            ["Renato", "email@email.com", 8000.00, "GERENTE"])
        assert salario == 5600.0
    except AssertionError:
        print('erro:', salario, 'Valor correto: 5600.0')
    else:
        print(salario, 'OK')


def verifica_funcoes5():
    try:
        salario = ac02.calcular_salario(
            ["Rafael", "email@email.com", 550.00, "ANALISTA"])
        assert salario == 467.50
    except AssertionError:
        print('erro:', salario, 'Valor correto: 467.50')
    else:
        print(salario, 'OK')


def verifica_funcoes6():
    try:
        salario = ac02.calcular_salario(
            ["Jonatas", "email@email.com", 3000.00, "ANALISTA"])
        assert salario == 2250.0
    except AssertionError:
        print('erro:', salario, 'Valor correto: 2250.0')
    else:
        print(salario, 'OK')


verifica_funcoes1()
verifica_funcoes2()
verifica_funcoes3()
verifica_funcoes4()
verifica_funcoes5()
verifica_funcoes6()

