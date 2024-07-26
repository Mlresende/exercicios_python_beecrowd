from math import sqrt

def distDoisPontos (A,B,C,D):
    return sqrt((x2-x1)**2+(y2-y1)**2)

ponto1 = input().split()
x1 = float(ponto1[0])
y1 = float(ponto1[1])

ponto2 = input().split()
x2 = float(ponto2[0])
y2 = float(ponto2[1])

print(f"{distDoisPontos(x1,y1,x2,y2):.4f}")