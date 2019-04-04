import random
#import lib1
##Цикл while
'''

num=10
while num !=0:
	print('NUM=',num)
	num-=1
print("No more num")


def rekursia():
    print('rekursia')
    return rekursia()

#rekursia()
'''    
## Проверка пароля
'''    
pwd = ''
while pwd != 'password':
    pwd = input('Введите пароль:')
    
print ("password is correct")
'''
#game
'''
size = int(random.randint(2,6))
rez = 1

while size != rez:
    rez =int(input('Enter the number '))
    
print('yuo win number is ',size)

'''
#try
"""
delimoe = int(input())
delitel = int(input())

try:
    print(delimoe/delitel)
except ZeroDivisionError:
    print('divizion by zero')
"""

#Цикл for
'''
strin ="hello"

for i in strin:
    print(i)
    if i == 'e':
        print ('e')
    
for i in range (10,20):
    print(i)
'''

#Ветвление if
'''
value1=lib1.gen_value()

if value1 ==2:
    print('value is 2')
elif value1 == 3:
    print('value is 3')
else:
    print('value isn\'t 2 and isn\'t 3')
    
'''

############################### Домашнее задание ###############################

z1 = ''' 
1)Даны три числа. Вывести на экран “yes”, если среди них есть одинаковые, иначе вывести “ERROR”;

'''

print(z1)

n1=int(input('Enter 1 number: '))
n2=int(input('Enter 2 number: '))
n3=int(input('Enter 3 number: '))



if n1 == n2:
    print("yes")
elif n2 == n3:
    print("yes")
elif n1 == n3:
    print("yes")
else:
    print("ERROR")
    
z2 = '''
2)Даны три числа. Вывести на экран “yes”, если можно взять какие-то два из них и в сумме получить третье;

'''

print(z2)

if n1+n2 == n3:
    print('yes')
elif n2+n3 == n1:
    print('yes')
elif n1+n3 == n2:
    print('yes')
    
z3 = ''' 
3)Посчитать сумму числового ряда от 0 до 14 включительно. Например, 0+1+2+3+…+14;
'''

print(z3)

zn =0
for i in range(15):
    zn+=i
print('Значение: ',zn)    

z4 = '''
4)Распечатывать дни недели с их порядковыми номерами. 
 Кроме того, рядом выводить выходной ли это день или рабочий.
 '''
 
print(z4)

week = ['Понедельник','Вторник','Среда','Четверг','Пятница','Суббота','Воскресенье']
work = ['Рабочий','Рабочий','Рабочий','Рабочий','Рабочий','Выходной','Выходной']

for i in range(len(week)):
    print(i+1,') ',week[i],' - ',work[i])
    