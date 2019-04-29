from math import log10
from random import randint

class Filme:
    def _init_(self):
        self.lancamento = lancamento
        self.popularidade = popularidade
        self.titulo = titulo
    def stringToFilme(self,string):
        string = string.split() 
        self.lancamento = string[0]
        self.popularidade = string[1]
        list_titulo = string[2:]
        self.titulo = ' '.join(list_titulo)

def main():
    inventario = []
    input1 = input()
    num = int(input1)
    for i in range(num):
        string = input()
        filme = Filme()
        Filme.stringToFilme(filme,string)
        inventario.append(filme)
    
    sortedByDate = inventario.copy()
    sortedByPopularity = inventario.copy()
    sortedByTitle = inventario.copy()
    comando = [1,1]
    if num < 30:
        insertionSortD(sortedByDate)
        insertionSortP(sortedByPopularity)     
        insertionSortN(sortedByTitle)     
    else:
        sortedByPopularity = msort(sortedByPopularity)
        sortedByTitle = quicksortN(sortedByTitle)
        radixsort(sortedByDate)
            
    while comando[0] != "TERMINA":
        comando = input()
        comando = comando.split()
        if comando[0] == "DATA":
            print(sortedByDate[int(comando[1])-1].titulo)
        elif comando[0] == "POPULARIDADE":
            print(sortedByPopularity[int(comando[1])-1].titulo)
        elif comando[0] == "NOME":
            print(sortedByTitle[int(comando[1])-1].titulo)

def printList(arr):
    for i in range(len(arr)):
        print(arr[i].titulo)
        
def msort(x):
    if len(x) < 2:return x

    result,mid = [],int(len(x)/2)

    y = msort(x[:mid])
    z = msort(x[mid:])

    while (len(y) > 0) and (len(z) > 0):
            a = int(y[0].popularidade)
            b = int(z[0].popularidade)
            if a < b :result.append(z.pop(0))   
            else:result.append(y.pop(0))

    result.extend(y+z)
    return result

def get_digit(number, base, pos):
    return (number // base ** pos) % base

def prefix_sum(array):
    for i in range(1, len(array)):
        array[i] = array[i] + array[i-1]
    return array

def radixsort(l):
    n = len(l) # contem o tamanho do array dos Filmes
    b = [0]*n

    # Procura a menor e a maior data do array dos Filmes
    maior = menor = int(l[0].lancamento)
    for i in range(1,n):
        if(maior < int(l[i].lancamento)):
            maior = int(l[i].lancamento)
        if(menor > int(l[i].lancamento)):
            menor = int(l[i].lancamento)
            
    dif = maior - menor
    count = [0]*(dif+1) # cria um array para conter o numeros de ocorrencias de cada data
    
    for i in range(n): # guarda os numeros de ocorrencias de cada data
        count[int(l[i].lancamento) - menor] += 1
    
    for i in range(dif+1): # o array passa a conter a posicao de cada data no array de filmes
        count[i] += count[i-1]
    
    i=n-1
    while i>=0: # constroi o array de output
        b[count[int(l[i].lancamento) - menor] - 2] = l[i] # diminui a dois para encontrar a posicao do filme ordenada
        count[int(l[i].lancamento) - menor] -= 1
        i -= 1
    
    for i in range(n): # copia o output para o array de entrada
        l[i] = b[i]

def insertionSortD(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
        temp = k[j]              #temp will be used for comparison with previous items, and sent to the place it belongs
        while j > 0 and int(temp.lancamento) < int(k[j-1].lancamento): #j>0 bcoz no point going till k[0] since there is no seat available on its left, for temp
            k[j] = k[j-1] #Move the bigger item 1 step right to make room for temp
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
        k[j] = temp

def insertionSortP(k):
    for i in range(1,len(k)):
        j = i 
        temp = k[j]              #temp will be used for comparison with previous items, and s
        while j > 0 and int(temp.popularidade) > int(k[j-1].popularidade): 
            k[j] = k[j-1] 
            j=j-1 
        k[j] = temp

def insertionSortN(k):
    for i in range(1,len(k)): 
        temp = k[i]
        j = i-1
        while j >= 0 and (k[j].titulo > temp.titulo):
            k[j+1] = k[j]
            j-=1 
        k[j+1] = temp
        
def quicksortN(x):
    if len(x) == 1 or len(x) == 0:
        return x
    else:
        pivot = x[0].titulo
        i = 0
        for j in range(len(x)-1):
            aux = x[j+1].titulo
            if (min(pivot,aux) == aux):
                x[j+1],x[i+1] = x[i+1], x[j+1]
                i += 1
        x[0],x[i] = x[i],x[0]
        first_part = quicksortN(x[:i])
        second_part = quicksortN(x[i+1:])
        first_part.append(x[i])
        return first_part + second_part

main()