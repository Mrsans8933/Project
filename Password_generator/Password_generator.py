import random
numbers = [1,2,3,4,5,6,7,8,9,0]
bukvi = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
choose = 0
password = []
print("Привет, это генератор паролей! Введи длину желанного пароля")
long = int(input())
print("Выбери вид пароля: 1 - только цифры; 2 - только буквы; 3 - все вместе")
choose = int(input())
if choose == 1:
    for i in range(long):
        password.append(random.choice(numbers))
if choose == 2:
    for i in range(long):
        password.append(random.choice(bukvi))
if choose == 3:
    all = "0123456789" + bukvi
    for i in range(long):
        password.append(random.choice(all))




print(*password)