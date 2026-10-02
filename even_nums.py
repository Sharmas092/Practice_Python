'''
Take an integer input from the user , print even numbers from 1 to N
'''

N = int(input())
num = 1

while num <= N :
    if num %2 == 0:
        print(num)
    num += 1    