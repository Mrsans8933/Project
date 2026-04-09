numbers = []
reserv = str() #
while True:
    try: 
        a = input("Введи число или stop")
        reserv = a
        a = int(a)
        numbers.append(a)
    except: 
        if reserv == 'Stop' or reserv == 'stop':
            break
        else:
            print("Ошибка команды")
more_num = numbers[0]
try:
    for i in numbers:
        if i > more_num: 
            more_num = i
    print(more_num)
except:
    print("Вы не ввели число")
