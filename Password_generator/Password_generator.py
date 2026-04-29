import random

numbers = [1,2,3,4,5,6,7,8,9,0]
letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
choose = 0
password = []
print("Привет, это генератор паролей! Введи длину желанного пароля")

try:
    long = int(input())
except ValueError:
    print("Ошибка вы ввели не число")
    long = int(input("Введи число: "))
print("Выбери вид пароля: 1 - только цифры; 2 - только буквы; 3 - все вместе")

try:
    choose = int(input())
except ValueError:
    print("Ошибка вы ввели не число")
    choose = int(input("Введите число: "))
    
if choose == 1:
    for i in range(long):
        password.append(random.choice(numbers))
if choose == 2:
    for i in range(long):
        password.append(random.choice(letters))
if choose == 3:
    all_symbols = "0123456789" + letters
    for i in range(long):
        password.append(random.choice(all_symbols))



print("Ваш пароль:")
print(*password, sep='')
