# Задание 1
# a = int (input('введите число:'))
# b = int (input('введите число:'))

# a,b = b,a

# print (a,b)



# Задание  2
# с = int (input('введите число:'))
# if с % 2==0:
#     print ('четное')
# else:
#     print('нечетное')


#Задание 3
# d = int (input('введите число:'))
# e = int (input('введите число:'))
# f = int (input('введите число:'))

# if d < e and d < f:
#     print (d)   
# if f < e and d < e:
#     print (f)
# if e < f and e < d:
#     print (e)

# Здание 4
# j = int (input ('введите число:'))
# sum = 0
# for i in range (1,j+1):
#     sum += i
# print (i,sum)

# Задание 5
# k  = int (input ('введите число:'))
# for i in range (1,11):
#     result = k*i
#     print (f"{k}*{i}={result}")

# Задание 6
# Ввод 5 чисел
m = int(input("Введите число: "))
n = int(input("Введите число: "))
o = int(input("Введите число: "))
p = int(input("Введите число: "))
z = int(input("Введите число: "))

# Счётчики
positive = 0
negative = 0
zero = 0

# Проверка каждого числа
for num in [m, n, o, p, z]:
    if num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        zero += 1

# Вывод результата
print("Положительных чисел:", positive)
print("Отрицательных чисел:", negative)
print("Нулей:", zero)
