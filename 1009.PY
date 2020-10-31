name = input('')
salary = float(input())
salesPerMonth = float(input())

total = salary + salesPerMonth*0.15

print('TOTAL = R$ {:.2f}'.format(total))