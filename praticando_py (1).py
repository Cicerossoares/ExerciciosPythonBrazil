# -*- coding: utf-8 -*-
"""praticando.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1I_wMv9P3g_nohA_bWcugiZZx_Ct6tmtt
"""

numero = 329

centenas_str = dezenas_str = unidades_str = ''

centenas_int, numero = divmod(numero, 100)

partes_numericas =0

if centenas_int == 1:
  centenas_str = '1 centena'
elif centenas_int > 1:
  centenas_str = f'{centenas_int} centenas'
  
  
  dezenas_int, numero = divmod(numero, 10)

if dezenas_int == 1:
  dezenas_str = '1 dezena'
elif dezenas_int > 1:
  dezenas_str = f'{dezenas_int} dezenas'


if numero == 1:
  unidades_str = '1 unidade'
elif numero > 1:
  unidades_str = f'{numero} unidades'

partes_numericas == 0
print()


print(centenas_str, dezenas_str, unidades_str)

"""EXERCICIO

"""

pop_a = int(input('Digite Populaçao de A : '))
pop_b = int(input('Digite Populaçao de B : '))
taxa_de_crescimento_a = 1.03
taxa_de_crescimento_b = 1.015
anos = 0

while pop_a < pop_b:
  #print(f'######## Populaçao no Ano {anos}')
  #print(f'Populaçao A {pop_a}')
  #print(f'Populaçao B {pop_b}')
  anos += 1

  pop_a = int(pop_a * taxa_de_crescimento_a)
  pop_b *= taxa_de_crescimento_b
  pop_b = int(pop_b)

print(f'######## Populaçao no Ano : {anos}')
print(f'Populaçao A : {pop_a}')
print(f'Populaçao B : {pop_b}')

"""EXERCICIO"""

maximo = float(input('Digite o Valor : '))

for _ in range(2):
  maximo = max(maximo, float(input('Digite o Valor : ')))
  print(f'Numero maximo encontrado ate agora : {maximo}')

"""EXERCICIO"""

soma = float(input('Digite o Valor : '))

for n in range(2, 6):
  soma += float(input('Digite o Valor : '))
  media = soma / n

  print(f'A soma dos número é : {soma} a media é : {media}')

"""Exercicio"""

lista = []
for _ in range(3):
   numero = int(input('Digite um numero : '))
   lista.append(numero)
print(f'Números adicionados a atualmente {lista}')

"""Exercicio"""

lista = []
for _ in range(10):
   numero = int(input('Digite um numero : '))
   lista.append(numero)
lista.reverse()
print(f'Números adicionados a atualmente {lista}')

"""EXERCICIO !"""

notas = []

while True:
  entrada = input('Digite um numero : ')
  if entrada == '-1':
   break
  notas.append(float(entrada))


tamanho = len(notas)
print(f'Total de notas {tamanho}')
print(' '.join ([str(nota) for nota in notas]))
notas.reverse()

for nota in notas:
  print(nota)

soma = sum(notas)
print(f'A soma das notas é : {soma}') 

media = soma / tamanho
print(f'A media é : {media}')

print('Notas acima da media: ')

print(' '.join ([str(nota) for nota in notas if nota > media ]))

print('Notas abaixo da media: ')

print(' '.join ([str(nota) for nota in notas if nota < media ]))

print('FINALIZADO PROGRAMA DE ESTATISTICA DE NOTAS.')

"""Exercicio

# `Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:`
$200 - $299
$300 - $399
$400 - $499
$500 - $599
$600 - $699
$700 - $799
$800 - $899
$900 - $999
$1000 em diante

```
# Isto está formatado como código
```


# Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
"""

salarios = [200, 250, 350, 477, 530, 620, 764, 810, 999, 1000, 2000, 3000]
contagem_faixa_salario = [0] * 9
for salario in salarios:
  indice = salario // 100 -2
  indice_maximo = len(contagem_faixa_salario) -1
  indice = min(indice, indice_maximo)
  contagem_faixa_salario[indice] += 1

print(contagem_faixa_salario)

"""exercicio

Faça um programa para imprimir:



    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.

```
# Isto está formatado como código
```


"""

n = int = 5
def imprimir_triangunlo_numeros(n: int):
  for i in range(1, n + 1):
    for _ in range(i):
     print(i, end= '   ')
    print('')  


#print('Triangulo com 1')   
#imprimir_triangunlo_numeros(1)
#print('Triangulo com 2')   
#imprimir_triangunlo_numeros(2)
#print('Triangulo com 3')   
#imprimir_triangunlo_numeros(3)

print(f'Triangulo com {n}')   

imprimir_triangunlo_numeros(n)

print('Exercicio concluido')

"""Exercicio

Faça um programa para imprimir:


    1
    1   2
    1   2   3
    .....
    1   2   3   ...  n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.










"""

def imprimir_triangunlo_numeros_crescentes(n: int):
  for linha in range(1, n + 1):
    for coluna in range(1, linha + 1):
     print(coluna, end= '   ')
    print('')  


print('Triangulo com 1')   
imprimir_triangunlo_numeros_crescentes(1)
print('Triangulo com 2')   
imprimir_triangunlo_numeros_crescentes(2)
print('Triangulo com 3')   
imprimir_triangunlo_numeros_crescentes(3)

"""Exercicio

Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings

String 1: Brasil Hexa 2006

String 2: Brasil! Hexa 2006!

Tamanho de "Brasil Hexa 2006": 16 caracteres

Tamanho de "Brasil! Hexa 2006!": 18 caracteres

 As duas strings são de tamanhos diferentes.

As duas strings possuem conteúdo diferente.
"""

s1 = input('Digite uma string: ')
s2 = input('Digite outra string: ')
tamanho1 = len(s1)
tamanho2 = len(s2)

print(f'"{s1}" : {tamanho1}')
print(f'"{s2}" : {tamanho2}')

comparaçao_de_tamanhos = 'diferentes'
comparaçao_de_conteudo = 'diferente'

if s1 == s2:
  comparaçao_de_tamanhos = 'iguais'
  comparaçao_de_conteudo = 'igual'

elif tamanho1 == tamanho2:
  comparaçao_de_tamanhos = 'iguais'  

print(f'As duas strings são de tamanhos {comparaçao_de_tamanhos}.')
print(f'As duas strings possuem conteúdo {comparaçao_de_conteudo}.')

"""Exercicio

Nome ao contrário em maiúsculas. Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas.
"""

nome = input('Digite seu nome : ')
nome.upper()

nome_invertido_por_letras = ''.join(reversed(nome))
nome_invertido_por_letras.upper()

nome_invertido_por_palavras = ' '.join(reversed(nome.split()))

print(f'Nome ao contrario em maiusculo {nome.upper()}')
print(f'Nome ao contrario em letras maiusculas {nome_invertido_por_letras.upper()}')
print(f'Nome ao contrario por palavras em maiusculas {nome_invertido_por_palavras.upper()}')

"""Exercicio

Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes de ser enforcado.

Digite uma letra: A

-> Você errou pela 1ª vez. Tente de novo!

Digite uma letra: O

A palavra é: _ _ _ _ O

Digite uma letra: E

A palavra é: _ E _ _ O

Digite uma letra: S

-> Você errou pela 2ª vez. Tente de novo!
"""

palavra = 'devpro'.upper()

print('Jogo da Forca')
print('Descubra a palavra')

print('A palavra é: ', end='')
for letra in palavra:
  print(f'_ ', end='')

conjunto_letras_palavras = set (palavra)  
conjunto_letras_digitadas = set ()
erros=0

while not (conjunto_letras_palavras.issubset(conjunto_letras_digitadas)) and erros < 7:
  print()
  print()
  letra_digitada = input('Digite uma letra : ').upper()
  conjunto_letras_digitadas.add(letra_digitada)
  if letra_digitada in conjunto_letras_palavras:
    print('A palavra é: ', end='')
    for letra in palavra:
       if letra in conjunto_letras_digitadas:
        print(f'{letra} ', end='')
       else:
        print (f'_ ', end='')
  else:
    erros += 1
    print(f' Erros {erros} de 7. Tente denovo !')


  print()
  print('Letras ja digitadas : ', conjunto_letras_digitadas)
    
if erros < 7:
      print('Voce conseguiu Parabéns !') 
else:
      print('Infelizmente voce perdeu !')

"""Teste :"""

nome = input('Digite seu nome : ').upper()
print(f'Aqui está seu nome : {nome}')

"""Exercicio 

Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO

FULAN

FULA

FUL

FU

F

"""

s = 'FULANO'
while s != '':
 print(s)
 s = s[:-1]

"""exercicio

Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.
O arquivo de entrada possui o seguinte formato:

200.135.80.9

192.168.1.1

8.35.67.74

257.32.4.5

85.345.1.2

1.2.3.4

9.8.234.5

192.168.0.256
"""

def validar(ip:str) ->bool:
  numeros = ip.split('.')
  if len(numeros) != 4:
   return False
  for n in numeros:
    if not(0 <= int(n) <=255):
     return False
  return True

ips_validos = []
ips_invalidos = []

with open('sample_data/ips.txt', 'r') as arquivo:
  for linha in arquivo:
    ip = linha.strip()
    if validar(ip):
      ips_validos.append(ip)
    else:
      ips_invalidos.append(ip) 

with open('sample_data/ips.saida.txt', 'w') as arquivo:
  arquivo.writelines('[Endereços válidos:]\n')

  for ip in ips_validos:
    arquivo.writelines(f'{ip}\n')

  arquivo.writelines('\n')
  arquivo.writelines('\n')
  arquivo.writelines('[Endereços inválidos:]\n')  


  for ip in ips_invalidos:
    arquivo.writelines(f'{ip}\n')

"""Exercicio

A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":

alexandre       456123789

anderson        1245698456

antonio         123456456

carlos          91257581

cesar           987458

rosemary        789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa que gere um relatório, chamado "relatório.txt", no seguinte formato:


ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário        Espaço utilizado     % do uso


1    alexandre       434,99 MB             16,85%

2    anderson       1187,99 MB             46,02%

3    antonio         117,73 MB              4,56%

4    carlos           87,03 MB              3,37%

5    cesar             0,94 MB              0,04%

6    rosemary        752,88 MB             29,16%


Espaço total ocupado: 2581,57 MB

Espaço médio ocupado: 430,26 MB

"""