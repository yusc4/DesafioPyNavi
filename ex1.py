

def Ex1(num1, num2):
    total = 0
    for i in range(num1, num2 + 1,1):
        if i % 2 == 0:          #para saber se é par             
            total +=1            
        elif i%37 == 0:         #para saber se é múltiplo de 37   
            total +=1
        elif i%49 == 0:         #para saber se é múltiplo de 49
            total +=1
       

    return total
            
print ('Digite os números do intervalo a seguir, Exemplo do Exercício 1 - Existem no intervalo [1,5000000]', Ex1(1, 5000000), 'números que satisfazem simultaneamente serem pares, mútiplos de 37 e 49.')
print ('')
num1 = int(input("1 - Entre com o número positivo do intervalo incial >>>>: "))
num2 = int(input("2 - Entre com o número positivo do intervalo final >>>>:  "))
print ('Existem', Ex1(num1, num2))  
