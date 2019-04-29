import random
def criaFich(n):
    f = open("inputMAXinsertion.txt","a+")
    f2 = open("filmes.txt","r")
    f.write("%d\n" % (n))
    next(f2)
    for i in range(n):
        a = f2.readline()
        f.write(a)
    tuplo = ["DATA", "NOME", "POPULARIDADE"]
    a = random.randint(5,50)
    b = random.randint(1,n)
    c = random.randint(0,2)
    for i in range(a):
        a = random.randint(5,50)
        b = random.randint(1,n)
        c = random.randint(0,2)
        print(tuplo[0])
        d = tuplo[c]
        f.write("%s %d\n" % (d,b))
    
    f.close()
    f2.close()