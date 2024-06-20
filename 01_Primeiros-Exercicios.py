#Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input('Digite um número: '))
print('O número informado foi %s ' %numero)

#Faça um Programa que peça dois números e imprima a soma.
a = int(input())
b = int(input))
print(a + b)

#Faça um Programa que peça as 4 notas bimestrais e mostre a média.
a = int(input())
b = int(input())
c = int(input())
d = int(input())
media  = (a+b+c+d)/4
print(media)

#Faça um Programa que converta metros para centímetros.
metro =float(input('Digite quantos metros voce tem: '))
cent = metro * 100
print(cent)

#Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
pi = float(3.14)
raio = int(input('informe o raio:' ))
area = pi * (raio**2)
print(area)

#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
lado1 = int(input())
lado2 = int(input())
area = (lado1 * lado2)*2
print(area)

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
hora = int(input('Quanto vc recebe por hora? '))
horas = int(input('Quantas horas voce trabalhou? '))
print(f'Seu salário será:{hora * horas}')

#Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a temperatura em graus Celsius. C = (5 * (F-32) / 9).
F = int(input('Digite a temperatura em Farenheit: '))
C = ((5 * (F-32)) / 9)
print(f'Temperatura em Farenheit: {float(C)}°F')
tempC = ((9 * (F+32))/ 5)
print(f'Temperatura em Celsius: {float(tempC)}°C')

#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
a = int(input())
b = int(input())
c = int(input())
produto= (a*2) * b//2
print(produto)
soma = (a*3) + c
print(soma)
print(c**3)

#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = float(input('Altura: '))
peso = (72.7*altura) - 58
print(f'Em torno de {int(peso)}kg')

#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
h = float(input('Digite sua altura: '))
numero = int(input('Digite 1 para homem e 2 para mulher: '))
if numero == 1:
    print(int((72.7*h) - 58))
if numero == 2  :
    print(int((62.1*h) - 44.7))

#João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
#Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo(50 quilos)
#deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes)
#e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar.
#Imprima os dados do programa com as mensagens adequadas
peso = float(input('Digite o peso do peixe: '))
excesso = peso - 50
multa = excesso * 4
if peso > 50:
    print('A multa será aplicada para cada 1kg excedente')
    print(f'Voce tem um excesso de {excesso}kg. Portanto irá pagar uma multa no valor de: {multa} reais.')
else:
    print('A quantidade esta permitida')

#Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês,
# sabendo-se que são descontados 11% para o Imposto de Renda,
# 8% para o INSS e
# 5% para o sindicato, faça um programa que nos dê:
#salário bruto.
#quanto pagou ao INSS.
#quanto pagou ao sindicato.
#o salário líquido.
#calcule os descontos e o salário líquido, conforme a tabela abaixo:
#+ Salário Bruto : R$
#- IR (11%) : R$
#- INSS (8%) : R$
#- Sindicato ( 5%) : R$
#= Salário Liquido : R$
#Obs.: Salário Bruto - Descontos = Salário Líquido.
hora = int(input('Pagamento por hora: '))
horas = int(input('Quantas horas: '))
salario = (hora * horas)
print(f'Seu salário bruto é de {salario}.Agora vamos para os descontos... :(')
ir = 0.11 * salario
print(f'IR: {ir}')
inss = 0.08 * salario
print(f'INSS: {inss}')
sindicato = 0.05 * salario
print(f'Sindicato: {sindicato}')
sl = salario - ir - inss - sindicato
print(f'Seu salário ao final do mês com os valores descontados será:{sl}')
