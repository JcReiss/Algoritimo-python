

##* 1 Dada a lista acima, crie um algoritimo para exibir as palavras com ''rr'' e ''ss''
'''
palavras= ["massa", "carro", "correr", "sol", "rir", "corrida", "ousado", "ressaca", "carroça",
           "cor", "muscular", "dor", "asa", "sonar", "assessor", "rua", "massagista", "sentimento",
           "passaporte", "acessoria", "obstáculos", "massagem", "resasaltar", "azul" ]
novaspalavras= [x for x in palavras if "rr" in x]
novalista= [x for x in palavras if "ss" in x]
print(novalista)
print(novaspalavras)
'''





##* 2 Dada a lista acima, filtre as palavras terminadas em "ar"
palavras= ["massa", "carro", "correr", "sol", "rir", "corrida", "ousado", "ressaca", "carroça",
           "cor", "muscular", "dor", "asa", "sonar", "assessor", "rua", "massagista", "sentimento",
           "passaporte", "acessoria", "obstáculos", "massagem", "resasaltar", "azul" ]
<<<<<<< HEAD
novalista=  [x for x in palavras if x.endswith("ar")]
print (novalista)
'''

=======
novalita=  [x for x in palavras if x.endswith("ar")]
print (novalita)
>>>>>>> 3de8b989e20190e0a5e7f1c3471c50a1fa8977ab




'''
##* 3 insira em uma lista secundaria as palvras iniciadas com "c"
palavras= ["massa", "carro", "correr", "sol", "rir", "corrida", "ousado", "ressaca", "carroça",
           "cor", "muscular", "dor", "asa", "sonar", "assessor", "rua", "massagista", "sentimento",
           "passaporte", "acessoria", "obstáculos", "massagem", "resasaltar", "azul" ]
novalista=  [x for x in palavras if x.startswith("c")]
print (novalista)
'''






'''
##* 4 dada a lista acima crie um algoritimo usando filter que filtre os numeros múltiplos de 3 ou 5

numeros= [9,56,45,59,555,489,723,220,49,87,74,71,51,76,125,265,433]
novalista =
print (novalista)
'''







##* 5 dada a lista acima, filtre os numeros multiplos de 3, exiba-os na tela, e em seguida exiba esses múltiplos de 3 somados a 5 cada um
'''
numeros= [9,56,45,59,555,489,723,220,49,87,74,71,51,76,125,265,433]
novalista = [x for x in numeros if x%3 ==0]

print (novalista)
'''





##* 6 dada a lista a cima filtre os numeros 3 ou 4 exiba-os na tela, em seguida exiba esses multiplos de 3 multiplicado por 3 cada um, e os numeros de 4 subtraidos de 2, cada um
'''
numeros= [9,56,45,59,555,489,723,220,49,87,74,71,51,76,125,265,433]
def filtrar (numero):

    if numero == 3 or 4:
        return True

    else:

        return False;

listarnumero= list(filter(filtrar, numeros))

print(listarnumero)
'''