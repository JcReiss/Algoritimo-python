
#?função01
'''
def mostrar_mensagem():
    print("Teste")
    
mostrar_mensagem()
'''



#?função02
'''
def soma(numero1, numero2):
    return numero1 + numero2
    print(numero1 + numero2)
    
print(soma(8, 10))
'''



#?função03
'''
def exibir_dados(nome, sobrenome, cpf, idade):
    print(f"O {nome} {sobrenome} tem {idade} anos e seu cpf é {cpf}.")
    
exibir_dados("Julio", "Reis", "07183738124", 19)
'''



#?função04
'''
soma = 0
for i in range(1,11):
    soma += i
print(soma)
'''



#?função05

'''
def celsius_para_kelvin(celsius):
    return celsius + 273.15
print(celsius_para_kelvin(31))
'''



#?função06
'''
def celsius_para_kelvin(climas):
    return climas + 273.15
climas=[15, 29, 31, 27, 23, 21, 15, 15]

novo_clima = list(map(celsius_para_kelvin, climas))
print(novo_clima)
'''



#?função07
'''
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero_ao_quadrado = []
for i in numeros:
    numeros_ao_quadrado.append(i**2)
print(numero_ao_quadrado)
'''



#?função08
'''
def juntar_nomes(nome, sobrenome):
    return nome + " " + sobrenome
print(juntar_nomes("Julio" , "Cesar"))
'''



#?função09

def juntar_nomes(nome, sobrenome):
    return nome + " " + sobrenome

nomes = []
sobrenomes = []
nomes_completos = []

for i in range(5):
    nome = input("Digite o nome:")
    sobrenome = input("Digite o sobrenome:")
    nomes_completos.append(juntar_nomes(nome, sobrenome))

print(nomes_completos)