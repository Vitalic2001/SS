def NumProv(n):
    temp = True
    while temp == True:
        if n.isdigit():
            return int(n)
        else:
            print('Введите адекватное число')
            n = input()


def Dv_DS(n, u):
    s = 0
    k = '10'
    n = " ".join(n)
    for i in "ABCDEF":
        n = n.replace(i, k)
        k = str(int(k)+1)
    n = n.split()
    for i in range(len(n)):
        s +=int(n[i])*u**(len(n)-1-i)
    return s

tt = input('Выберите систему счисления \n')
tt =NumProv(tt)
oo = input('Какое число будем переводить? \n')
print(Dv_DS(oo, tt))