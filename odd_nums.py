'''
Take an integer input from the user , print odd numbers from 1 to N
'''

N = int(input())
num = 1

while num <= N :
    if num % 2 == 1 :
        print(num)
    num += 1