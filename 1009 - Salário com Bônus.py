sellerName = input()
grossWage = float(input())
commission = (float(input()) * 0.15)

sumSalary = grossWage + commission

print("TOTAL = R$", "{:.2f}".format(sumSalary))