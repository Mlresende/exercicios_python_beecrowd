from tokenize import Double


a = float(input())
b = float(input())

pesoA = 3.5
pesoB = 7.5

media = ((a*pesoA)+(b*pesoB))/(pesoA+pesoB)

print("MEDIA =", "{:.5f}".format(media))