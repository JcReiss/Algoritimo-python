
#? Você foi contratado para desenvolver uma solução simples para uma loja. 
#? A loja está realizando uma promoção em que todos os produtos terão um desconto de 10% aplicado no preço original.
#? Sua tarefa é criar um pequeno programa que automatize esse processo, aplicando o desconto automaticamente para todos os produtos da loja.
#? A lista de preços dos produtos já está disponível, e você precisa aplicar o desconto de forma eficiente, usando as ferramentas de programação map e função.
#? Seu objetivo é garantir que todos os preços atualizados com desconto sejam exibidos corretamente para os clientes da loja.

'''
precos = [299, 200,  499, 300, 400, 559, 1500]  
desconto=list(map(lambda x: x*0.1, precos))
 
print(desconto)
'''


#? Você terá que desenvolver um sistema de controle de entrada em uma boate chamada "Boate Azul". 
#? Para garantir que a boate siga as regras, apenas pessoas com 18 anos ou mais podem entrar.
#? Sua tarefa é criar um programa que receba a idade de 10 pessoas que estão na fila para entrar na boate. 
#? Depois disso, o programa deve verificar, de forma automática, quem tem permissão para entrar, utilizando as ferramentas list,  filter e função.
#? O objetivo é garantir que somente as pessoas com a idade mínima exigida possam entrar, e o sistema deve exibir a lista de idades que foram autorizadas a entrar na boate.

'''
idades = [18, 25, 36, 22, 21, 24, 17, 30, 32, 31, 28, 29, 16, 15, 54]
idades_maiores = [] 
def verificar_idades(idades):
    if idades>=18:
         return True

    else:
         return False;
     
idades_maiores=list(filter(verificar_idades,idades))
print(idades_maiores)
'''

#?
'''
nomes = []
saldos = []

def criar_conta(nome, saldo=0):
    nomes.append(nome)
    saldos.append(saldo)

def depositar(indice, valor):
    saldos[indice] = saldos[indice] + valor
    print(f"Depósito de R${valor} realizado com sucesso.")

def sacar(indice, valor):
    if saldos[indice] >= valor:
        saldos[indice] = saldos[indice] - valor
        print(f"Saque de R${valor} realizado com sucesso.")
    else:
        print("Saldo insuficiente.")

def consultar_saldo(indice):
    print(f"O saldo da conta de {nomes[indice]} é R${saldos[indice]}.")

def acessar_conta(nome, saldo):
    while True:
        print("\nEscolha uma operação:")
        print("1 - Depósito")
        print("2 - Saque")
        print("3 - Saldo")
        print("4 - Sair")
        opcao = int(input("Digite a opção desejada: "))

        indice = nomes.index(nome)

        if opcao == 1:
            valor = float(input("Digite o valor do depósito: "))
            depositar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 2:
            consultar_saldo(indice)
            valor = float(input("Digite o valor do saque: "))
            sacar(indice, valor)
            consultar_saldo(indice)
        elif opcao == 3:
            consultar_saldo(indice)
        elif opcao == 4:
            break
        else:
            print("Opção inválida. Tente novamente.")

def solicita_nome():
    return input("Digite o nome do titular da conta: ")

def solicita_saldo():
    return float(input("Digite o saldo inicial: "))

while True:
    print("\nEscolha uma operação:")
    print("1 - Criar conta")
    print("2 - Acessar a conta")
    print("3 - Sair")
    resposta = int(input())

    if resposta == 1:
        nome = solicita_nome() 
        saldo = solicita_saldo() 
        criar_conta(nome, saldo)
    elif resposta == 2:
        nome = solicita_nome()  
        if nome in nomes: 
            acessar_conta(nome)
        else:
            print("Conta não encontrada.")
    elif resposta == 3:
        break
    else:
        print("Opção inválida. Tente novamente.")

'''


#? O setor de recursos humanos de uma empresa te chamou para ajudar na automatização do cálculo de impostos sobre os salários dos funcionários. 
#? A empresa precisa calcular 5% de imposto de IR e 4% de imposto de INSS sobre cada salário e quer que você desenvolva um programa para realizar essa tarefa de forma automática.
#? Sua tarefa é criar um programa que receba a lista de salários dos funcionários e calcule o valor do imposto a ser descontado de cada um. Para isso, utilize map, list, e função.
#? Ao final, o programa deve exibir os valores de impostos que serão descontados para cada funcionário.
'''
salarios = [2000, 6874, 3000, 6200, 5000, 8000, 5550, 7500, 2500, 1489]  
imposto_desconto = []

IR = 0.04
INSS = 0.05

imposto_desconto = list(map(lambda x: x * (IR + INSS), salarios))
print(imposto_desconto)


'''
#?
'''
media_notas = []

for i in range (3):
    aluno_notas = []
    print(f"Digite as notas dos alunos {i+1}:")
    notas = 0
    for j in range (2):
        nota = float(input(f"Nota {j+1}:"))
        notas+= nota
        aluno_notas.append(nota)
        media = notas/2
        media_notas.append(media)
for x in media_notas:
    if x >= 6:
        print(f"A media do aluno {i+1} é {x: .2f}, ou seja, ele esta aprovado!")
    else:
        print(f"A media do aluno {i+1} é {x: .2f}, ou seja, ele esta reprovado!")    
'''



#? Você está desenvolvendo um sistema para uma loja de informática que precisa aplicar um desconto de 20% em todos os preços de produtos acima de R$100,00.
#? Sua tarefa é criar um programa que, com base em uma lista de preços, aplique o desconto apenas aos produtos que custam mais de R$100,00 e mantenha os outros preços inalterados.
#? Seu programa deve usar uma função para calcular o desconto e os conceitos de "list comprehension" para aplicar essa função.

precos = [189, 250, 40, 150, 34, 171 , 99 , 80, 70, 101]  

descPrecos = [preco - (preco * 0.2) for preco in precos if preco > 100]

print(descPrecos)