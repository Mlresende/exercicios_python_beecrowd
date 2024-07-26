def maiorABS(A, B, C):
    maiorAB = (A+B+abs(A - B))/2
    return (maiorAB + C +abs(maiorAB - C))/2

lista01 = input().split()
valA = int(lista01[0])
valB = int(lista01[1])
valC = int(lista01[2])

print(f"{maiorABS(valA,valB, valC):.0f} eh o maior")