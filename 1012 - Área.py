def areaTriangulo(A, C):
    return A * C / 2

def areaCirculo(A):
    pi = 3.14159
    return pi *A**2

def areaTrapezio(A, B, C):
    return (A + B) * C / 2

def areaQuadrado(B):
    return B**2

def areaRetangulo(A,B):
    return A*B

Lista1 = input().split()

val1 = float(Lista1[0])
val2 = float(Lista1[1])
val3 = float(Lista1[2])

str1 = f"""TRIANGULO: {areaTriangulo(val1, val3):.3f}
CIRCULO: {areaCirculo(val3):.3f}
TRAPEZIO: {areaTrapezio(val1,val2,val3):.3f}
QUADRADO: {areaQuadrado(val2):.3f}
RETANGULO: {areaRetangulo(val1,val2):.3f}
"""

print(str1)