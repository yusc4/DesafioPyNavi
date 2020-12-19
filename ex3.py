from random import* #módulo de números aleatórios

# função que inicia dicionário de notas
def iniciaDicNotas (dic):
 dic['Pedro'] = round(uniform(5, 10), 1)
 dic['João'] = round(uniform(5, 10), 1)
 dic['Tiago'] = round(uniform(5, 10), 1)
 dic['Maria'] = round(uniform(5, 10), 1)
 dic['Isabel'] = round(uniform(5, 10), 1)

# iniciar dicionário de notas
dicNotas = {}
iniciaDicNotas(dicNotas)

#variáveis auxiliares 
maiorNota= 0
aux= 0

alunos = list(dicNotas.keys())
notas = list(dicNotas.values())

maiorNota= notas[0]
for i in range(5):
    print ('O(A) Aluno(a)',(alunos[i]), 'tem a nota', (notas[i]), 'na prova.') 
    if maiorNota <= notas[i]:
        maiorNota= notas[i]
        aux= i
        
    
print ('')
print ('')
print ('O(A) Aluno(a) com maior nota é', (alunos[aux]), 'que tem', (maiorNota),'na prova.') 




