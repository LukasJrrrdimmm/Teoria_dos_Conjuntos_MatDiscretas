
import math
import matplotlib.pyplot as plt
import numpy as np
lim = int(input("Digite o limite do domínio:"))
lim2 = int(input("Digite o limite do contradomínio"))
c = int(0)

vec1 = [0] * lim
vec2 = [0] * lim2
print("Digite os valores do domínio")
while c < lim:
        vec1[c] = int(input("Valor:"))
        c = c + 1
c = 0
print("Digite os valores do contradomíneo")
while c < lim2:
        vec2[c] = int(input("Valor:"))
        c = c + 1
c = 0
res = [0] * lim
a = lim
admitir = int(0)
d = int(0)
ercount = [0]*lim
imCount = int(0)
r = [0] * lim2
i = int(0)
while c < lim2:
        r[c] = [0]
        c = c + 1
c = 0
while c < lim:
        ercount[c] = [0]
        c = c + 1
c = int(0)
j = int(0)
vd = int(0)
h = int(0)
#teste = [0]*lim2
while c < lim:
        #Inserir função dentro dos colchetes.
        #o domínio é o arrey vec1.
        #o contradomíneo é o arrey vec2.
        res[c] = 2 * vec1[c] + 1
        print(res[c])
        while d < lim2:
            if res[c] == vec2[d]:
                imCount = imCount + 1
                r[i] = vec2[d]
            if c > lim2:
                break
            if vec2[d] == vec1[c]:
                ercount[c] = ercount[c] + 1
                if ercount[c] == 2:
                    vd = vec2[d]
                    while j < lim2:
                        if vd == vec2[j]:
                            h = h + 1
                        j = j + 1
                    if h < 2:
                        print("Is Not Function.")
                    else:
                        print("Is Function.")
            else:
                print("Is Function.")
            d = d + 1
        c = c + 1
if imCount == lim:
        print("Injector Function")
        admitir = admitir + 1

if imCount == lim2:
        print("Sobrejector Function")
        admitir = admitir + 1
if admitir == 2:
        print("Bijector Function")
