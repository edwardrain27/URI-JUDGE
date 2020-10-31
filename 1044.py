
numbers = input().split(' ')

numbers = [int(x) for x in numbers] 

a = numbers[0]
b = numbers[1]

if a%b == 0 or b%a == 0:
    print('Sao Multiplos')

else:
    print('Nao sao Multiplos')