numbers = []
reserv = str() #
while True:
    try:        #Проверяем на число
        a = input()
        reserv = a
        a = int(a)
        numbers.append(a)
    except: #Есди вводили строку то проверка команды
        if reserv == 'Stop' or reserv == 'stop':
            break
        else:
            print("Ошибка команды")
more_num = numbers[0]
try:
    for i in numbers:
        if i > more_num: #Отслеживаем проверяем на большее число
            more_num = i
    print(more_num)
except:
    print("Вы не ввели число")