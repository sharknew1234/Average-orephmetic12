from time import sleep
from os import system

system('cls||clear')
def arif(num1, num2, num3):
    if num1.isnumeric() and num2.isnumeric():
        listnum = [int(num1), int(num2), int(num3)]
        c = int(num1) + int(num2) + int(num3)
        print('Sum of 2 numbers:',str(c))
        sleep(0.2)
        print('Average orephmetic:')
        print(c / len(listnum))
    else:
        print('No number')

num1 = input('Enter the one num:')
num2 = input('Enter the two num:')
num3 = input('Enter the there num:')

arif(num1, num2, num3)