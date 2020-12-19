import math

vetor =[]


for i in range(10):
    if i % 2 == 0:
       vetor.append(round(3**i + 7*(math.factorial(i)),4))

    else:
        vetor.append(round(2**i + 4*(math.log(i)),4))
        
print ('O vetor é formado pelos seguintes valores',(vetor))

maiorVetor= vetor[0]
posicao= 0
media=0
for i in range(len(vetor)):
    media= media + vetor[i]
    if maiorVetor <= vetor[i]:
        maiorVetor= vetor[i]
        posicao= i
        


print ('')
print('')
print (' A posição do maior elemento do vetor é', (posicao+1),'valor de',(maiorVetor),'e, a média dos elementos contidos no vetor é', round((media/10),2))


