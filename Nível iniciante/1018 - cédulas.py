def calculador_notas(valor):
    notas = [100, 50, 20, 10, 5, 2, 1]
    quantidade_notas = {nota: 0 for nota in notas}
    print(valor)
    for nota in notas:
        quantidade_notas[nota] = valor // nota
        valor = valor % nota
    
    for nota in notas:
        print(f"{quantidade_notas[nota]} nota(s) de R${nota},00")

valor = int(input())

calculador_notas(valor)