#https://www.acmicpc.net/problem/5585

coins = [500,100,50,10,5,1]

left = 1000 - int(input())
count = 0

for i in coins:
    count += left // int(i)
    left = left % int(i)

print(count)
