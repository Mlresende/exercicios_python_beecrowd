'''Usamos input().split() para ler a entrada e dividir os valores em uma lista de strings.'''

linha1 = input().split()
codPeca1 = int(linha1[0])
quantPeca1 = int(linha1[1])
valUnitPeca1 = float(linha1[2])

linha2 = input().split()
codPeca2 = int(linha2[0])
quantPeca2 = int(linha2[1])
valUnitPeca2 = float(linha2[2])

totalapagar = (quantPeca1*valUnitPeca1) + (quantPeca2*valUnitPeca2)

print(f"VALOR A PAGAR: R$ {totalapagar:.2f}")