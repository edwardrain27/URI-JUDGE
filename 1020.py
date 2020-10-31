
days = int(input())

years = days//365
month = (days%365)//30
day = (days%365)%30

#1 ano(s)
#1 mes(es)
#5 dia(s)

print('{} ano(s)'.format(years))
print('{} mes(es)'.format(month))
print('{} dia(s)'.format(day))