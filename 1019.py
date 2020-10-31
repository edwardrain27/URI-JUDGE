

second = int(input())

hours = second // 3600
r1 = second%3600
minutes = r1//60
r2=r1%60
seconds=r2

print('{}:{}:{}'.format(hours,minutes,seconds))

